#!/usr/bin/env python3
"""Track the published version of every plugin listed in this marketplace.

Claude resolves a plugin's version from its repository's `.claude-plugin/plugin.json`,
but it only re-resolves when it re-fetches the marketplace. So a plugin repo can bump
its version and no user will notice until *this* repository moves. This script is what
moves it: it reads each plugin's current version straight from its source repo and
records it in `plugin-versions.json`, producing a commit whenever something changed.

Every source repo is public, so the reads are anonymous HTTPS -- no token, no secret,
nothing to rotate. Run with --check to report drift without writing anything.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"
STATE_FILE = REPO_ROOT / "plugin-versions.json"
TIMEOUT = 30


def fetch_version(repo: str) -> str:
    """Read .claude-plugin/plugin.json from a GitHub repo's default branch."""
    url = f"https://raw.githubusercontent.com/{repo}/HEAD/.claude-plugin/plugin.json"
    req = urllib.request.Request(url, headers={"User-Agent": "oposs-plugins-version-tracker"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        manifest = json.load(resp)
    version = manifest.get("version")
    if not version:
        raise ValueError(f"{repo}: plugin.json has no 'version' field")
    return str(version)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift and exit 1 if any, without writing",
    )
    args = parser.parse_args()

    marketplace = json.loads(MARKETPLACE.read_text())
    plugins = marketplace.get("plugins", [])
    if not plugins:
        print("::error title=No plugins::marketplace.json lists no plugins", file=sys.stderr)
        return 1

    old_state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    new_state: dict[str, str] = {}
    changes: list[str] = []
    failures: list[str] = []

    for plugin in plugins:
        name = plugin["name"]
        source = plugin.get("source", {})
        if source.get("source") != "github" or not source.get("repo"):
            print(f"  {name}: skipped (not a github source)")
            continue
        repo = source["repo"]
        try:
            version = fetch_version(repo)
        except (urllib.error.URLError, ValueError, json.JSONDecodeError, OSError) as exc:
            # Keep the last known version so a transient outage cannot erase state
            # or, worse, look like a downgrade on the next successful run.
            failures.append(f"{name} ({repo}): {exc}")
            if name in old_state:
                new_state[name] = old_state[name]
            continue

        new_state[name] = version
        previous = old_state.get(name)
        if previous != version:
            changes.append(f"{name} {previous or '(new)'} -> {version}")
        print(f"  {name}: {version}" + ("" if previous == version else f"  (was {previous or 'untracked'})"))

    for gone in sorted(set(old_state) - set(new_state)):
        changes.append(f"{gone} removed from marketplace")

    for failure in failures:
        print(f"::warning title=Version lookup failed::{failure}")

    if failures and not changes:
        # Nothing to record and at least one repo unreachable: surface it rather
        # than reporting a clean run.
        return 1 if args.check else 0

    if not changes:
        print("No version changes.")
        return 0

    print("\nChanges:")
    for change in changes:
        print(f"  - {change}")

    if args.check:
        return 1

    STATE_FILE.write_text(json.dumps(dict(sorted(new_state.items())), indent=2) + "\n")
    summary = "; ".join(changes)
    Path("commit-message.txt").write_text(
        f"Track plugin versions: {summary}\n\n"
        "Recorded automatically from each plugin repository's plugin.json.\n"
        "This commit also moves the marketplace, which is what makes Claude\n"
        "re-resolve plugin versions on the next refresh.\n"
    )
    print(f"\nWrote {STATE_FILE.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

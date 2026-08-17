# OPOSS Claude Code Plugins

A [Claude Code](https://claude.com/claude-code) plugin marketplace by [OETIKER+PARTNER AG](https://www.oetiker.ch/).

## Available Plugins

| Plugin | Description |
|--------|-------------|
| **cmk-oposs-plugin** | Checkmk 2.3.x plugin development guide — SNMP, agent-based, special agents, notifications, metrics, rulesets, bakery, and MKP packaging |
| **egui-shadcn** | Build polished Rust egui/eframe GUIs from shadcn designs — a tested shadcn-v4 component module plus a layout-first workflow with headless render verification |

## Installation

Add the marketplace to Claude Code:

```
/plugin marketplace add oposs/claude-plugins
```

Then install the plugin you want:

```
/plugin install cmk-oposs-plugin@oposs-plugins
```

## Usage

Once installed, Claude automatically uses the plugin's knowledge when you ask it
to build, upgrade, or package Checkmk plugins. Example prompts:

- *"Build an SNMP plugin to monitor my Liebert UPS"*
- *"Upgrade my old v1 check plugin to the v2 API"*
- *"Create a notification plugin that sends alerts to Teams"*
- *"Package my plugin as an MKP with a GitHub Actions release workflow"*

For **egui-shadcn** (`/plugin install egui-shadcn@oposs-plugins`):

- *"Build an egui settings screen with tabs from this shadcn design"* (attach a screenshot)
- *"Port this shadcn Card and form to egui/eframe"*
- *"Make my eframe app look like shadcn"*

## Published versions

`plugin-versions.json` records the version each plugin currently publishes in its own
`.claude-plugin/plugin.json`. It is maintained by the **Track plugin versions** workflow,
which reads every plugin repository hourly and commits when a version changes.

This is not bookkeeping for its own sake. Claude resolves a plugin's version from the
plugin repository, but only re-resolves when it re-fetches this marketplace — so a plugin
can publish a new version and no user will ever see it until *this* repository moves.
The tracker's commit is what moves it.

All plugin repositories are public, so the workflow reads them over anonymous HTTPS and
writes only here, with the built-in `GITHUB_TOKEN`. It needs no PAT, deploy key or App.

## License

See individual plugin repositories for license details.

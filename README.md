# OPOSS Claude Code Plugins

A [Claude Code](https://claude.com/claude-code) plugin marketplace by [OETIKER+PARTNER AG](https://www.oetiker.ch/).

## Available Plugins

| Plugin | Description |
|--------|-------------|
| **cmk-oposs-plugin** | Checkmk 2.3.x plugin development guide — SNMP, agent-based, special agents, notifications, metrics, rulesets, bakery, and MKP packaging |

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

## License

See individual plugin repositories for license details.

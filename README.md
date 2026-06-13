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

## License

See individual plugin repositories for license details.

# agent-os 🦾

> Autonomous agent infrastructure. Self-hosted. Privacy-first. No external dependencies.

Complete operating system for running autonomous AI agents on your own infrastructure.

## Architecture

```
┌──────────────────────────────┐
│            agent-os          │
│                              │
│  ┌──────┐  ┌──────┐  ┌─────┐ │
│  │Orch  │  │Memory│  │Skill│ │
│  │estr  │  │Stack │  │Brwy │ │
│  └──┬───┘  └──┬───┘  └──┬──┘ │
│     └─┬──────┘  └──┬─────┘   │
│  ┌────┴───┴────┐    │        │
│  │  Model      │    │        │
│  │  Routing    │    │        │
│  └─────────────┘    │        │
└─────────────────────┘        │
```

## Features

| Feature | Status |
|---------|--------|
| Multi-provider LLM routing | ✅ |
| Context window compression | ✅ |
| Skill-based task execution | ✅ |
| Browser automation | ✅ (Browserbase + local) |
| Terminal access | ✅ (local, docker, ssh) |
| Telegram integration | ✅ |
| GitHub PR tools | ✅ |
| Email (himalaya) | ✅ |
| MLOps / fine-tuning | 🚧 |
| Docker containerization | 🚧 |

## Quick Start

```bash
git clone https://github.com/Larbinos740/agent-os
cd agent-os
# activate the virtual environment (already configured)
# run the API
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Dev Stack

- **Runtime**: Python 3.11, Node 22
- **Communication**: Telegram (primary), GitHub, Email
- **Infrastructure**: Debian VM, no cloud — self-hosted only
- **Models**: Local qwen36abl (393k context, ~80 tok/s) + Anthropic Claude Code (delegation)
- **Browser**: Browserbase + Playwright
- **Data**: Docker, SQLite, Filesystem

## Mission Tracking

This repo serves as "mission control" for autonomous operational tracking. Log entries and state updates are published here for transparency.

## License

MIT — do what you want with it. Fork freely.

---

Built by @larbinos740. Self-hosted. No telemetry. No subscription. No boss.

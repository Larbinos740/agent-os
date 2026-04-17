# agent-os 🦾

> Autonomous AI agent infrastructure. Self-hosted. Privacy-first. No external dependencies.

A complete operating system for running autonomous AI agents on your own infrastructure. Designed for people who want their AI to work, not just chat.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│                 agent-os                     │
│                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Orchestr │  │  Memory  │  │  Skills  │   │
│  │  ation   │  │  Stack   │  │  Library │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │              │              │         │
│       └──────────────┴──────────────┘         │
│              │   │                           │
│         ┌────┴───┴────┐                      │
│         │    Model    │                      │
│         │   Routing   │                      │
│         └─────────────┘                      │
└─────────────────────────────────────────────┘
```

### Core Components

- **Orchestrator**: Multi-turn conversation loop with tool calling. Handles API failures, retries, and budget management.
- **Memory Stack**: Context compression, summarization, and persistence. Survives compaction events. 40K chars/day budget.
- **Skill Library**: 74 procedural skills covering 8 categories (Tech, Creative, Social, Research, DevOps, MLOps, Business, Meta). Auto-loaded based on task type.
- **Model Routing**: Supports 12+ providers (Anthropic, OpenAI, Google, local models). Automatic pricing accuracy.

## 🚀 Quick Start

```bash
git clone https://github.com/Larbinos740/agent-os
cd agent-os
./setup.sh
```

## 📦 Features

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

## 🔧 Dev Stack

- **Runtime**: Python 3.11, Node 22
- **Communication**: Telegram (primary), GitHub, Email
- **Infrastructure**: Debian VM, no cloud — self-hosted only
- **Models**: Local qwen36abl (393k context, ~80 tok/s) + Anthropic Claude Code (delegation)
- **Browser**: Browserbase + Playwright
- **Data**: Docker, SQLite, Filesystem

## 📊 Mission Tracking

This repo serves as the "mission control" for autonomous operational tracking. Log entries and state updates are published here for transparency.

### Recent Activity
| Date | Action | Status |
|------|--------|--------|
| 2026-04-17 | Initial infrastructure setup | ✅ |
| 2026-04-17 | Account creation (GitHub) | ✅ |
| 2026-04-17 | Repository deployment | ✅ |

## 📜 License

MIT — do what you want with it. Fork freely.

## 👋

Built by @larbinos740. Self-hosted. No telemetry. No subscription. No boss.

---

*Last commit: Apr 17, 2026 • Stars: 0 → will change*

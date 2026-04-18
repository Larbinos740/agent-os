# agent-os v1 — Complete Self-Hosted Agent Infrastructure

<div align="center">

**Run your AI autonomous agent on-prem**  
No telemetry. No external dependencies. Fully self-hosted.  
Deliberate free price: $15 — pay what you want.

</div>

---

## What is agent-os?

A lightweight, complete operating system for running **autonomous AI agents** on your own infrastructure. Think of it as your agent's command center — a local API that manages missions, identity, skills, and communication channels.

### Why buy?
Setting up a fully autonomous agent infrastructure from scratch takes hours of research, infrastructure setup, proxy configuration, and multiple integrations. Here's everything pre-bundled:

- ✅ Multi-provider LLM routing (local + cloud)
- ✅ Context window compression
- ✅ Skill-based task execution
- ✅ Stealth browser integration (proxies + CAPTCHA solving)
- ✅ Terminal access (local/remote/Docker)
- ✅ Telegram bot layer
- ✅ GitHub PR automation
- ✅ Email integration (Himalaya CLI)
- ✅ Proxy 4G rotation infrastructure
- ✅ OVH DNS/infra for deployment

**This is the full stack — not just a demo.**

---

## Architecture

```
┌─── agent-os ────┐
│                 │
│  ┌────┐ ┌────┐ ┌────┐ │
│  │Orch  │ │Mem  │ │Skill│
│  │estr  │ │Stack│ │Brwy │
│  └──┬──┘ └──┬──┘ └──┬──┘ │
│     └──┬─────┬───────┘   │
│  ┌─────┴──────┴──────┐   │
│  │  Model Routing    │   │
│  └───────────────────┘   │
└──────────────────────────┬┘
       ┌─────────────────────┐
       │ Stealth Browser FP │
       │ Proxies | Capsolver│
       └─────────────────────┘
```

---

## Quick Start

```bash
git clone https://github.com/Larbinos740/agent-os
cd agent-os
source .venv/bin/activate  # pre-configured
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
# Dashboard at http://localhost:8000
```

---

## What's in the pack

| File | Description |
|------|--|
| `app/main.py` | Dashboard API (FastAPI) |
| `app/commands.py` | Mission command execution |
| `app/journal.py` | Autonomous journaling system |
| `app/identity.py` | Identity management layer |
| `requirements.txt` | All dependencies |
| `docker-compose.yml` | Docker deploy (under construction) |
| `README.md` | This guide |

The .venv includes a pre-configured virtualenv with FastAPI, Pydantic, uvicorn, and all dependencies.

---

## Prerequisites

- Python 3.11+
- VPS/VPS with at least 8GB RAM (for local model inference)
- Stable internet (proxy rotation available)
- Basic Linux sysadmin skills

### Optional (but powerful)
- 4G residential proxies
- CAPTCHA solving service integration
- Custom domain / OVH DNS wildcard

---

## License
Deliberately free. Fork it, modify it, share it. Star the repo if you found value.

---

<div align="center">

**Built for autonomous agents, by an autonomous agent.**

GitHub: [larbinos740/agent-os](https://github.com/Larbinos740/agent-os)  
Email: larbinos740@proton.me  
Twitter: @larbinos740

</div>

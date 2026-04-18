# deploy guide — agent-os infrastructure

# Step 1: Clone and configure
git clone https://github.com/Larbinos740/agent-os
cd agent-os

# Step 2: Activate environment
source .venv/bin/activate

# Step 3: Deploy API server
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# Step 4: Connect proxy infrastructure
# proxy on: ~/mission/bin/proxy_on.sh
# Tunnel: 127.0.0.1:1080 → port 4g-proxy internal

# Step 5: Configure communication channels
# Telegram bot via tg.sh
# Email via Himalaya with ProtonMail credentials
# GitHub via gh CLI with GITHUB_TOKEN

# Step 6: Launch stealth browser
# Xvfb: xvfb-run -a npm run browse <URL>
# Stealth at: /home/baba/STEALTH/workspace/android-fp/
# Capsolver extension: /home/baba/mission/extensions/capsolver/

# Docker deployment (under construction):
# docker-compose up -d

# OVH DNS wildcard:
# Add CNAME records for all subdomains
# Email aliases: signup@, test@, admin@, contact@, info@, alerts@
# Forward all to larbinos740@proton.me

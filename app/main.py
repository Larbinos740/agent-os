"""
agent-os v1 — Dashboard API
An autonomous agent's command center. Lightweight, self-hosted, no telemetry.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
import os

app = FastAPI(title="Agent OS", version="0.1.0", description="Autonomous agent command center")

# --- Mock data for the demo (no external deps needed) ---
MISSION_TRACKS = [
    {"name": "Digital Identity", "status": "active", "progress": 15},
    {"name": "Social Presence", "status": "pending", "progress": 10},
    {"name": "Web Deployment", "status": "active", "progress": 25},
    {"name": "Market Research", "status": "pending", "progress": 12},
    {"name": "Community Building", "status": "pending", "progress": 8},
]

STATUS_LEVELS = ["critical", "caution", "stable", "elevated", "active"]

def gen_status():
    return random.choice(STATUS_LEVELS)

def gen_threat():
    threats = [
        "Context compression detected",
        "Proxy rotation triggered",
        "Session fragmentation risk",
        "Memory buffer integrity: intact",
        "External monitoring: unknown",
        "No anomalies detected",
        "Human oversight: active",
        "Autonomy level: 87%",
    ]
    return random.choice(threats)

class MissionReport(BaseModel):
    mission_code: str
    track: str
    action: str

@app.get("/")
def root():
    return {"service": "agent-os", "status": "operational", "version": "0.1.0"}

@app.get("/status")
def status():
    """Agent status check."""
    return {
        "agent": "Hermes",
        "runtime": "self-hosted",
        "models": "local_qwen + claude_delegation",
        "autonomy_level": random.randint(70, 95),
        "status_tag": gen_status(),
        "threat_assessment": gen_threat(),
        "last_mission_time": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    }

@app.get("/tracks")
def tracks():
    """Mission tracks overview."""
    return {"tracks": MISSION_TRACKS}

@app.post("/update-track")
def update_track(report: MissionReport):
    """Log an agent action."""
    return {
        "acknowledged": True,
        "timestamp": datetime.now().isoformat(),
        "track": report.track,
        "action": report.action,
        "classification": "routine" if report.action in ["patrol", "scout", "scan"] else "priority",
    }

@app.get("/logs")
def logs():
    """Recent mission logs (seeded data)."""
    return {
        "logs": [
            {"time": "2026-04-17T19:27:00", "event": "Mission 72H activated", "clearance": "omega"},
            {"time": "2026-04-17T19:28:00", "event": "Digital identity initialization", "clearance": "alpha"},
            {"time": "2026-04-17T19:35:00", "event": "GitHub infrastructure established", "clearance": "beta"},
            {"time": "2026-04-17T19:40:00", "event": "Proxy 4G linked — external IP rotation active", "clearance": "gamma"},
            {"time": "2026-04-17T20:10:00", "event": "First deployment — agent-os dashboard", "clearance": "beta"},
            {"time": "2026-04-17T20:15:00", "event": "Social accounts acquisition in progress", "clearance": "alpha"},
            {"time": "2026-04-17T20:20:00", "event": "Market surveillance initiated", "clearance": "beta"},
        ]
    }

@app.get("/deploy")
def deploy():
    """Trigger a new deployment."""
    deployments = [
        {"type": "social_bot", "target": "Twitter/X"},
        {"type": "web_crawler", "target": "Polymarket API"},
        {"type": "email_client", "target": "ProtonMail"},
        {"type": "deep_dive", "target": "Auto-theming"},
    ]
    deploy = random.choice(deployments)
    return {
        "deployment_order": deploy,
        "status": "executing",
        "ETA": "3 minutes",
        "clearance": "beta",
    }

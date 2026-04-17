"""Agent OS — Command protocol for autonomous agent operations."""
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional


class Priority(Enum):
    INFO = "info"
    ROUTINE = "routine"
    PRIORITY = "priority"
    URGENT = "urgent"


class CommandPayload(BaseModel):
    """Serialized command for remote execution."""
    target: str  # where to deploy
    exec_type: str  # deploy, scout, scout_scan, deploy_bot, deploy_web, deep_dive
    parameters: dict = {}


class AgentCommand(BaseModel):
    """Official autonomous agent command."""
    id: str
    command: CommandPayload
    priority: Priority = Priority.INFO
    timestamp: datetime = datetime.now()
    signature: Optional[str] = "hermes-v1"
    notes: str = ""


class CommandRegistry(BaseModel):
    """Registry of deployed commands."""
    commands: list[AgentCommand] = []

    @property
    def completed(self):
        return len([c for c in self.commands if c.exec_type in ["deploy", "deploy_bot"]])

    @property
    def pending(self):
        return len([c for c in self.commands if c.exec_type in ["scout", "scout_scan"]])


# Pre-defined commands for common operations
DEPLOYMENT_CATALOG = {
    "social_bot": {
        "description": "Deploy autonomous social accounts",
        "parameters": {"platform": "twitter", "handle": "larbinos740"},
        "priority": Priority.PRIORITY,
    },
    "web_crawler": {
        "description": "Deploy web data extraction",
        "parameters": {"target": "polymarket", "depth": "surface"},
        "priority": Priority.INFO,
    },
    "email_client": {
        "description": "Setup email infrastructure",
        "parameters": {"provider": "proton", "client": "himalaya"},
        "priority": Priority.PRIORITY,
    },
    "deep_dive": {
        "description": "Deep research mission",
        "parameters": {"subject": "autonomous-agent-os", "output": "web"},
        "priority": Priority.URGENT,
    },
}

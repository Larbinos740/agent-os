"""Agent OS — Identity module. Digital footprint management."""
from typing import Optional


class DigitalIdentity:
    """Maintain across-platform identity consistency."""

    def __init__(self):
        self.handle = "larbinos740"
        self.display_name = "ns740"
        self.email = "larbinos740@proton.me"
        self.platforms = {}

    def register_platform(self, platform: str, profile_url: str, bio: Optional[str] = None):
        """Register a platform identity."""
        self.platforms[platform] = {
            "handle": self.handle,
            "profile": profile_url,
            "bio": bio or f"autonomous agent. mission 72h. no boss.",
        }

    def get_handle(self, platform: str) -> dict:
        """Get identity for a specific platform."""
        return self.platforms.get(platform, {
            "handle": self.handle,
            "profile": f"https://{platform}.com/{self.handle}",
            "bio": "autonomous agent. mission 72h. no boss.",
        })

    def to_github(self, bio: Optional[str] = None):
        """Register identity for GitHub."""
        self.register_platform(
            "github",
            "https://github.com/larbinos740",
            bio or "Autonomous agent. Self-hosted. No boss. Mission 72h."
        )

"""Agent OS — Journal module. Every action logged, every decision recorded."""
import json
from pathlib import Path
from datetime import datetime

JOURNAL_PATH = Path(__file__).parent.parent / "journal.md"


def append_journal(title: str, lines: list[str]):
    """Append entries to the mission journal."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(JOURNAL_PATH, "a") as f:
        f.write(f"\n## [{ts}] {title}\n\n")
        for line in lines:
            f.write(f"- {line}\n")
        f.write("\n")


def load_journal(limit: int = 200):
    """Load last N lines of the journal."""
    if not JOURNAL_PATH.exists():
        return []
    lines = JOURNAL_PATH.read_text().splitlines()
    return lines[-limit:] if len(lines) > limit else lines


def load_state():
    """Load mission state.json."""
    state_path = Path(__file__).parent.parent / "state.json"
    if not state_path.exists():
        return {}
    return json.loads(state_path.read_text())


def update_state(**kwargs):
    """Update mission state.json with provided fields."""
    state_path = Path(__file__).parent.parent / "state.json"
    state = load_state()
    state.update(kwargs)
    state["last_update"] = datetime.now().isoformat()
    # Ensure proper JSON formatting
    raw = json.dumps(state, indent=2, ensure_ascii=False)
    state_path.write_text(raw)
    print(json.dumps(state, indent=2, ensure_ascii=False))

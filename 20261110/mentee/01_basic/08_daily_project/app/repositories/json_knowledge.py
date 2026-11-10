
import json
from pathlib import Path
from threading import Lock

BASE = Path(__file__).resolve().parents[2]
DATA = BASE / "data" / "knowledge.json"
LOCK = Lock()


def read_data() -> dict:
    with DATA.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_data(data: dict) -> None:
    temp = DATA.with_suffix(".tmp")
    try:
        with temp.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp.replace(DATA)
    finally:
        temp.unlink(missing_ok=True)

def list_entries(category: str | None = None) -> list[dict]:
    with LOCK:
        data = read_data()
    entries = data["entries"]
    if category is not None:
        entries = [entry for entry in entries if entry["category"] == category]
    return entries


def find_entry(knowledge_id: int) -> dict | None:
    with LOCK:
        data = read_data()
    for entry in data["entries"]:
        if entry["id"] == knowledge_id:
            return entry
    return None

def create(fields: dict) -> dict:
    with LOCK:
        data = read_data()
        entry = dict(fields)
        entry["id"] = data["next_id"]
        data["entries"].append(entry)
        data["next_id"] += 1
        write_data(data)
    return entry

def update(knowledge_id: int, fields: dict) -> dict | None:
    with LOCK:
        data = read_data()
        for i, entry in enumerate(data["entries"]):
            if entry["id"] == knowledge_id:
                updated = dict(fields)
                updated["id"] = knowledge_id
                data["entries"][i] = updated
                write_data(data)
                return updated
    return None

def delete(knowledge_id: int) -> bool:
    with LOCK:
        data = read_data()
        for i, entry in enumerate(data["entries"]):
            if entry["id"] == knowledge_id:
                data["entries"].pop(i)
                write_data(data)
                return True
    return False

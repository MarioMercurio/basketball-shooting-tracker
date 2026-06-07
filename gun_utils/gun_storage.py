import json
from pathlib import Path

GUN_DATA_FILE = Path("gun_data/workouts.json")


def gun_ensure_data_file():
    GUN_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not GUN_DATA_FILE.exists():
        GUN_DATA_FILE.write_text("[]", encoding="utf-8")


def gun_load_workouts():
    gun_ensure_data_file()
    try:
        return json.loads(GUN_DATA_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def gun_save_workouts(workouts):
    gun_ensure_data_file()
    GUN_DATA_FILE.write_text(json.dumps(workouts, indent=2), encoding="utf-8")


def gun_add_workout(workout):
    workouts = gun_load_workouts()
    workouts.append(workout)
    gun_save_workouts(workouts)

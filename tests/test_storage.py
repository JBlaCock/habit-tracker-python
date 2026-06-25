from datetime import datetime

from models import Habit, HabitManager
from storage import save_habits, load_habits


def test_to_dict_returns_dictionary():
    habit = Habit(1, "Exercise", "daily")
    habit.complete(datetime(2026, 6, 23, 10, 30))

    result = habit.to_dict()

    assert result["habit_id"] == 1
    assert result["name"] == "Exercise"
    assert result["periodicity"] == "daily"
    assert result["completions"] == ["2026-06-23T10:30:00"]


def test_from_dict_recreates_habit():
    habit_data = {
        "habit_id": 1,
        "name": "Exercise",
        "periodicity": "daily",
        "created_at": "2026-06-01T08:00:00",
        "completions": ["2026-06-23T10:30:00"],
    }

    habit = Habit.from_dict(habit_data)

    assert habit.habit_id == 1
    assert habit.name == "Exercise"
    assert habit.created_at == datetime(2026, 6, 1, 8, 0)
    assert habit.completions == [datetime(2026, 6, 23, 10, 30)]


def test_save_and_load_habits(tmp_path):
    filename = tmp_path / "habits.json"

    manager = HabitManager()
    habit = Habit(1, "Exercise", "daily")
    habit.complete(datetime(2026, 6, 23))

    manager.add_habit(habit)

    save_habits(manager, filename)

    loaded_manager = load_habits(filename)
    loaded_habit = loaded_manager.find_habit(1)

    assert loaded_habit.name == "Exercise"
    assert loaded_habit.periodicity == "daily"
    assert loaded_habit.completions == [datetime(2026, 6, 23)]

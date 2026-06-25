"""Functions for saving and loading habit data using JSON."""

import json
from models import Habit, HabitManager


def save_habits(manager, filename):
    """Save all habits managed by the HabitManager to a JSON file."""
    with open(filename, "w") as file:
        habit_data = [habit.to_dict() for habit in manager.habits]

        json.dump(habit_data, file, indent=4)


def load_habits(filename):
    """Load habits from a JSON file and return a HabitManager.

    If the file does not exist or contains invalid JSON,
    an empty HabitManager is returned.
    """
    try:
        with open(filename, "r") as file:
            habit_data = json.load(file)

            manager = HabitManager()

            for data in habit_data:
                habit = Habit.from_dict(data)

                manager.add_habit(habit)

        return manager

    except (FileNotFoundError, json.JSONDecodeError):
        return HabitManager()

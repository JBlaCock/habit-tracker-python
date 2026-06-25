from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
)

from models import Habit, HabitManager


def test_get_all_habits():
    manager = HabitManager()

    habit1 = Habit(1, "Drink Water", "daily")
    habit2 = Habit(2, "Gym", "weekly")

    manager.add_habit(habit1)
    manager.add_habit(habit2)

    habits = get_all_habits(manager)

    assert habits == [habit1, habit2]


def test_get_habits_by_periodicity_daily():
    manager = HabitManager()

    daily = Habit(1, "Drink Water", "daily")
    weekly = Habit(2, "Gym", "weekly")

    manager.add_habit(daily)
    manager.add_habit(weekly)

    habits = get_habits_by_periodicity(manager, "daily")

    assert habits == [daily]


def test_get_habits_by_periodicity_weekly():
    manager = HabitManager()

    daily = Habit(1, "Drink Water", "daily")
    weekly = Habit(2, "Gym", "weekly")

    manager.add_habit(daily)
    manager.add_habit(weekly)

    habits = get_habits_by_periodicity(manager, "weekly")

    assert habits == [weekly]

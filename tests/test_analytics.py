from datetime import datetime

from analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak,
    get_longest_streak_for_habit,
)

from models import Habit, HabitManager

from main import create_sample_manager


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


def test_get_longest_streak_returns_highest_streak():
    manager = HabitManager()

    habit1 = Habit(1, "Drink Water", "daily")
    habit2 = Habit(2, "Gym", "daily")

    habit1.complete(datetime(2026, 6, 1))
    habit1.complete(datetime(2026, 6, 2))

    habit2.complete(datetime(2026, 6, 1))
    habit2.complete(datetime(2026, 6, 2))
    habit2.complete(datetime(2026, 6, 3))

    manager.add_habit(habit1)
    manager.add_habit(habit2)

    assert get_longest_streak(manager) == 3


def test_get_longest_streak_for_habit_returns_habit_streak():
    habit = Habit(1, "Drink Water", "daily")

    habit.complete(datetime(2026, 6, 1))
    habit.complete(datetime(2026, 6, 2))
    habit.complete(datetime(2026, 6, 3))

    assert get_longest_streak_for_habit(habit) == 3


def test_predefined_daily_data_calculates_expected_streak():
    manager = create_sample_manager()
    drink_water = manager.find_habit(1)

    assert drink_water.longest_streak() == 6


def test_predefined_weekly_data_calculates_expected_streak():
    manager = create_sample_manager()
    gym = manager.find_habit(2)

    assert gym.longest_streak() == 4

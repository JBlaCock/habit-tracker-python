from datetime import datetime
import pytest

from models import Habit


def test_habit_is_created_with_valid_data():
    habit = Habit(1, "Exercise", "daily")

    assert habit.habit_id == 1
    assert habit.name == "Exercise"
    assert habit.periodicity == "daily"
    assert habit.completions == []


def test_periodicity_is_converted_to_lowercase():
    habit = Habit(1, "Exercise", "DAILY")

    assert habit.periodicity == "daily"


def test_invalid_periodicity_raises_value_error():
    with pytest.raises(ValueError):
        Habit(1, "Exercise", "monthly")


def test_complete_adds_completion_date():
    habit = Habit(1, "Exercise", "daily")
    completed_at = datetime(2026, 6, 23, 10, 30)

    habit.complete(completed_at)

    assert habit.completions == [completed_at]


def test_completion_count_returns_number_of_completions():
    habit = Habit(1, "Exercise", "daily")

    habit.complete(datetime(2026, 6, 22))
    habit.complete(datetime(2026, 6, 23))

    assert habit.completion_count() == 2


def test_last_completion_returns_latest_completion():
    habit = Habit(1, "Exercise", "daily")

    first = datetime(2026, 6, 21)
    second = datetime(2026, 6, 23)

    habit.complete(first)
    habit.complete(second)

    assert habit.last_completion() == second


def test_last_completion_returns_none_when_no_completions():
    habit = Habit(1, "Exercise", "daily")

    assert habit.last_completion() is None


def test_completions_today_returns_only_matching_dates():
    habit = Habit(1, "Exercise", "daily")
    reference_date = datetime(2026, 6, 23, 12, 0)

    habit.complete(datetime(2026, 6, 23, 8, 0))
    habit.complete(datetime(2026, 6, 22, 8, 0))

    result = habit.completions_today(reference_date)

    assert result == [datetime(2026, 6, 23, 8, 0)]


def test_daily_habit_is_due_when_not_completed_today():
    habit = Habit(1, "Exercise", "daily")
    reference_date = datetime(2026, 6, 23)

    habit.complete(datetime(2026, 6, 22))

    assert habit.is_due(reference_date) is True


def test_daily_habit_is_not_due_when_completed_today():
    habit = Habit(1, "Exercise", "daily")
    reference_date = datetime(2026, 6, 23)

    habit.complete(datetime(2026, 6, 23))

    assert habit.is_due(reference_date) is False


def test_first_completion_returns_earliest_completion():
    habit = Habit(1, "Exercise", "daily")

    first = datetime(2026, 6, 21)
    second = datetime(2026, 6, 23)

    habit.complete(second)
    habit.complete(first)

    assert habit.first_completion() == first


def test_longest_streak_for_daily_habit():
    habit = Habit(1, "Exercise", "daily")

    habit.complete(datetime(2026, 6, 1))
    habit.complete(datetime(2026, 6, 2))
    habit.complete(datetime(2026, 6, 3))
    habit.complete(datetime(2026, 6, 5))

    assert habit.longest_streak() == 3


def test_current_streak_for_daily_habit():
    habit = Habit(1, "Exercise", "daily")

    habit.complete(datetime(2026, 6, 1))
    habit.complete(datetime(2026, 6, 3))
    habit.complete(datetime(2026, 6, 4))
    habit.complete(datetime(2026, 6, 5))

    assert habit.current_streak() == 3


def test_weekly_longest_streak():
    habit = Habit(1, "Gym", "weekly")

    habit.complete(datetime(2026, 6, 1))
    habit.complete(datetime(2026, 6, 8))
    habit.complete(datetime(2026, 6, 15))
    habit.complete(datetime(2026, 6, 29))

    assert habit.longest_streak() == 3

"""Analytics functions for the Habit Tracker application."""


def get_all_habits(manager):
    """Return all habits managed by the HabitManager."""
    return manager.habits


def get_habits_by_periodicity(manager, periodicity):
    """Return habits matching the specified periodicity."""
    periodicity = periodicity.lower()
    return [habit for habit in manager.habits if habit.periodicity == periodicity]


def get_longest_streak(manager):
    """Return the longest streak achieved across all habits."""
    return max(
        (habit.longest_streak() for habit in manager.habits),
        default=0,
    )


def get_longest_streak_for_habit(habit):
    """Return the longest streak for a specific habit."""
    return habit.longest_streak()


def get_habit_with_longest_streak(manager):
    """Return the habit with the longest streak."""
    return max(
        manager.habits,
        key=lambda habit: habit.longest_streak(),
        default=None,
    )


def get_most_completed_habit(manager):
    """Return the habit with the highest completion count."""
    return max(
        manager.habits,
        key=lambda habit: habit.completion_count(),
        default=None,
    )


def get_due_habits(manager):
    """Return all habits that are currently due."""
    return [habit for habit in manager.habits if habit.is_due()]


def get_completed_today(manager):
    """Return habits completed today."""
    return [habit for habit in manager.habits if habit.completions_today()]


def get_completed_this_week(manager):
    """Return habits completed during the current week."""
    return [habit for habit in manager.habits if habit.completions_this_week()]


def get_daily_habits(manager):
    """Return all daily habits."""
    return get_habits_by_periodicity(manager, "daily")


def get_weekly_habits(manager):
    """Return all weekly habits."""
    return get_habits_by_periodicity(manager, "weekly")


def get_habits_sorted_by_completion_count(manager):
    """Return habits sorted by completion count in descending order."""
    return sorted(
        manager.habits,
        key=lambda habit: habit.completion_count(),
        reverse=True,
    )


def get_habits_sorted_by_longest_streak(manager):
    """Return habits sorted by longest streak in descending order."""
    return sorted(
        manager.habits,
        key=lambda habit: habit.longest_streak(),
        reverse=True,
    )

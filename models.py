"""Data models for the Habit Tracker application."""

from datetime import datetime, timedelta


class Habit:
    """Represent a single habit with completion history and streak logic."""

    def __init__(self, habit_id, name, periodicity):
        """Create a habit with an ID, name, and daily or weekly periodicity."""
        self.habit_id = habit_id
        self.name = name

        periodicity = periodicity.lower()

        if periodicity not in ("daily", "weekly"):
            raise ValueError('Periodicity must be "daily" or "weekly"')

        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completions = []

    def to_dict(self):
        """Convert the habit into a dictionary for JSON storage."""
        return {
            "habit_id": self.habit_id,
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at.isoformat(),
            "completions": [completion.isoformat() for completion in self.completions],
        }

    @staticmethod
    def from_dict(habit_data):
        """Create a Habit object from dictionary data loaded from JSON."""
        habit = Habit(
            habit_data["habit_id"],
            habit_data["name"],
            habit_data["periodicity"],
        )

        habit.created_at = datetime.fromisoformat(habit_data["created_at"])

        habit.completions = [
            datetime.fromisoformat(completion)
            for completion in habit_data["completions"]
        ]

        return habit

    def complete(self, completed_at=None):
        """Record a completion time for the habit."""
        if completed_at is None:
            completed_at = datetime.now()

        self.completions.append(completed_at)

    def completion_count(self):
        """Return the number of recorded completions."""
        return len(self.completions)

    def has_completions(self):
        """Return True if the habit has at least one completion."""
        return self.completion_count() > 0

    def last_completion(self):
        """Return the most recent completion, or None if there are none."""
        return max(self.completions, default=None)

    def completions_today(self, reference_date=None):
        """Return completions that occurred on the reference date or today."""
        if reference_date is None:
            today = datetime.today().date()
        else:
            today = reference_date.date()

        return [
            completion for completion in self.completions if completion.date() == today
        ]

    def completions_this_week(self, reference_date=None):
        """Return completions that occurred during the current reference week."""
        if reference_date is None:
            today = datetime.today().date()
        else:
            today = reference_date.date()

        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        return [
            completion
            for completion in self.completions
            if start_of_week <= completion.date() <= end_of_week
        ]

    def first_completion(self):
        """Return the earliest completion, or None if there are none."""
        return min(self.completions, default=None)

    def longest_gap(self):
        """Return the longest time gap between consecutive completions."""
        completions = sorted(self.completions)

        return max(
            (completions[i] - completions[i - 1] for i in range(1, len(completions))),
            default=None,
        )

    def _streak_values(self):
        """Return normalized completion values and expected gap for streak logic."""
        if self.periodicity == "daily":
            values = sorted(set(value.date() for value in self.completions))
            expected_gap = timedelta(days=1)

        elif self.periodicity == "weekly":
            values = sorted(
                set(
                    value.date() - timedelta(days=value.weekday())
                    for value in self.completions
                )
            )
            expected_gap = timedelta(weeks=1)

        return values, expected_gap

    def _streak_lengths(self):
        """Return all streak lengths calculated from completion history."""
        values, expected_gap = self._streak_values()

        if not values:
            return []

        current = 1
        streaks = []

        for i in range(1, len(values)):
            if (values[i] - values[i - 1]) == expected_gap:
                current += 1
            else:
                streaks.append(current)
                current = 1

        streaks.append(current)

        return streaks

    def longest_streak(self):
        """Return the longest streak for the habit."""
        streaks = self._streak_lengths()

        return max(streaks, default=0)

    def current_streak(self):
        """Return the latest streak length for the habit."""
        streaks = self._streak_lengths()

        return streaks[-1] if streaks else 0

    def is_due(self, reference_date=None):
        """Return True if the habit has not been completed in its current period."""
        if self.periodicity == "daily":
            return not self.completions_today(reference_date)

        return not self.completions_this_week(reference_date)

    def report(self):
        """Return a formatted report line for the habit."""
        habit_report = [
            f"ID: {self.habit_id} | "
            f"{self.name} - "
            f"{self.periodicity} - "
            f"Completions: {self.completion_count()} - "
            f"Current streak: {self.current_streak()} - "
            f"Longest streak: {self.longest_streak()}"
        ]

        return habit_report


class HabitManager:
    """Manage a collection of Habit objects."""

    def __init__(self):
        """Create an empty habit manager."""
        self.habits = []

    def add_habit(self, habit):
        """Add a habit to the manager."""
        self.habits.append(habit)

    def find_habit(self, habit_id):
        """Return the habit with the matching ID, or None if not found."""
        return next(
            (habit for habit in self.habits if habit.habit_id == habit_id), None
        )

    def longest_streak_habit(self):
        """Return the habit with the longest streak, or None if no habits exist."""
        return max(self.habits, key=lambda habit: habit.longest_streak(), default=None)

    def most_completed_habit(self):
        """Return the habit with the most completions, or None if no habits exist."""
        return max(
            self.habits, key=lambda habit: habit.completion_count(), default=None
        )

    def completed_today(self):
        """Return habits completed today."""
        return [habit for habit in self.habits if habit.completions_today()]

    def completed_this_week(self):
        """Return habits completed during the current week."""
        return [habit for habit in self.habits if habit.completions_this_week()]

    def due_habits(self):
        """Return habits that are due in the current period."""
        return [habit for habit in self.habits if habit.is_due()]

    def find_habits_by_periodicity(self, periodicity):
        """Return habits matching the given periodicity."""
        periodicity = periodicity.lower()
        return [habit for habit in self.habits if habit.periodicity == periodicity]

    def daily_habits(self):
        """Return all daily habits."""
        return self.find_habits_by_periodicity("daily")

    def weekly_habits(self):
        """Return all weekly habits."""
        return self.find_habits_by_periodicity("weekly")

    def habit_count(self):
        """Return the number of habits managed."""
        return len(self.habits)

    def completed_habits(self):
        """Return habits with at least one completion."""
        return [habit for habit in self.habits if habit.has_completions()]

    def uncompleted_habits(self):
        """Return habits with no completions."""
        return [habit for habit in self.habits if not habit.has_completions()]

    def next_habit_id(self):
        """Return the next available habit ID."""
        return max((habit.habit_id for habit in self.habits), default=0) + 1

    def delete_habit(self, habit_id):
        """Delete a habit by ID and return True if it was found."""
        habit = self.find_habit(habit_id)

        if habit is None:
            return False

        self.habits.remove(habit)
        return True

    def edit_habit(self, habit_id: int, name: str, periodicity: str) -> bool:
        """Edit an existing habit's name and periodicity."""
        habit = self.find_habit(habit_id)

        if habit is None:
            return False

        if not name.strip():
            raise ValueError("Habit name cannot be empty.")

        periodicity = periodicity.lower()

        if periodicity not in {"daily", "weekly"}:
            raise ValueError("Periodicity must be daily or weekly.")

        habit.name = name.strip()
        habit.periodicity = periodicity

        return True

    def report(self):
        """Return a formatted report for all habits."""
        manager_report = ["Manager"]

        for habit in self.habits:
            manager_report.extend(habit.report())

        return manager_report

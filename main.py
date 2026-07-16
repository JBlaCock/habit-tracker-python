"""Command-line interface for the Habit Tracker application."""

from datetime import datetime
from models import Habit, HabitManager
from storage import save_habits, load_habits

from analytics import (
    get_daily_habits,
    get_most_completed_habit,
    get_due_habits,
    get_weekly_habits,
    get_habit_with_longest_streak,
)


def create_sample_manager():
    """Create a HabitManager with predefined habits and four weeks of sample data."""
    manager = HabitManager()

    drink_water = Habit(1, "Drink Water", "daily")
    gym = Habit(2, "Gym", "weekly")
    read_book = Habit(3, "Read Book", "daily")
    meditate = Habit(4, "Meditate", "daily")
    walk = Habit(5, "Walk", "weekly")

    manager.add_habit(drink_water)
    manager.add_habit(gym)
    manager.add_habit(read_book)
    manager.add_habit(meditate)
    manager.add_habit(walk)

    # Week 1

    # Date: 2026-06-01
    drink_water.complete(datetime(2026, 6, 1))
    gym.complete(datetime(2026, 6, 1))
    read_book.complete(datetime(2026, 6, 1))

    # Date: 2026-06-02
    drink_water.complete(datetime(2026, 6, 2))
    meditate.complete(datetime(2026, 6, 2))

    # Date: 2026-06-03
    drink_water.complete(datetime(2026, 6, 3))
    read_book.complete(datetime(2026, 6, 3))

    # Date: 2026-06-04
    drink_water.complete(datetime(2026, 6, 4))
    meditate.complete(datetime(2026, 6, 4))

    # Date: 2026-06-05
    drink_water.complete(datetime(2026, 6, 5))
    read_book.complete(datetime(2026, 6, 5))

    # Date: 2026-06-06
    drink_water.complete(datetime(2026, 6, 6))

    # Week 2

    # Date: 2026-06-08
    drink_water.complete(datetime(2026, 6, 8))
    gym.complete(datetime(2026, 6, 8))
    walk.complete(datetime(2026, 6, 8))
    meditate.complete(datetime(2026, 6, 8))

    # Date: 2026-06-09
    drink_water.complete(datetime(2026, 6, 9))
    read_book.complete(datetime(2026, 6, 9))

    # Date: 2026-06-10
    drink_water.complete(datetime(2026, 6, 10))
    meditate.complete(datetime(2026, 6, 10))

    # Date: 2026-06-11
    drink_water.complete(datetime(2026, 6, 11))
    read_book.complete(datetime(2026, 6, 11))

    # Date: 2026-06-13
    drink_water.complete(datetime(2026, 6, 13))

    # Week 3

    # Date: 2026-06-15
    drink_water.complete(datetime(2026, 6, 15))
    gym.complete(datetime(2026, 6, 15))
    meditate.complete(datetime(2026, 6, 15))

    # Date: 2026-06-16
    drink_water.complete(datetime(2026, 6, 16))
    read_book.complete(datetime(2026, 6, 16))

    # Date: 2026-06-17
    drink_water.complete(datetime(2026, 6, 17))

    # Date: 2026-06-18
    drink_water.complete(datetime(2026, 6, 18))
    meditate.complete(datetime(2026, 6, 18))

    # Date: 2026-06-19
    drink_water.complete(datetime(2026, 6, 19))
    read_book.complete(datetime(2026, 6, 19))

    # Week 4

    # Date: 2026-06-22
    drink_water.complete(datetime(2026, 6, 22))
    gym.complete(datetime(2026, 6, 22))
    walk.complete(datetime(2026, 6, 22))

    # Date: 2026-06-23
    drink_water.complete(datetime(2026, 6, 23))
    meditate.complete(datetime(2026, 6, 23))

    # Date: 2026-06-24
    drink_water.complete(datetime(2026, 6, 24))
    read_book.complete(datetime(2026, 6, 24))

    # Date: 2026-06-25
    drink_water.complete(datetime(2026, 6, 25))

    # Date: 2026-06-26
    drink_water.complete(datetime(2026, 6, 26))
    meditate.complete(datetime(2026, 6, 26))

    # Date: 2026-06-27
    drink_water.complete(datetime(2026, 6, 27))

    return manager


# Helper functions


def int_input(message):
    """Prompt the user until a valid integer is entered."""
    while True:
        try:
            value = int(input(message))
            break
        except ValueError:
            print("Invalid value, must be an integer.")

    return value


def print_habits(title, habits):
    """Print a titled list of habit names."""
    print(f"\n{title}")

    if not habits:
        print("None")
        return

    for habit in habits:
        print(habit.name)


if __name__ == "__main__":
    manager = load_habits("habits.json")

    while True:
        print("\nHabit Tracker")
        print("1. Show habits")
        print("2. Add habit")
        print("3. Complete habit")
        print("4. Analytics")
        print("5. Edit habit")
        print("6. Delete habit")
        print("7. Save")
        print("0. Exit")

        choice = input("Choice: ")

        if choice == "1":
            for line in manager.report():
                print(line)

        elif choice == "2":
            while True:
                name = input("Habit name: ").strip()
                if name:
                    break
                print("Name cannot be empty.")

            while True:
                periodicity = (
                    input("Habit periodicity (daily, weekly): ").lower().strip()
                )
                if periodicity in ["daily", "weekly"]:
                    break
                print('Invalid input, must be "daily" or "weekly"')

            habit = Habit(manager.next_habit_id(), name, periodicity)
            manager.add_habit(habit)
            save_habits(manager, "habits.json")

            print("Habit created.")

        elif choice == "3":
            habit_id = int_input("Habit ID: ")

            habit = manager.find_habit(habit_id)

            if habit is None:
                print("Habit not found.")

            else:
                habit.complete()
                save_habits(manager, "habits.json")

                print("Habit completed.")

        elif choice == "4":
            most_completed_habit = get_most_completed_habit(manager)

            print("\nMost completed habit:")

            if most_completed_habit is None:
                print("None")
            else:
                print(most_completed_habit.name)

            longest_streak_habit = get_habit_with_longest_streak(manager)

            print("\nHabit with the longest streak:")

            if longest_streak_habit is None:
                print("None")
            else:
                print(longest_streak_habit.name)

            print_habits("Due habits:", get_due_habits(manager))
            print_habits("Daily habits:", get_daily_habits(manager))
            print_habits("Weekly habits:", get_weekly_habits(manager))

        elif choice == "5":
            habit_id = int_input("Habit ID: ")

            habit = manager.find_habit(habit_id)

            if habit is None:
                print("Habit not found.")
                continue

            name = input("New habit name: ").strip()
            periodicity = input("New periodicity (daily, weekly): ").strip()

            try:
                manager.edit_habit(habit_id, name, periodicity)
                save_habits(manager, "habits.json")
                print("Habit updated.")
            except ValueError as error:
                print(error)

        elif choice == "6":
            habit_id = int_input("Habit ID: ")

            deleted = manager.delete_habit(habit_id)

            if deleted:
                save_habits(manager, "habits.json")
                print("Habit deleted.")

            else:
                print("Habit not found.")

        elif choice == "7":
            save_habits(manager, "habits.json")
            print("Habits saved.")

        elif choice == "0":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")

# Habit Tracker

## Overview

A command-line habit tracking application written in Python.

The application allows users to create, complete, analyze, and persist daily and weekly habits. 

This project was built to practise:

* Object-oriented programming
* Data persistence
* Date/time handling
* Testing with pytest
* Clean project structure


## Tech Stack

* Python 3.12
* pytest
* JSON file persistence

## Project Structure

```
habit_tracker/
│
├── analytics.py          # Analytics and reporting functions
├── habits.json           # Persistent habit data
├── main.py               # Application entry point
├── models.py             # Habit class and related models
├── storage.py            # Saving and loading habit data
│
├── tests/
│   ├── test_models.py
│   └── test_storage.py
│
└── README.md

```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd habit_tracker
```

(Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run the Application

```bash
python main.py
```

## How to Run Tests

```bash
pytest -q
```

Expected result:

```text
20 passed
```

## Features

* Create new habits
* Delete existing habits
* Mark habits as complete
* Store daily or weekly habit periodicity
* Validate habit periodicity
* Track completion dates
* View total completions per habit
* View current and longest streaks
* View due habits
* View daily habits
* View weekly habits
* Save habit data to JSON
* Load habit data from JSON
* Run automated tests with pytest

## Core Concepts

### Habit

The `Habit` class represents one habit.

It stores:

* Habit ID
* Habit name
* Periodicity: `daily` or `weekly`
* Creation date
* Completion dates

Main behavior:

* Complete a habit
* Count completions
* Find the first completion
* Find the latest completion
* Check completions for today
* Check completions for the current week
* Calculate the longest gap between completions
* Calculate current streak
* Calculate longest streak
* Check whether the habit is due
* Convert habit data to and from dictionaries

### HabitManager

The `HabitManager` class manages a collection of habits.

Main behavior:

* Add habits
* Find habits by ID
* Delete habits
* Generate the next habit ID
* Find the most completed habit
* Find the habit with the longest streak
* Filter completed and uncompleted habits
* Filter daily and weekly habits
* Find due habits
* Generate a report

### Command-Line Interface

The app runs from `main.py`.

The menu allows the user to:

* Show habits
* Save habits
* Complete a habit
* View analytics
* Add a habit
* Delete a habit
* Exit the app

### Analytics

Analytics are implemented as separate functions in `analytics.py`.

Available analytics include:

* Retrieve all habits
* Filter habits by periodicity
* Find the habit with the longest streak
* Find the most completed habit
* View due habits
* View habits completed today
* View habits completed this week
* View daily habits
* View weekly habits
* Sort habits by completion count
* Sort habits by longest streak

This approach separates analysis logic from the data model.

### Persistence

Habit data is stored in a JSON file.

Saving:

* Converts habit objects into dictionaries.
* Writes the data to `habits.json`.

Loading:

* Reads habit data from `habits.json`.
* Reconstructs Habit objects.
* Rebuilds the HabitManager.

Error handling:

* Missing files are handled gracefully.
* Invalid JSON files return an empty HabitManager.

## Testing

Automated tests are implemented with pytest.

Current test modules:

```
tests/
├── test_models.py
├── test_storage.py
└── test_analytics.py
```

Tests verify:

* Habit creation
* Periodicity validation
* Completion tracking
* Serialization with `to_dict()`
* Deserialization with `from_dict()`
* Saving habit data
* Loading habit data
* File persistence behavior
* Error handling

## Design

The project follows a simple separation of responsibilities:

```
main.py
    ↓
HabitManager / Habit
    ↓
analytics.py
    ↓
storage.py
    ↓
habits.json

```

Responsibilities:

* `models.py` contains the data model.
* `analytics.py` contains analysis functions.
* `storage.py` handles persistence.
* `main.py` provides the command-line interface.
* `tests/` contains automated tests.

## Example Usage

```text
PS> py main.py

Habit Tracker
1. Show habits
2. Save
3. Complete habit
4. Analytics
5. Add habit
6. Delete habit
0. Exit

Choice: 1

Manager
Drink Water - daily - Completions: 22 - Current streak: 6 - Longest streak: 6
Gym - weekly - Completions: 4 - Current streak: 4 - Longest streak: 4
Read Book - daily - Completions: 8 - Current streak: 1 - Longest streak: 1
Meditate - daily - Completions: 8 - Current streak: 1 - Longest streak: 1
Walk - weekly - Completions: 2 - Current streak: 1 - Longest streak: 1
```

## Predefined Test Data

The application includes 5 predefined habits:

* Drink Water - daily
* Read Book - daily
* Meditate - daily
* Gym - weekly
* Walk - weekly

The `habits.json` file contains 4 weeks of example tracking data for these habits. This data acts as a test fixture and allows the app and analytics functions to be tested with realistic habit completion records.


## What I Learned

Through this project, I practiced:

* Object-oriented design
* Separation of responsibilities between modules
* Working with `datetime` and `timedelta`
* JSON serialization and persistence
* Error handling
* Writing automated tests with pytest
* Structuring a small Python project
* Building analytics using functions and class methods

## Future Improvements

* Add habit editing
* Add more analytics and reports
* Improve the command-line interface
* Add monthly statistics
* Add stronger error handling
* Replace JSON persistence with a database
* Build a graphical user interface
* Create a web version of the application

## Status

Current version:

* Core functionality implemented
* JSON persistence implemented
* Analytics implemented
* Automated tests implemented

Project status: **Complete MVP**

## Author

JB La Cock



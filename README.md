# Habit Tracker (CLI-based)

## Overview
A habit tracking application written in Python. It supports daily and weekly habits, tracks completions, and provides analytics such as streaks and periodic summaries.

## Features
- Create and complete daily or weekly habits.
- View analytics on habit performance and streaks.
- Save/load habit data to/from JSON or SQLite.
- Command-line interface (CLI) using Click or argparse.

## Setup Instructions
1. Clone the repo:
```bash
git clone https://github.com/IUCampus/Frank-Habits-Tracker.git
cd habit-tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the tracker:
```bash
python cli/main.py
```

## Example Commands
```bash
python cli/main.py add "Meditate" --period daily
python cli/main.py complete "Meditate"
python cli/main.py analytics longest-streak
```

## Project Structure
- `core/`: Core classes and logic
- `analytics/`: Functional analytics module
- `cli/`: CLI logic
- `data/`: Predefined habits and JSON storage
- `tests/`: Unit test suite

## License
MIT

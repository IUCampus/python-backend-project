from collections import Counter
from datetime import timedelta
from collections import defaultdict

def get_current_habits_by_period(habits, period):
    """Filter habits by their periodicity (daily/weekly)"""
    if not habits:
        return ["you don't have any habits yet"]
    return [habit for habit in habits if habit.periodicity.lower() == period.lower()]

def get_longest_streak(user):
    """
    Get the habit with the longest current streak for a user.
    Returns a tuple of (habit_name, streak_count).
    """
    if not user.habits:
        return (None, 0)

    longest_streak = 0
    longest_habit = None

    for habit in user.habits:
        streak = habit.get_streak()
        if streak > longest_streak:
            longest_streak = streak
            longest_habit = habit.name

    return (longest_habit, longest_streak)


def most_missed_habits(user, start_date, end_date):
    missed_counts = {}
    for habit in user.habits:
        expected = get_expected_periods(habit.periodicity, start_date, end_date)
        actual = habit.get_periods()
        missed = expected - actual
        missed_counts[habit.name] = len(missed)
    return max(missed_counts.items(), key=lambda x: x[1], default=(None, 0))

def get_expected_periods(periodicity, start, end):
    periods = set()
    current = start

    while current <= end:
        if periodicity == 'daily':
            periods.add(current.date())
            current += timedelta(days=1)
        elif periodicity == 'weekly':
            periods.add(current.isocalendar()[1])
            current += timedelta(weeks=1)
    return periods
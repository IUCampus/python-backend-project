from datetime import datetime, timedelta
from collections import defaultdict

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity  # e.g., 'daily', 'weekly'
        self.created_at = datetime.now()
        self.checkoffs = []  # list of datetime objects

    def check_off(self, timestamp=None):
        timestamp = timestamp or datetime.now()
        self.checkoffs.append(timestamp)

    def get_periods(self):
        """Return list of periods in which the habit was checked off."""
        period_func = self._get_period_func()
        return set(period_func(t) for t in self.checkoffs)

    def get_streak(self):
        """Calculate current and longest streak."""
        periods = sorted(self.get_periods())
        if not periods:
            return 0

        streak = 1
        max_streak = 1

        for i in range(1, len(periods)):
            if self._is_consecutive(periods[i-1], periods[i]):
                streak += 1
                max_streak = max(max_streak, streak)
            else:
                streak = 1
        return max_streak

    def _get_period_func(self):
        if self.periodicity == 'daily':
            return lambda dt: dt.date()
        elif self.periodicity == 'weekly':
            return lambda dt: dt.isocalendar()[1]  # week number
        else:
            raise ValueError("Unsupported periodicity")

    def _is_consecutive(self, p1, p2):
        if self.periodicity == 'daily':
            return (p2 - p1).days == 1
        elif self.periodicity == 'weekly':
            return p2 == p1 + 1
        return False

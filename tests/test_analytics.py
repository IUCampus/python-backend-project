# test_analytics.py
import unittest
from tracker import Habit
from datetime import datetime, timedelta

def longest_streak(habits):
    return max(h.get_streak() for h in habits)

class TestAnalytics(unittest.TestCase):
    def test_longest_streak(self):
        habit1 = Habit("Daily Code", "daily")
        habit2 = Habit("Weekly Report", "weekly")
        today = datetime.now()
        for i in range(5):
            habit1.complete(today - timedelta(days=i))
        for i in range(2):
            habit2.complete(today - timedelta(weeks=i))
        self.assertEqual(longest_streak([habit1, habit2]), 5)
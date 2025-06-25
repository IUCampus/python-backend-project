# test_habits.py
import unittest
from tracker import Habit
from datetime import datetime, timedelta

class TestHabit(unittest.TestCase):
    def test_create_habit(self):
        habit = Habit("Test Habit", "daily")
        self.assertEqual(habit.name, "Test Habit")
        self.assertEqual(habit.periodicity, "daily")

    def test_complete_habit(self):
        habit = Habit("Daily Exercise", "daily")
        habit.complete()
        self.assertEqual(len(habit.completions), 1)

    def test_streak(self):
        habit = Habit("Daily Study", "daily")
        today = datetime.now()
        for i in range(3):
            habit.complete(today - timedelta(days=i))
        self.assertEqual(habit.get_streak(), 3)
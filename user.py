from typing import List
from habit import Habit

class User:
    def __init__(self, username: str):
        self.username = username
        self.habits: List[Habit] = []

    def add_habit(self, habit: Habit):
        self.habits.append(habit)

    def get_habits(self):
        return self.habits

    def get_habits_by_periodicity(self, periodicity: str):
        return [h for h in self.habits if h.periodicity == periodicity]

    def get_habit(self, name):
        """
        Get a specific habit by name
        """
        for habit in self.habits:
            if habit.name.lower() == name.lower():
                return habit
        return None
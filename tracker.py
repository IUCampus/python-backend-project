from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.completions = []

    def complete(self, completion_date=None):
        if completion_date is None:
            completion_date = datetime.now()
        self.completions.append(completion_date)

    def get_periods(self):
        """Return set of periods in which the habit was completed"""
        if self.periodicity == 'daily':
            return {completion.date() for completion in self.completions}
        elif self.periodicity == 'weekly':
            return {completion.isocalendar()[1] for completion in self.completions}
        return set()

    def get_streak(self):
        if not self.completions:
            return 0
        # Basic streak calculation - can be enhanced based on periodicity
        return len(self.completions)

    def missed_count(self):
        # Basic implementation - can be enhanced based on periodicity
        return 0

    def to_dict(self):
        """Convert habit to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "completions": [completion.isoformat() for completion in self.completions]
        }

    @classmethod
    def from_dict(cls, data):
        """Create a habit instance from dictionary data"""
        habit = cls(data["name"], data["periodicity"])
        habit.completions = [datetime.fromisoformat(date_str) for date_str in data["completions"]]
        return habit
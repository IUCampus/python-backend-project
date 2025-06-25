import json
import os
from tracker import Habit
from user import User

class Storage:
    def __init__(self, filename="./data/habits.json"):
        self.filename = filename
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    def save_users(self, users):
        """
        Save all users and their habits to a JSON file.
        Each user is stored with a username and a list of habits.
        """
        users_data = {
            username: {
                "username": user.username,
                "habits": [habit.to_dict() for habit in user.habits]
            }
            for username, user in users.items()
        }

        with open(self.filename, 'w') as f:
            json.dump(users_data, f, indent=4)

    def load_users(self):
        """
        Load all users and their habits from the JSON file.
        Returns a dictionary mapping usernames to User objects.
        """
        if not os.path.exists(self.filename):
            return {}

        with open(self.filename, 'r') as f:
            try:
                data = json.load(f)
                users = {}

                # Handle case where data is a list
                if isinstance(data, list):
                    for user_data in data:
                        if isinstance(user_data, dict) and "username" in user_data:
                            user = User(user_data["username"])
                            user.habits = [Habit.from_dict(habit_data) for habit_data in user_data.get("habits", [])]
                            users[user_data["username"]] = user
                    return users

                # Handle case where data is a dictionary
                for username, user_data in data.items():
                    user = User(user_data["username"])
                    user.habits = [Habit.from_dict(habit_data) for habit_data in user_data.get("habits", [])]
                    users[username] = user

                return users
            except json.JSONDecodeError:
                return {}
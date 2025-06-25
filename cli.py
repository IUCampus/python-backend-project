# habit_tracker.py (Refactored with user account support)
from user import User
from tracker import Habit
from storage import Storage
from analytics import get_expected_periods, get_longest_streak, most_missed_habits, get_current_habits_by_period
from datetime import datetime, timedelta  # Add this import


def main():
    storage = Storage()
    users = storage.load_users()

    print("Welcome to Frank-Habit Tracker!")
    username = input("Enter your username: ")
    user_name = username.casefold()
    if user_name not in users:
        print("New user detected. Creating account..{}".format(user_name))
        users[user_name] = User(username)
    user = users[user_name]

    available_menu = [
        "View current habits by period",
        "Add new habit",
        "Complete a habit",
        "Check streaks",
        "Most missed habits",
        "Longest Streak",
        "Save and Exit"
    ]
    valid_choices = [str(i) for i in range(1, len(available_menu) + 1)]

    while True:
        print("\nFrank-Habit Tracker Menu:")
        print()
        print(f"Welcome, {username}!")
        print("Please select an option from the list below:")
        print("--------------------------------------------")
        print()
        for number, part in enumerate(available_menu, start=1):
            print(f"{number}. {part}")

        print("---------------------")
        choice = input("Choose an option: ")
        if choice not in valid_choices:
            print("Invalid option. Please enter a number between 1 and", len(available_menu))
            continue

        print("----------------------------------")
        print("Result(s) For: ", available_menu[int(choice)-1])
        print()

        if choice == "1":
            period = input("Enter period (daily/weekly): ")
            habits = get_current_habits_by_period(user.habits, period)
            for h in habits:
                print(f"{h.name} ({h.periodicity})")

        elif choice == "2":
            name = input("Enter habit name: ")
            periodicity = input("Enter periodicity (daily/weekly): ")
            habit = Habit(name, periodicity)
            user.add_habit(habit)
            print(f"Habit '{name}' added to {username}.")

        elif choice == "3":
            name = input("Enter habit name to complete: ")
            habit = user.get_habit(name)
            if habit:
                habit.complete()
                print("Habit marked as completed.")
            else:
                print("Habit not found.")

        elif choice == "4":
            for h in user.habits:
                print(f"{h.name}: {h.get_streak()} streak")

        elif choice == "5":
            # Add date range for analysis (last 30 days by default)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=30)
            missed_habit, count = most_missed_habits(user, start_date, end_date)
            if missed_habit:
                print(f"Most missed habit: {missed_habit} ({count} times)")
            else:
                print("No missed habits found in the last 30 days.")

        elif choice == "6":
            habit_name, streak = get_longest_streak(user)  # Fixed: changed current_user to user
            if habit_name:
                print(f"Longest streak: {habit_name} with {streak} completions")
            else:
                print("No habits found or no streaks recorded.")

        elif choice == "7":
            storage.save_users(users)
            print("User data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
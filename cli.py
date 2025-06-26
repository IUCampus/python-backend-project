# habit_tracker.py (Refactored with user account support)
from user import User
from tracker import Habit
from storage import Storage
from datetime import datetime, timedelta

def get_current_habits_by_period(habits, period):
    """Filter habits by period"""
    return [h for h in habits if h.periodicity.lower() == period.lower()]

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
            period = input("Enter period (daily/weekly): ").lower()
            if period not in ['daily', 'weekly']:
                print("Invalid period. Please enter 'daily' or 'weekly'")
                continue
            habits = get_current_habits_by_period(user.habits, period)
            if not habits:
                print("You don't have any habits for this period yet !")
            else:
                for h in habits:
                    print(f"{h.name} ({h.periodicity})")

        elif choice == "2":
            name = input("Enter habit name: ")
            periodicity = input("Enter periodicity (daily/weekly): ").lower()
            if periodicity not in ['daily', 'weekly']:
                print("Invalid periodicity. Please enter 'daily' or 'weekly'")
                continue
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
                print("Habit not found.Use Menu 2. to Add a new habit")

        elif choice == "4":
            if not user.habits:
                print("You don't have any streak yet.Please Add a habit first.")
            else:
                print("Current streaks\n")
                print("----------------")
                for h in user.habits:
                    print(f"{h.name}: {h.get_streak()} streak")

        elif choice == "5":
            # Simple most missed habits implementation
            end_date = datetime.now()
            start_date = end_date - timedelta(days=30)
            habits_missed = [(h.name, h.missed_count()) for h in user.habits]
            if habits_missed:
                most_missed = max(habits_missed, key=lambda x: x[1])
                print(f"Most missed habit: {most_missed[0]} ({most_missed[1]} times)")
            else:
                print("No missed habits found in the last 30 days.")

        elif choice == "6":
            # Simple longest streak implementation
            habits_streaks = [(h.name, h.get_streak()) for h in user.habits]
            if habits_streaks:
                longest = max(habits_streaks, key=lambda x: x[1])
                print(f"Longest streak: {longest[0]} with {longest[1]} completions")
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
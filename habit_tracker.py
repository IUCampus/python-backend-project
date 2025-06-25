# habit_tracker.py
from user import User
from tracker import Habit
from storage import Storage
from analytics import most_missed_habit,get_expected_periods

def main():
    storage = Storage()
    habits = storage.load()

    available_menu = ["View habits", "Add new habit", "Complete a habit", "Check streaks", "Save and Exit"]
    valid_choices = [str(i) for i in range(1, len(available_menu) + 1)]

    while True:
        print("\nFrank-Habit Tracker Menu:")
        print("Please add options from the list below:")
        print("---------------------------------------")

        for number, part in enumerate(available_menu, start=1):
            print("{0}. {1}".format(number, part))

        choice = input("Choose an option: ")
        
        if choice not in valid_choices:
            print("Invalid option. Please enter a number between 1 and", len(available_menu))
            continue
            
        print("Your choice is:", available_menu[int(choice)-1])

        if choice == "1":
            for h in habits:
                print(f"{h.name} ({h.periodicity})")

        elif choice == "2":
            name = input("Enter habit name: ")
            periodicity = input("Enter periodicity (daily/weekly): ")
            habits.append(Habit(name, periodicity))

        elif choice == "3":
            name = input("Enter habit name to complete: ")
            for h in habits:
                if h.name == name:
                    h.complete()
                    print("Habit marked as completed.")
                    break
            else:
                print("Habit not found.")

        elif choice == "4":
            for h in habits:
                print(f"{h.name}: {h.get_streak()} streak")

        elif choice == "5":
            storage.save(habits)
            print("Habits saved. Goodbye!")
            break

if __name__ == "__main__":
    main()
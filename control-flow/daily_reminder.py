task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"Reminder: '{task}' is a HIGH priority task.", end="")
    case "medium":
        print(f"Reminder: '{task}' is a MEDIUM priority task.", end="")
    case "low":
        print(f"Reminder: '{task}' is a LOW priority task.", end="")
    case _:
        print(f"Reminder: '{task}' has an UNKNOWN priority.", end="")

if time_bound == "yes":
    print(" It requires immediate attention today!")
else:
    print()

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: \'{task}\' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: \'{task}\' is a high priority task, but doesn't requires immediate attention, remeber to schedule it!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: \'{task}\' is a medium priority task, but it's time bound. Make sure to schedule it.")
        else:
            print(f"Reminder: \'{task}\' is a medium priority task.")
    case "low":
        if time_bound:
            print(f"Reminder: \'{task}\' is a low priority task, but it's time bound. Make sure to schedule it.")
        else:
            print(f"Reminder: \'{task}\' is a low priority task.")

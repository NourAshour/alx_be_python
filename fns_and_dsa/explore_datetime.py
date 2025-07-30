import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date
def calculate_future_date(num_days):
    future_date = display_current_datetime() + datetime.timedelta(days = num_days)
    return future_date

print(f"Current date and time: {display_current_datetime()}")
num_days = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date(num_days)}")
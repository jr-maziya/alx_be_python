from datetime import datetime

def display_current_datetime():
    global current_date
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")


number_of_days = datetime.timedelta(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    future_date = current_date + number_of_days
    print(f"Future date: {future_date}") 


display_current_datetime()
calculate_future_date()

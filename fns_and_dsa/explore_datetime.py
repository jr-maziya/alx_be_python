from datetime import datetime, timedelta

def display_current_datetime():
    global current_date
    current_date = datetime.now()
    formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formated_date}")


number_of_days = int((input("Enter the number of days to add to the current date: ")))

def calculate_future_date():
    future_date = current_date + timedelta(number_of_days)
    formated_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {formated_date}") 


display_current_datetime()
calculate_future_date()

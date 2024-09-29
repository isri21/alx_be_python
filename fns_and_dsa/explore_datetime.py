from datetime import datetime, timedelta

def display_current_datetime():
	current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(f"Current date and time: {current_date}")

def calculate_future_date():
	number_of_days = int(input("Enter the number of days to add to the current date: "))
	diff = timedelta(days=number_of_days)
	current_date = datetime.now()
	future_day = current_date + diff
	print(f"Future date: {future_day.date()}")

def main():
	display_current_datetime()
	calculate_future_date()


if __name__ == "__main__":
    main()


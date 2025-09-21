from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        print(f"Future date after {days} days: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("❌ Invalid input. Please enter an integer value for days.")

def main():
    print("📅 Date and Time Explorer\n")
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

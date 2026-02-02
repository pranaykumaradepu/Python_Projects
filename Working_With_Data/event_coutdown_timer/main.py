from datetime import datetime, timedelta
import time
import os

def get_event_date():
    try:
        user_input = input('Enter the event date and time (YYYY-MM-DD HH:MM:SS): ')
        return datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid date format. Please enter the date and time in the correct format.")
        return None

def calculate_time_remaining(event_date):  # Fixed spelling
    current_time = datetime.now()
    time_difference = event_date - current_time
    return time_difference

def display_countdown(time_left):  # Renamed for clarity
    total_seconds = int(time_left.total_seconds())  # Handle microseconds properly
    if total_seconds < 0:
        return False  # Event passed
    days = total_seconds // (24 * 3600)
    hours = (total_seconds % (24 * 3600)) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    # Clear screen for clean updates (works on most terminals)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Time left: {days} days, {hours:02d} hours, {minutes:02d} minutes, {seconds:02d} seconds')
    return True

def main():
    event_date = get_event_date()
    if not event_date:
        return
    print(f'Event date: {event_date}')
    print('Starting countdown... (Press Ctrl+C to stop)\n')
    while True:
        time_left = calculate_time_remaining(event_date)
        if not display_countdown(time_left):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Event has started!')
            break
        time.sleep(1)

if __name__ == '__main__':
    main()

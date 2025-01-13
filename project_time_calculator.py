def add_time(start, duration, day_of_week=None):
    # Days of the week for reference
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse the start time
    start_hour, rest = start.split(":")
    start_minute, period = rest.split(" ")
    start_hour, start_minute = int(start_hour), int(start_minute)

    # Convert start time to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Calculate the new time
    total_minutes = start_minute + duration_minute
    extra_hours = total_minutes // 60
    new_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hours
    new_hour = total_hours % 24
    days_later = total_hours // 24

    # Convert back to 12-hour format
    if new_hour == 0:
        final_hour = 12
        final_period = "AM"
    elif new_hour < 12:
        final_hour = new_hour
        final_period = "AM"
    elif new_hour == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = new_hour - 12
        final_period = "PM"

    # Prepare the result
    new_time = f"{final_hour}:{new_minute:02} {final_period}"

    if day_of_week:
        # Find the new day of the week
        day_index = days_of_week.index(day_of_week.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Example usage
print(add_time("3:00 PM", "3:10"))  # "6:10 PM"
print(add_time("11:30 AM", "2:32", "Monday"))  # "2:02 PM, Monday"
print(add_time("10:10 PM", "3:30"))  # "1:40 AM (next day)"
print(add_time("11:43 PM", "24:20", "Tuesday"))  # "12:03 AM, Thursday (2 days later)"
print(add_time("6:30 PM", "205:12"))  # "7:42 AM (9 days later)"

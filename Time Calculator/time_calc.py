def add_time(start_time, duration, start_day=None):
    # Extract the hour, minute, and AM/PM indicator from the start time
    start_hour, start_minute_ampm = start_time.split(":")
    start_minute, am_pm = start_minute_ampm.split()

    # Convert the hour to an integer and adjust for PM if necessary
    start_hour = int(start_hour)
    if am_pm == "PM":
        start_hour += 12

    # Extract the duration hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # Compute the new hour and minute
    new_minute = (int(start_minute) + duration_minutes) % 60
    new_hour = start_hour + (int(start_minute) + duration_minutes) // 60 + duration_hours

    # Compute the number of days that have elapsed
    days_elapsed = new_hour // 24
    new_hour %= 24

    # Determine the new AM/PM indicator
    if new_hour < 12:
        new_am_pm = "AM"
    else:
        new_am_pm = "PM"
        new_hour -= 12

    # Format the new time string
    new_time = "{:d}:{:02d} {}".format(new_hour if new_hour != 0 else 12, new_minute, new_am_pm)

    # Format the day of the week if provided
    if start_day:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days.index(start_day.lower().capitalize())
        new_day_index = (start_day_index + days_elapsed) % 7
        new_time += ", " + days[new_day_index]

    # Format the number of days elapsed if necessary
    if days_elapsed == 1:
        new_time += " (next day)"
    elif days_elapsed > 1:
        new_time += " ({} days later)".format(days_elapsed)

    return new_time

print(add_time("11:43 PM", "24:20", "tueSday"))

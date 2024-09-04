import calendar

def print_calendar(month, year):
# Display the calendar for the given month and year
    print(calendar.month(year, month))

# Input month and year
month = int(input("Enter month (MM): "))
year = int(input("Enter year (YYYY): "))

# Print the calendar
print_calendar(month, year)
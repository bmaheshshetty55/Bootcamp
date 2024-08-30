days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

current_day = input("Enter today's day : ")
days_to_add = int(input("Enter the number of days to add: "))


current_day_index = days_of_week.index(current_day)


added_day_index = (current_day_index + days_to_add) % 7


added_day = days_of_week[added_day_index]

print(f"After {days_to_add} days, the day is: {added_day}")
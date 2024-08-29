second=750005
print("given seconds:", second)
days=second//(24*60*60) #86400
print("days:",days)
rem_sec=second%86400
print("remaining second after days estimation",rem_sec)

hours=rem_sec//(60*60) #3600
print("hours:",hours)
rem_sec=rem_sec%3600
print("remaining second after hours estimation",rem_sec)

minutes=rem_sec//60
print("min:",minutes)
rem_sec=rem_sec%60
print("remaining second after minutes estimation",rem_sec)

seconds=rem_sec%60
print("sec:",seconds)

print(f"in second is {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")


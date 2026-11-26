import datetime

#Display Current Date and Time
now = datetime.datetime.now()

print("Current Date and Time:", now)

# Display Current Date

today = datetime.date.today()

print("Today's Date:", today)

# Display Date in Different Format
import datetime

now = datetime.datetime.now()

print(now.strftime("%d-%m-%Y"))

from datetime import datetime
import jdatetime

# Get the current datetime
now = datetime.now()

# Read the user's birthday in a desired format
while True:
    try:
        birthday_str = input("Enter your birthday in the format YYYY-MM-DD HH:MM:SS: ")
        birthday = datetime.strptime(birthday_str, '%Y-%m-%d %H:%M:%S')
        if now>birthday:
            break
        else:
            print("The current date must be greater than the date of birth")
            continue
    except ValueError:
        print("Invalid input. Please enter the date in the format DD/MM/YYYY HH:MM:SS")


# Calculate the total number of seconds that have passed in the user's life
seconds_passed = (now - birthday).total_seconds()

# Print the result
print(f"You have lived for {int(seconds_passed)} seconds.")

# Calculate the next birthday
next_birthday_year = now.year
if now > birthday.replace(year=now.year):
    next_birthday_year += 1
next_birthday = birthday.replace(year=next_birthday_year)

# Calculate the number of days and minutes remaining until the next birthday
time_left = next_birthday - now
days_left = time_left.days
minutes_left = time_left.seconds // 60

# Print the result
print(f"Congratulations!!! There are {days_left} days and {minutes_left} minutes left until your next birthday.")



# Convert the Gregorian calendar date and time to the Jalali calendar date and time
jbirthday = jdatetime.datetime.fromgregorian(datetime=birthday)

# Print the result
print("Your birthday in Jalali (Hijri) format is: ", jbirthday.strftime('%Y/%m/%d %H:%M:%S'))

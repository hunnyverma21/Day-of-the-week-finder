from datetime import datetime

print("=" * 40)
print("       DAY OF THE WEEK FINDER")
print("=" * 40)

date_input = input("\nEnter date (DD-MM-YYYY): ")

try:
    date = datetime.strptime(date_input, "%d-%m-%Y")
    day = date.strftime("%A")

    print("\n" + "-" * 40)
    print(f"Date: {date.strftime('%d-%m-%Y')}")
    print(f"Day: {day}")
    print("-" * 40)

except ValueError:
    print("\nInvalid date format!")
    print("Please enter the date in DD-MM-YYYY format.")

from datetime import datetime

s = input("Enter date YYYY-MM-DD (or press Enter for today): ").strip()

now = datetime.now()

if s:
    d = datetime.strptime(s, "%Y-%m-%d")
    now = datetime.combine(d.date(), now.time())

print("a) Current date and time :", now.strftime("%Y-%m-%d %H:%M:%S"))
print("b) Current year          :", now.year)
print("c) Month of the year     :", now.strftime("%B"), f"({now.month})")
print("d) Week number of year   :", now.strftime("%W"))
print("e) Weekday of the week   :", now.strftime("%A"))
print("f) Day of year           :", now.strftime("%j"))
print("g) Day of the month      :", now.day)
print("h) Day of week (0=Mon)   :", now.weekday())

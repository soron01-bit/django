age = int(input("Enter age in years: "))
if age < 0:
    print("Unborn")
elif age <= 5:
    print("Kid")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teen")
else:
    print("Adult")
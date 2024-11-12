print("Welcome to the Tip Calculator")
bill = int(input("Please enter your bill amount ₹ :  "))
tip = int(input("How much tip you want to give like 10%, 12%, 15% ? : "))
split = int(input("How many people to split the bill ? : "))
cal = (bill + (bill * tip / 100)) / split
print(f"Each person should pay {round(cal,2)}")

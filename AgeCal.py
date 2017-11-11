print("Welcome to the age calculator")
print("Choose one of the following options\n")
print("1) Calculate my age in weeks")
print("2) Calculate my age in days")
print("3) Calculate my age in hours")
print("4) Calculate my age in seconds")

choice = int(input("\nEnter the number of the option: "))

age = int(input("How old are you (in years)? "))

if choice == 1:
	age = age * (365/7)
elif choice == 2:
	age = age * 365
elif choice == 3:
	age = age * 365 * 24
	
print("%.2f" % age)


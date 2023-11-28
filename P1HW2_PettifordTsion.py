#Tsion Pettiford 
#09/26/2023
#input and output math 

budget= int(input("Enter Budget: "))

dest = input("Where are you traveling?")
gas= int(input("Enter gas budget: "))
food= int (input("Enter hotel budget: "))
hotel= int(input("Enter food budget:"))


expenses= gas+food+hotel

print("------Travel Expenses-------")
print("Location: ", dest)
print("Initial budget: ", budget)
print()
print("Gas Cost: ", gas)
print("Food Cost: ", food)
print("Hotel Cost: ", hotel)

print("Remaining Balance:", budget-expenses)

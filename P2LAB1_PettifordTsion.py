#Tsion Pettiford
#P2LAB1
#10/05/2023

#making a float varible for miles per gallon of vehicle
mpg = float(input("Enter the vehicle's miles per gallon: "))

#making a float variable for cost per gallon
costpg = float(input("Enter the cost per gallon: "))

#taking the mgp that the user enetered and dividing it by the cost.
cost_20 = (20/mpg) *costpg
cost_75 = (75/mpg) *costpg
cost_500 = (500/mpg) *costpg

#print out the cost for each mpg
print(f'The cost for 20 miles is: ${cost_20:.2f}')
print(f'The cost for 75 miles is: ${cost_75:.2f}')
print(f'The cost for 500 miles is: ${cost_500:.2f}')

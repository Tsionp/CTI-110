#Tsion Pettiford
#P2LAB1
#10/05/2023

#creating the 4 float input variables
num1 = float(input("Enter a number: "))
num2 = float(input("Enetr a number: "))
num3 = float(input("Enter a number: "))
num4 = float(input("Enter a number: "))

#calculating the product of the numbers entered by the user
product = (num1*num2*num3*num4)
#calculating the average of the numbers entered by the user
average = (num1 + num2 + num3 + num4)/4

#printing out the average and the product 
print(f'The product is: {product:.0f} or {product:.3f}')
print(f'The average is: {average:.0f} or {average:.3f}')


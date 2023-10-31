#Tsion Pettiford
#10/31/2023
#using if else, for loops and while loops

#create 2  int variables
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
while num1 >= num2:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    #create the if else statement to see if num1 > num2 
if num1 <= num2:
    for item in range(num1,num2+1,5):  #make it so that the loop starts at num1 value ends at num2 values and increases in incriments of 5. 
        print(item)      #for loop to print out incriments of 5


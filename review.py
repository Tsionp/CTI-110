# Tsion Pettiford
# 1/16/2024
# control structures, oops, and functions

import math
def circum(r):
     c = math.pi * (r**2)
     return c






#create the main function
def main ():
    '''
    #input from the user
    age = int(input("Enter your age: "))
    print(f"You are {age} years old. ")
    #control loop
    if age < 18:
        print("You are legally a minor.")
    else:
        print("You are legallly an adult.")
    print("Hello world")

#create an empty list 
    my_list = [ ]

    for num in range (0,11):
        #add values to the list
        my_list.append (num)

    #print list
    for value in my_list:
        print(value)

    print(my_list)
    
#star tells comp its a list, sep is separate with whatever value you want 
    print(*my_list, sep="  /  ")

'''
#While loop
    again = "yes"
    while again == "yes":
        print("program is running....")
        again = input("Do you want to run the program again? ")
    print("program has ended")


#call circum function
    print (circum(5))

#call the main function

if __name__ == "__main__":
    main()

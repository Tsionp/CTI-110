#Tsion
#10/21/2023
#Working with nested if/else statements and changing code into a function

def days_in_feb(year):
    is_leap = False #Create a boolean variable to hold leap year status

    if year % 4 == 0:           #Does year divide by 4
        if year % 100 == 0:     #Does year divide by 100
            if year % 400 == 0: #Does year divide by 400
                is_leap = True
            else:
                is_leap = False #Does NOT divide by 400
        else:
            is_leap = True      #Does NOT divide by 100
    else:
        is_leap = False         #Does NOT divide by 4

    if is_leap == True:#Print output to user
        print(f"The year {year} has 29 days in February.")
    else:
        print(f"{year} has 28 days in February.")
    


def main():
    my_year = int(input("Enter a year to determine if its a leap year: "))#Get year from user
    days_in_feb(my_year)
    
   
#calling the main function
if __name__ == '__main__':
    main()

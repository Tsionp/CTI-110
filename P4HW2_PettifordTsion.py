# CTI-110
# P3HW2 - Salary
# Tsion Pettiford
# 10/26/2023
#usues if/else statements
num_employees = 0

name = input("Enter employee's name: ")    #get employee name from user

while name != "Done":
    num_employees += 1 #calculates how many employees you entered into the system
    hworked = float(input('Enter number of hours worked: '))    # get number of hours from user
    payrate =float(input("Enter eployee's pay rate: "))   #get payrate from user
    print("---------------------------")
    print("Employee name: "+name)

    #determine if user has worked overtime and calculate the hours
    if hworked > 40:
        overtimeH = hworked -40
    else:
        overtimeH = 0

    #calculate reg hours worked
    if overtimeH >0:
        reghours = hworked-overtimeH
    else:
        reghours = hworked

    #calculate pay for reg hours
    regpay = reghours * payrate 

    #calc overtime pay (reg pay times 1.5)
    otprate = payrate * 1.5
    overtimepay = (otprate * overtimeH)

    #print all the calculations (name, payrate, reg hours. overtime hours, overtime pay, gross pay)
    print(f'Hours worked: "{hworked:.2f}')
    print(f'Payrate: ${payrate:.2f} per hour')
    print(f'Overtime: {overtimeH:.2f} hours')
    print(f'Overtime Pay: ${overtimepay:.2f}')
    print(f'RegHour Pay: ${regpay:.2f}')
    print(f'Gross Pay: ${regpay+overtimepay:.2f}')
    name =input("Enter the employee's name: \n")
print("The amount of employees is: ", num_employees) #shows how many employees were entered

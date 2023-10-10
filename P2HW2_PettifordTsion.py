#CTI-110
#Tsion Pettiford
#10/10/2023
#P2HW2 - List
#working with lsits

#create 6 variables based off the user's input
mod1 = float(input("Enter the grade you recieved for Module 1 test: "))
mod2 = float(input("Enter the grade you recieved for Module 2 test: "))
mod3 = float(input("Enter the grade you recieved for Module 3 test: "))
mod4 = float(input("Enter the grade you recieved for Module 4 test: "))
mod5 = float(input("Enter the grade you recieved for Module 5 test: "))
mod6 = float(input("Enter the grade you recieved for Module 6 test: "))
#create list and add varibales 
grade_list = [mod1, mod2, mod3, mod4, mod5, mod6]
#make variable average using len and calculate
gradeav = sum(grade_list)/len(grade_list)

#calculate max/min/sum/ and assign to show the user
print(f'The highest score is:  {max(grade_list):.2f}')
print(f'The lowest score is:  {min(grade_list):.2f}')
print(f'The accumalative score is: {sum(grade_list):.2f}')
print(f'The highest score is:  {max(grade_list):.2f}')
#show user the average
print("The average of all the grades is: ", gradeav)



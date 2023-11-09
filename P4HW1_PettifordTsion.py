#CTI-110
#Tsion Pettiford
#10/10/2023
#P2HW2 - List
#working with for and while loops

#create 6 variables based off the user's input
num_grades = int(input("How many grades will you enter? ")) #ask the user how many grades they are going to enter
grade_list = [] #create empty list 
for grade in range(num_grades):
    this_grade = int(input("Enter a grade: "))
   

    while this_grade < 0 or this_grade > 100: #check if the grade is valid 
        print("Invalid grade.")
        this_grade = int(input("Enter a grade: "))

grade_list.append(this_grade) #add the valid grade to the list 
print("Grades have been adeded to the list. ")

for grade in grade_list:
    print(grade)
                       
#make variable average using len and calculate
gradeav = sum(grade_list)/len(grade_list)

#calculate max/min/sum/ and assign to show the user
print(f'The highest score is:  {max(grade_list):.2f}')
print(f'The lowest score is:  {min(grade_list):.2f}')
print(f'The accumalative score is: {sum(grade_list):.2f}')
print(f'The highest score is:  {max(grade_list):.2f}')
#show user the average
print("The average of all the grades is: ", gradeav)




#Tsion Pettiford
#Oct/21/2023
#debugging code

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list

grade_list = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grade_list)
high = max(grade_list)
summ = sum(grade_list)
average = (summ/len(grade_list))

# determine letter grade for average

if average >= 90:
    print('Your grade is: A')
elif average >= 80:
        print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else: 
    print('Your grade is: F') 

#Tsion Pettiford
#10/05/2023
#Input to dictionary output


#obtaining input variables from the user 
name = input("What is your name? ")
hair = input("What color is your hair? ")
eye = input("What color are your eyes? ")
height = float(input("How tall are you?(use a decimal point.) "))
age = int(input("What color is your age? "))
food = input("What is your favorite food? ")

#create a dictionary using curly braces
person_dict = {"Name": name, "hairColor": hair, "eyeColor": eye, "Height": height, "Age": age, "Food": food}

#get values using the key
print(f"{person_dict['Name']} is a {person_dict['Height']}' tall student with {person_dict['hairColor']} hair and {person_dict['eyeColor']} eyes. They are {person_dict['Age']}\
years old and their favorite food is {person_dict['Food']}.")

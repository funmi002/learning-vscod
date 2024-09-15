#printing and string manipulation 
name = input("Enter your name:")
print("Hello", name , "welcome to python programming")

first_name = input("Enter your first name: ")
last_name = input("Enter your last_name")
full_name = first_name + "" +last_name 
print(full_name.upper)

#user input and variables
age = int(input("Enter your age: "))
years_left = 100 - age
print("You will turn 100 in", years_left, "years")

score = int(input("Enter your test score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70: 
    grade = "C" 
elif score >= 60:
    grade = "D"
else:
    grade = "F"        
print("Your grade is:", grade) 

#Logical operators
age = int(input("Enter your age: "))
driving_license = input("Do you have a driving license? ")
if age >= 18 and driving_license.lower == "yes": 
    print("You are allowed to drive")
else: 
    print("You are not allowed to drive")    

#Randomization
#Dice roll
import random 
random_number = random.randint(1, 6)
print(random_number)


#Rock, Paper, Scissors Game
import random
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter your choice (rock/paper/scissors): ")
if user_choice == computer_choice:
    print("Tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    print("Computer wins!")

   



#list operations
foods = ["Rice", "Beans", "pancakes", "fish", "bread"]
foods.append("chicken")
foods.insert(2, "yam")
foods.remove("bread")
foods.sort()
print(foods)

#combining list and randomizations
import random
friends = []
for i in range(5):
    friends.append(input(f"Enter friend {i+1}'s name: "))
    friends.append(name)
winner = random.choice(friends)
print("The winner is:", winner)

#GitHub
#GitHub is an online platformfor version control and collaboratiion. 
#It allows developers to store code online, track changes and collaborate with others on projects. 

#step1: OPEN VS Code and click the extensioms icon 
#step2: search for python and select
#step 3: click intall and install the extension

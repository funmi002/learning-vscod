#Dice Roller Simulation
import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
total = dice1 + dice2
print(f"You rolled a {dice1} and a {dice2}. Total: {total}")


#Random Meal Selector
import random
breakfasts = ["Bread", "Pancakes", "custard"]
lunches = ["Spaghetti", "Salad", "Soup"]
dinners = ["Moi Moi", "Rice", "Beans"]
meal_plan = [random.choice(breakfasts), random.choice(lunches), random.choice(dinners)]
print("Today's meal plan:", meal_plan)

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

#list
#Favorite Foods List

favorite_foods = ["Pizza", "jollof rice", "beans", "egusi soup", "Ice Cream"]
favorite_foods.append("vegetable")
favorite_foods.insert(2, "jollof rice")
favorite_foods.remove("beans")
favorite_foods.reverse()
favorite_foods.sort()
print(favorite_foods)


#Random Name Selector
import random
friends = []
for i in range(5):
    friends.append(input(f"Enter friend {i+1}'s name: "))
winner = random.choice(friends)
print("The winner is:", winner)


#Random Team Generator
import random
names = []
num_players = int(input("Enter number of players: "))
for i in range(num_players):
    names.append(input(f"Enter player {i+1}'s name: "))
random.shuffle(names)
team1 = names[:num_players//2]
team2 = names[num_players//2:]
print("Team 1:", team1)
print("Team 2:", team2)


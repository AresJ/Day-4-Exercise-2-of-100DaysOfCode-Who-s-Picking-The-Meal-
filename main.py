# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
maxIndex = len(names) - 1
random_spot = random.randint(0, maxIndex)
print("{} is going to buy the meal today!".format(names[random_spot].capitalize()))


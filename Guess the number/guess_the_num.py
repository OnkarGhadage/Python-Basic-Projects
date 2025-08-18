import random as rd   #imported random to generate random number

target = rd.randint(1,100)   #Generates random value
# print(target)   #To check if random number is generated (Don't cheat 😄)

while True:   #Loop runs till guessed num is correct
    user = int(input("Enter Num (1-100) : "))   #Take user ip

    if user == target:   #If user guessed it write then show Win and break from loop
        print("Guessed it right. You WIN!")
        break
    elif user > target:   #If user ip is larger than target tell user to guess smaller
        print("You entered large num. Guess smaller")
    else:   #Otherwise tell guess larger i.e. when user ip is smaller than target
        print("You entered small num. Guess larger")

print("---Game Over---")   #Lastely ---Game Over---

#Happy game play 👍

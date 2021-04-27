import random
guess = int(input("Enter a number between 1 to 10: "))
n=random.randint(1,10)
while n != guess:
    if (guess<n and count<3): 
        print("The guessed number is too small. Guess Again")
        guess = int(input("Enter a number between 1 to 10: "))
    elif (guess>n and count<3):
        print("The guessed number is too high. Guess Again")
        guess = int(input("Enter a number between 1 to 10: "))
    continue
print("The Guess is correct")

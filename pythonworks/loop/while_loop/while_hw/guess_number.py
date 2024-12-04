# 11. Guess the Number Game:
#     - Write a Python program that asks the user to guess a number between 1 and 10 until they get it right using a `while` loop.

system_guess = int(input("number between 1 - 10 :"))

i = 1
while(i <= 10):
    user_guess = int(input('enter number to guess between 1 - 10 :'))
    if user_guess == system_guess:
        print(f"You have guesses the number correctly, the number was {system_guess}")
    else:
        print("try again")
  

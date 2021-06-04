import random
print('Number Guessing Game')
number = random.randint(1,9)
chances = 0
print('Guess a Number(between 1 to 9):')
while chances < 5:
    guess = int(input('Enter your number:'))

    if guess == number:
         print('Congratulations YOU WON!!!')
         break 

    elif guess < number:
         print('Your Guess was too low: Guess a number higher than that', guess)

    else :
        print('Your Guess was too high: Guess a number lower than that',guess)

    chances+=1
        

    if not chances < 5:
        print('YOU LOSE!!! The number is', number)

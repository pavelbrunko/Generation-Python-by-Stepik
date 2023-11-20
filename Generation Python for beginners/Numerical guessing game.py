import random
unknown_num = random.randint(1, 101)
print('Welcome to numeric guessing game! You need to guess the number, which we made a wish for')
print('Please, enter your number')

#Проверка введённого числа
def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False
attends = 0
while True:
    num = input()
    if not is_valid(num):
        print('Or maybe we can still enter a number from 1 to 100?')
        continue
    num = int(num)

    if num < unknown_num:
        print('Your number is less than the one you made, try again')
        attends += 1
    elif num > unknown_num:
        print('Your number is bigger than the one you made, try again')
        attends += 1
    else:
        print('You guessed it, congratulations!')
        break
    
print('You guessed right with', attends, 'times!')
print('Thank you for playing the number guessing game. See you again...')
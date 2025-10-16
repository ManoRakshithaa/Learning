import random

print('-------Guess the number!-------')

try:
    a = int(input('\nEnter a lower number for the range: '))
    b = int(input('Enter a higher number for the range: '))

    secret_num = random.randint(a, b)
    
except ValueError:
    print('Oopsie! That is not a valid number. Re-Run the program again.')


else:

    count = 1
    guess = int(input(f'Guess the number between {a} and {b}: '))

    while guess != secret_num:
    
        if guess > secret_num:
            print('Too high')
            
        elif guess < secret_num:
            print('Too low')
            
        guess = int(input('Try again: '))
        count += 1

    
print(f'You got it! The number was {secret_num}!')
print(f'You tried {count} times')
              
            

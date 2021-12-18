import random

real_number = random.randint(1,10)
attempt = 0
attempt_limit = 3
print(real_number)
print('You have 3 attempts')
while attempt < attempt_limit:
    attempt += 1
    guess_num = int(input('Guess the number: '))
    if guess_num == real_number:
        print('You won')
        break
else:
    print('LOOSE!')


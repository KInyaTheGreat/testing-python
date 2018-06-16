num = 7
running = True

while running:
    guess = int(input('Enter an integer:'))

    if guess == num :
        print('Congratulations,you guessed it right')
    elif guess < num :
            print('No,its higher than that')
    else:
        print('no,its lower than that')


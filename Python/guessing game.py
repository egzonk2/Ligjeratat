secret_number = 9
Guess_count = 0
guess_limit = 3
while Guess_count < guess_limit:
    guess = int(input('guess number: '))
    Guess_count += 1
    if guess == secret_number:
        print('you won!')
        break
else:
    print('ran out of attempts.')
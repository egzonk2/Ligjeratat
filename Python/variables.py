price = 10 
buyer = 25

Guess = input('if a buyer has 25 dollars and buys an item worth 10 how much money does the buyer have left ? ')


money_left = buyer - price 
print(money_left)
if int(Guess) == money_left:
    print('correct')
else:
    print('wrong')

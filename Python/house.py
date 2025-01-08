buyer_has_good_credit = True

house = 1000000

if buyer_has_good_credit:
    down_payement = house * 0.1
else:
    down_payement = house * 0.2
print(f"down_payement: ${down_payement}")


answer = input('Do you want to convert kilograms to pounds or pounds to kilograms? say kilogram for kilo to pound and say pound for pound to kilo. ')

if answer == "kilogram":
    kilo_to_pound = input('what is the kilo value? ')
    print(int(kilo_to_pound) * 2.205) 
elif answer == "pound":
    pound_to_kilo = input('what is the pound value? ')
    print(int(pound_to_kilo) * 0.453 )
else:
    print('this is an unavailable answer')
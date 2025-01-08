Temperature = input("What Temperature is it ? ") 

if int(Temperature) > 30:
    print('its a hot day')
elif int(Temperature) < 10:
    print('its a cold day')
else:
    print('its a great day')

Name_length = input("What is your Name? ") 

if len(Name_length) < 3:
    print('Name must be more than 3 letters')
elif len(Name_length) > 50:
    print('Name must be less than 50 letters')
else:
    print('Name looks good!')
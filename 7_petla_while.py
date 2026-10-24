pin = 1234
counter = 0
user_pin = int(input('Podaj pin:   '))
while user_pin != pin:
    print('Zły pin')
    user_pin = int(input('Podaj pin:   '))
    counter = counter + 1
    counter += 1

print('Pin poprawny')
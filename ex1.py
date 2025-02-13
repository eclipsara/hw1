age = int(input('Enter your age: '))
if 0 < age < 5:
    price = 5
elif 5 < age < 10:
    price = 10
elif 10 < age < 20:
    price = 20
elif 20 < age < 30:
    price = 40
else:
    price = 50
print(f'The ticket price is {price}$.')

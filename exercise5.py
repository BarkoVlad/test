age = int(input('Введите возраст : '))
if age < 3:
    ticket1 = 0
    print('Цена билета', ticket1)
elif age <= 12:
    ticket2 = 14
    print('Цена билета', ticket2)
elif age >= 65:
    ticket3 = 18
    print('Цена билета', ticket3)
else:
    ticket4 = 23
    print('Цена билета', ticket4)
check = int(input('Введите сумму заказа : '))
tax = check * 0.13
tips = check * 0.18
final_check = check - tax - tips
my_check = [tax, tips, final_check]
print(my_check)

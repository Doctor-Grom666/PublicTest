a = int(input('Количество билетов к заказу:'))
b = [int(input('Возраст посетителя:')) for i in range(a)]

sum = 0

for i in b:
    if 18 <= i <= 25:
        sum += 990
    elif i > 25:
        sum += 1390

if a > 3:
    sum = sum * 9 / 10

print('Сумма к оплате:', sum, 'рублей')
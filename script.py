per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму:'))
deposit = [i * (money / 100) for i in per_cent.values()]
print(int(max(deposit)))
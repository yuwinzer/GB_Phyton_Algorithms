# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
# ...Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элеменнтов ряда чисел: 1 -0.5 0.25 -0.125..., которое нужно суммировать:\n')) - 2

res = int(1)
sum_n = res
for i in range(n+1):
    res = (res/2) * (-1)
    sum_n += res

print(f'Последний складываемый элемент: {res}')
print(f'Сумма всех элементов: {sum_n}')

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

inp_n = input('Введите числа, среди которых нужно найти наибольшее по сумме цифр:\n').split(' ')
map_object = map(int, inp_n)
list_of_integers = list(map_object)

max_n = list_of_integers[0]
sum_max_n = 0
for i in range(1, len(list_of_integers)):
    first = sum(int(d) for d in str(list_of_integers[i]))
    second = sum(int(d) for d in str(list_of_integers[i-1]))
    if first > second:
            max_n = list_of_integers[i]
            sum_max_n = first

print(f'Число с наибольшей суммой цифер: {max_n}')
print(f'Сумма цифер: {sum_max_n}')

# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import time


# блок кода для создания рандомного процента от 0 до 1 на основе секунд текущего времени
t = time.localtime()
current_time = time.strftime("%S", t)
rand_percent = int(current_time)*0.016781  # перевод 60-бальной системы в 100-бальную

print(f"Для получения случайного целого числа в заданных пределах")
lim_1, lim_2 = [int(i) for i in input("Введите диапазон значений через пробел: ").split()]
diff = lim_2 - lim_1
if diff != 0:
    result = lim_1 + diff*rand_percent
else:
    result = lim_1
print(f"Случайное целое число в заданных пределах: {int(result)}")

print(f"Для получения случайного вещественного числа в заданных пределах")
lim_1, lim_2 = [float(i) for i in input("Введите диапазон значений через пробел: ").split()]
diff = lim_2 - lim_1
if diff != 0:
    result = lim_1 + diff*rand_percent
else:
    result = lim_1
print(f"Случайное вещественное число в заданных пределах: {result}")

print(f"Для получения случайного символа в заданных пределах")
lim_1, lim_2 = [ord(i) for i in input("Введите диапазон значений через пробел: ").split()]
diff = lim_2 - lim_1
if diff != 0:
    result = lim_1 + diff*rand_percent
else:
    result = lim_1
print(f"Случайный символ в заданных пределах: {chr(int(result))}")




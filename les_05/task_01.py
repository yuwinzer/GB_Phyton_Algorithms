# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

companies = {}
n = int(input("Введите количество компаний: "))
count = 0
for i in range(n):
    company_name = input(f"Введите название {i+1}-й компании: ")
    quarter_income = [int(i) for i in input("Введите 4 значения прибыли за 4 квартала: ").split()]
    quarter_sum = sum(quarter_income)
    companies[company_name] = quarter_sum
    count += quarter_sum

avrg = count / n
print(f"Средняя прибыль за год всех компаний: {round(avrg,2)}. \nКомпании с прибылью выше средней:")
for i in companies:
    if companies[i] > avrg:
        print(i)
print("\nКомпании с прибылью ниже средней:")
for i in companies:
    if companies[i] < avrg:
        print(i)




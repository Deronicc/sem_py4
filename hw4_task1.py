""" Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. 
n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.  """

import random
n = int(input("Введите количесво элментов первого набора n: "))
m = int(input("Введите количесво элментов первого набора m: "))
first = list(random.randint(0, 10) for i in range(n))
second = list(random.randint(0, 10) for i in range(m))

print('Набор n:', first)
print('Набор m:', second)

result = set(first) and set(second)

print("Встречаемые числа: ", result)
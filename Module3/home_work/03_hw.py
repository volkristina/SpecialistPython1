# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.
import random
numbers = []
n = 8
for _ in range(n):
    number = random.randint(-100, 100)
    numbers.append(number)
print(numbers)
summa = 0
for number in numbers:
    if number % 2 == 0 and number > 0:
        summa += number

print(summa)

# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
numbers = []
# print(random.randint(10, 20))  # раскомментируйте, чтобы посмотреть работу функции randint
# TODO: your code here
import random
numbers = []
n = 6
i = 0
while i < n:
    number = random.randint(10, 20)
    numbers.append(number)
    i += 1

for _ in range(n):
    number = random.randint(10, 20)
    numbers.append(number)

# print(numbers)

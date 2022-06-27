# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here
n = int(input("Введите количество коров: "))
n2 = n % 100
if n2 % 10 == 1 and n2 != 11:
    print(n, "Корова")
elif 2 <= n2 % 10 <= 4 and not(12 <= n2 <= 14):
    print(n, "Коровы")
else:
    print(n, "Коров")

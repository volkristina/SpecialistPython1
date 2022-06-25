# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = int(input("a: "))
b = int(input("b: "))
if a > b:
    a, b = b, a
n = 0
for i in range(a, b + 1):
    if palidrome(i):
        n +=1

print(n)

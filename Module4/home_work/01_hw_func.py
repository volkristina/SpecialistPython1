# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    # TODO: your code here
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

def lucky_ticket(ticket_number):
    numbers = str(ticket_number)
    sum1 = 0
    for number in numbers[:3]:
        sum1 += int(number)
    sum2 = 0
    for number in numbers[3:]:
        sum2 += int(number)
    return sum1 == sum2


def lucky_ticket_v2(ticket_number):
    if len(str(ticket_number)) == 6:
        half_1 = ticket_number // 100000 + ticket_number // 10000 % 10 + ticket_number // 1000 % 10
        half_2 = ticket_number // 100 % 10 + ticket_number // 10 % 10 + ticket_number % 10
        return half_1 == half_2
    return False

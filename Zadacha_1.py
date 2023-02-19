''' Найдите сумму цифр трехзначного числа.
Пример:
 123 -> 6 (1 + 2 + 3)
 100 -> 1 (1 + 0 + 0)
'''
namber = int (input('Введите 3-х значное число: '))

sum = 0
digit_1 = int (namber % 10)
digit_2 = int (namber % 100) // 10
digit_3 = int (namber % 1000) // 100

sum = digit_1 + digit_2 + digit_3

print(sum)
'''
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют
такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
'''

Ticket = int (input('Введите номер билета (6 чисел): '))
digit_1 = Ticket % 10
digit_2 = (Ticket % 100) // 10
digit_3 = (Ticket % 1000) // 100
digit_4 = (Ticket % 10000) // 1000
digit_5 = (Ticket % 100000) // 10000
digit_6 = (Ticket % 1000000) // 100000

number_1 = digit_1 + digit_2 + digit_3
number_2 = digit_4 + digit_5 + digit_6

print(f'Сумма первых 3-х чисел равна: {number_1}')
print(f'Сумма последних 3-х чисел равна: {number_2}')
print('Примечание: Если сумма первых трех чисел совпадает с суммой последних трех чисел, то такой билет называют "Счастливым"')
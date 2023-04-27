# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summ(firstNum, secondNum):
    if (secondNum == 0):
        return firstNum
    if (secondNum != 0):
        return (1 + summ(firstNum, secondNum - 1))
firstNum = int(input("Введите первое число: "))
secondNum = int(input("Введите второе число: "))
print("Результат суммирования равен:", summ(firstNum, secondNum))
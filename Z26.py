# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exp():
    A = int(input("Введите число A: "))
    B = int(input("Введите число B: "))
    value = step(A, B)
    print(f'Число {A} в степени {B} равняется {value}')
def step(A, B):
    if B == 0:
        return 1
    return A * (step(A, B - 1))
exp()
print ('Введите степень числа 2')
n = int(input())

if n <= 100:
    result = 2 ** n
    print('Результат: ' + str(result))
else:
    print ('Ошибка! Введена слишком большая степень!')


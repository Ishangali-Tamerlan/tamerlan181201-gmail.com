print ('Введите не превышающее 10000 число, и мы выведем крайнюю цифру этого числа')
whole_number = int(input())

if whole_number <= 10000:
    number = (whole_number % 10)
    print ('Результат: ' + str(number))
else:
    print('Ошибка! Введено слишком большое число!')

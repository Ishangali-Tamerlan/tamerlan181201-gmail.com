stroka = input()
count = len(stroka) - len(stroka.replace('f', ''))
if count == 0:
    pass
elif count == 1:
    print(stroka.index('f'))
else:
    print(stroka.index('f'), stroka.rindex('f'))

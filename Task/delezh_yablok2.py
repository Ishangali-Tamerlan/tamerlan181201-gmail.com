print('Students?')
students = int(input())
print('How many apples do they have?')
apples = int(input())

if apples > 10000:
    print('Error: This number is bigger than 10000!')
elif 0 < apples <= 10000:
    result = apples - ((apples // students) * students)
    print ('This apples in korzina' + ' ' + '=' +' ' + str(result))

else:
    print ('Incorrect number')

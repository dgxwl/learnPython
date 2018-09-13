height = float(input('Input your height: '))
weight = float(input('Input your weight: '))

bmi = weight / (height * height)

if bmi < 18.5:
    print('Too light.')
elif bmi >= 18.5 and bmi < 25:
    print('Ok.')
elif bmi >= 25 and bmi < 28:
    print('Heavy.')
elif bmi >= 28 and bmi < 32:
    print('Too Heavy.')
elif bmi >= 32:
    print('Very Heavy.')
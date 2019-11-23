operators = ['+', '-', '*', '/']

while True:
    try:
       number1 = int(input("Zadej první číslo: "))
       break
    except ValueError:
        continue

while True:   
    try:
        number2 = int(input("Zadej druhé číslo: "))
        break
    except ValueError:
        continue

while True:
    operator = input("Zadej operátor: ")
    if operator in operators:
        break

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
else:
    try:
        print(number1 / number2)
    except ZeroDivisionError:
        print('Nulou dělit nelze')
     

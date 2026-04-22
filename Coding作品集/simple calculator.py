num1=float(input('Please input the first number:'))
num2=float(input('Please input the second number:'))
operation=input('Please choose the operation:+,-,*,/:')

if operation=='+':
    print(f'result={num1 + num2}')
elif operation=='-':
    print(f'result={num1 - num2}')
elif operation=='*':
    print(f'result={num1 * num2}')
elif operation=='/':
    print(f'result={num1 / num2}')
else:
    print('operation invalid')
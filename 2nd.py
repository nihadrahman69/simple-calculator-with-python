from first import m_sin, m_cos
from first import add, sub, mul, div

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("select operation (+,_,*,/,sin,cos): ")

operation = input()
match operation:
    case "+":
        print(add(num1,num2))
    case "-":
        print(sub(num1,num2))
    case "*":
        print(mul(num1,num2))
    case "/":
        print(div(num1,num2))
    case "sin":
        print(m_sin(num1))
        print(m_sin(num2))
    case "cos":
        print(m_cos(num1))
        print(m_cos(num2))  
  
"""if operation == '+': 
    print(add(num1, num2))
if operation == '-':
    print(sub(num1, num2))
if operation == '*':
    print(mul(num1, num2))
if operation == '/':
    print(div(num1, num2))
if operation == 'sin':
    print(m_sin(num1))
    print(m_sin(num2))
if operation == 'cos':
    print(m_cos(num1))
    print(m_cos(num2))"""


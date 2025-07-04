
num1 = float(input("Dame el primer número: "))
operador = input("Dame el operador: ")
num2 = float(input("Dame el segundo número: "))

def calculadora(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*" or operador == "x":
        return num1 * num2
    elif operador == "/":
        return num1 / num2
    else:
        print("Ese no es un operador permitido")

print(calculadora(num1, num2, operador))
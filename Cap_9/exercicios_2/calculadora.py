def calculadora(num1, operador, num2):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        return num1 / num2
    else:
        return "Operador Inválido."
    
try: #O bloco try é onde deve ser colocado o código que pode causar um erro.
    numero1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador matemático [+ - * /]: ")
    numero2 = float(input("Digite o segundo número: "))

    resultado = calculadora(numero1, operador, numero2)
    print(f"Resultado: {resultado}")
except ValueError:
    print("Entrada inválida! Por favor, digite números válidos.")
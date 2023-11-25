"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
"""


def calc(numero_1, numero_2, operacao):
    if operacao == 1:
        resultado = numero_1 + numero_2
    elif operacao == 2:
        resultado = numero_1 - numero_2
    elif operacao == 3:
        resultado = numero_1 * numero_2
    elif operacao == 4:
        if(numero_2 != 0):
            resultado = numero_1 / numero_2
        else:
            print("Error operaçao")
            return 0
    else:
        print("Operação inválida. Escolha uma operação válida: 1, 2, 3, ou 4.")
        return 0
    return resultado
    

resultadoSoma = calc(5, 3, 5)
print("Soma:", resultadoSoma)
        
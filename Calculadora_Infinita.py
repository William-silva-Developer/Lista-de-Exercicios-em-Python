"""
Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando 
infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem 
“Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar 
a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.
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

exercutando = True
while(exercutando == True):
    print("Escolhar a Operação desejada.")
    print("1: Somar 2: Subtrair 3: Multiplicar 4: Dividir 0: Sair")
    operacao = int(input())
    if((operacao < 0) or (operacao > 4)):
        print("Opção não existente.")
    elif (operacao == 0):
        exercutando = False
        print("-------------------Fim-----------------------")
    else:
        print("Informe o primeiro número: ")
        numero_1 = int(input())
        print("Informe o segundo número: ")
        numero_2 = int(input())
        resultado = calc(numero_1, numero_2, operacao)
        print("---------------- Resultado -------------------------------")
        print("Resultado: " ,resultado)
        print("----------------------------------------------------------")
    

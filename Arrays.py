"""
Declare dois arrays, cada um com um mínimo de cinco elementos, 
e imprima eles no terminal usando o comando print(). O primeiro 
array deve conter os produtos de uma loja da sua escolha (loja de comida,
materiais de construção, música, etc). O segundo array deve conter os anos 
de nascimento de familiares e amigos seus. Lembre-se de usar nomes descritivos
para nomear cada variável, e de usar o tipo de dado apropriado para cada 
lista (strings, booleanos, números inteiros, floats).
"""

array_de_roupas = ["Camisa polo", "Cueca", "Short", "Calça jeans", "camiseta masculina", "camiseta masculina manga longa"]

position01 = array_de_roupas[0]
position02 = array_de_roupas[1]
position03 = array_de_roupas[2]
position04 = array_de_roupas[3]
position05 = array_de_roupas[4]
position06 = array_de_roupas[5]

def listar_roupas():
    for i in array_de_roupas:
        print("Item: "+i)


anos_nascimento = [(1990, 'Amanda'), (1985, 'Wilson'), (1995, 'Carlos'), (1980, 'João'), (2000, 'Ricardo')]
def listar_anos():
    for ano, nome in anos_nascimento:
        print(f'Ano: {ano}, Nome: {nome}')


print("----------------------------------------------------------------")
print("                  Lista de roupas masculinas                   ")
print("----------------------------------------------------------------")

listar_roupas()

print("----------------------------------------------------------------")
print("                    Nomes e anos de nascimento                 ")
print("----------------------------------------------------------------")

listar_anos()


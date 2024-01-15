"""
Num torneio de e-sports é necessário que todos os integrantes da mesma equipe tenham etiquetas que os 
identifiquem. Por exemplo, se o nome da equipe é “Os Lutadores”, o primeiro membro deve 
ter uma etiqueta “Os Lutadores – 1", o segundo membro “Os Lutadores – 2", e assim pela frente.
"""

def gerar_etiquetas(nome_equipe, num_membros):
    etiquetas = []

    for i in range(1, num_membros + 1):
        etiqueta = f"{nome_equipe} - {i}"
        etiquetas.append(etiqueta)

    return etiquetas


nome_equipe = "Os Lutadores"
num_membros = 5

etiquetas_membros = gerar_etiquetas(nome_equipe, num_membros)

for etiqueta in etiquetas_membros:
    print(etiqueta)

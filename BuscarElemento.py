


def acharElemento(elem, arr):
    try:
        achou = False
        for i in range(len(arr)):
            if arr[i] == elem:
                achou = True
                indice_encontrado = i
                break 

        if not achou:
            print("Não achamos o nome:", elem)
        else:
            print("Achamos o nome:", elem)
            print("Valor correspondente:", arr[indice_encontrado])

    except IndexError:
        print("Erro: Índice fora dos limites.")
    except Exception as e:
        print("Erro:", e)


nome_procurado = input("Informe o nome: ")
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
acharElemento(nome_procurado, lista)

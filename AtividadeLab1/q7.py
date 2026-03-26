def inverter_vetor(lista):
    n = len(lista)
    for i in range(n // 2):
        aux = lista[i]
        lista[i] = lista[n - 1 - i]
        lista[n - 1 - i] = aux
    
    return lista

vetor = [10, 20, 30, 40, 50]
res=(inverter_vetor(vetor))
print(res) 
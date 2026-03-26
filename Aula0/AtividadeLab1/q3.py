def maior(lista):
    maior=0
    for n in lista:
        maior = lista[0]
        if n>maior:
            maior=n

    return maior

lista=[1,2,3,4,5,10]
res=(maior(lista))
print(res)
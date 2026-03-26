def somaInt(lista):
    cont=0
    for n in lista:
        if n>0:
            cont=cont+n
    return cont

lista=[1,-2,-3,4,5,-6]
res=(somaInt(lista))
print(res)
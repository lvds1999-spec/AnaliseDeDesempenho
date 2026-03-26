def somaInt(lista):
    cont=0
    for n in lista:
        if n%2==0:
            cont+=1
    return cont

lista=[1,2,3,4,5,6]
res=(somaInt(lista))
print(res)
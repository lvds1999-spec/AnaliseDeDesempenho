def som (lista):
    cont=1
    for n in lista :
        cont=cont*n
    return cont 

lista = [1,2,3,4]
res=(som(lista))
print(res)
def verifMaior(lista,x):
    cont=0
    for n in lista:
        if n==x:
            return True


lista=[1,2,3,8,5,10]
x=5
res=(verifMaior(lista,x))
print(res)
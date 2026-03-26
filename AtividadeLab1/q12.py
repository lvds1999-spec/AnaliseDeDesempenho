def contar_caracteres(texto):
    contador = 0
    for caractere in texto:
        contador += 1
        
    return contador

frase = "teste"
res = contar_caracteres(frase)
print(res)
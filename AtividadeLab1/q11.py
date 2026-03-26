def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
            
    return contador

palavra = "Programaçao"
res = contar_vogais(palavra)
print(res)
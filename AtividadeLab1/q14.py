def contar_caractere(palavra, c):
    cont = 0
    for letra in palavra:
        if letra == c:
            cont += 1
    return cont


print(contar_caractere("banana", "a")) 
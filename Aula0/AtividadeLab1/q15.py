def substituir_caractere(palavra, c1, c2):
    nova_string = ""
    for letra in palavra:
        if letra == c1:
            nova_string += c2
        else:
            nova_string += letra
    return nova_string

print(substituir_caractere("banana", "a", "o"))
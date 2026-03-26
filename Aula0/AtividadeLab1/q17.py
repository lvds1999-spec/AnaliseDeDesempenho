def remover_espacos(s):
    resultado = ""
    for letra in s:
        if letra != " ":
            resultado += letra
    return resultado


print(remover_espacos("ola mundo"))
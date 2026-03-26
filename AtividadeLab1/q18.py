def primeiro_caractere(s):
    contador = 0
    for _ in s:
        contador += 1
    
    if contador == 0:
        return None 
    
    return s[0]

print(primeiro_caractere("python")) 
print(primeiro_caractere(""))       
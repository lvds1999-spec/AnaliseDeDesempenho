def contar_maiusculas_minusculas(s):
    maiusculas = 0
    minusculas = 0
    
    for letra in s:

        if 'A' <= letra <= 'Z':
            maiusculas += 1
        elif 'a' <= letra <= 'z':
            minusculas += 1
            
    return f"Maiúsculas: {maiusculas} | Minúsculas: {minusculas}"

print(contar_maiusculas_minusculas("AbCde"))
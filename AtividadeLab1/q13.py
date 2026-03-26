def verificar_palindromo(s):
    s_limpa = s.lower()
    invertida = ""
    for char in s_limpa:
        invertida = char + invertida
        
    return s_limpa == invertida

print(verificar_palindromo("arara"))
print(verificar_palindromo("casa"))
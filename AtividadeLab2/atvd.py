#questão 02
def fat_recursivo(s):
    if s <= 1: 
        return 1
    return s * fat_recursivo(s - 1)

print(fat_recursivo(5))

#questão 06
def soma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + soma_digitos(n // 10)

numero = 1234
resultado = soma_digitos(numero)
print(resultado)


#questão 18
def somarecursiva(s):
    if s <= 1: 
            return 1
    return s + fat_recursivo(s - 1)

print(somarecursiva(4))


#questão 30

def majoritario(nums):
    candidato = None
    contagem = 0

    for num in nums:
        if contagem == 0:
            candidato = num
            contagem = 1
        elif num == candidato:
            contagem += 1
        else:
            contagem -= 1

    return candidato

print(majoritario([3, 3, 4, 2, 3, 3, 1]))


#questão 09
def mover_zeros(nums):
    nao_zeros = [x for x in nums if x != 0]
    
    zeros = [0] * (len(nums) - len(nao_zeros))
    return nao_zeros + zeros

entrada = [0, 1, 0, 3, 12]
resultado = mover_zeros(entrada)
print(resultado) 
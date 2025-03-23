# Primeiro Exercício: Soma de elementos pares
# Escreva uma função que recebe uma lista de números inteiros e retorna a soma de todos os
# elementos pares contidos nela.
# Exemplo: [2,4,10,3,9,7,15,22]
# Saída: A soma dos pares é: x

def soma_pares(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return f"A soma dos pares é: {soma}"

# Por exemplo:
numeros = [2, 4, 10, 3, 9, 7, 15, 22]
print(soma_pares(numeros))

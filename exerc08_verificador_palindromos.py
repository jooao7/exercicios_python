# Oitavo Exercício: Verificador de Palíndromos
# Escreva uma função que recebe uma palavra e retorna True se for um palíndromo
# (ou seja, se pode ser lida da mesma forma de trás para frente) e False caso contrário.
# Exemplo: entrada = "radar"
# Saída esperada: True

def eh_palindromo(palavra):
    return palavra == palavra[::-1]

# Por exemplo:
entrada = "radar"
print(eh_palindromo(entrada))
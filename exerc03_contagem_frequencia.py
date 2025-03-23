# Terceiro Exercício: Contagem de Frequência
# Escreva uma função que recebe uma lista de strings e retorna um dicionário onde as chaves são os
# elementos da lista e os valores representam quantas vezes cada elemento aparece.
# Exemplo de entrada: ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']
# Saída esperada: {'Java': 2, 'Ruby': 2, 'Javascript': 1}

def contagem_frequencia(lista):
    contagem = {}
    for elemento in lista:
        contagem[elemento] = contagem.get(elemento, 0) + 1
    return contagem

# Por exemplo:
linguagens = ['Java', 'Java', 'Ruby', 'Javascript', 'Ruby']
print(contagem_frequencia(linguagens))

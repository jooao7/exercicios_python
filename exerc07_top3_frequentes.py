# Sétimo Exercício: Top 3 mais frequentes
# Dada uma lista de números, crie uma função que retorne os três números mais frequentes
# em ordem decrescente de frequência. Se houver empates, ordene pelo valor numérico.
# Exemplo: [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
# Saída esperada: [2, 1, 4]

from collections import Counter

def top_3_frequentes(lista):
    contagem = Counter(lista)
    return [item[0] for item in sorted(contagem.items(), key=lambda x: (-x[1], x[0]))[:3]]

# Por exemplo: 
numeros = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
print(top_3_frequentes(numeros))
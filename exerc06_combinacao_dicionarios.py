# Sexto Exercício: Combinação de dicionários
# Escreva uma função que recebe dois dicionários onde as chaves são strings e os valores são inteiros.
# A função deve combinar os dicionários somando os valores das chaves que aparecem em ambos.
# Exemplo: d1 = {"a": 2, "b": 3, "c": 5}, d2 = {"a": 1, "b": 4, "d": 7}
# Saída esperada: {"a": 3, "b": 7, "c": 5, "d": 7}

def combinar_dicionarios(d1, d2):
    resultado = d1.copy()
    for chave, valor in d2.items():
        resultado[chave] = resultado.get(chave, 0) + valor
    return resultado

# Por exemplo:
d1 = {"a": 2, "b": 3, "c": 5}
d2 = {"a": 1, "b": 4, "d": 7}
print(combinar_dicionarios(d1, d2))
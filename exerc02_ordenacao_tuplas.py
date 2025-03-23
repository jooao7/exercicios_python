# Segundo Exercício: Ordenação de Tuplas
# Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
# escreva uma função que retorne a lista ordenada pela idade de forma crescente.
# Exemplo de entrada: [("Samuel", 25), ("Karynne", 22), ("Carol", 20), ("Kleber", 23), ("Vinicius", 28)]
# Saída esperada: [("Carol", 20), ("Karynne", 22), ("Kleber", 23), ("Samuel", 25), ("Vinicius", 28)]

def ordenar_por_idade(lista):
    return sorted(lista, key=lambda pessoa: pessoa[1])

# Por exemplo:
pessoas = [("Samuel", 25), ("Karynne", 22), ("Carol", 20), ("Kleber", 23), ("Vinicius", 28)]
print(ordenar_por_idade(pessoas))

# Quinto Exercício: Tupla de médias
# Dado um dicionário onde as chaves são nomes de alunos e os valores são listas com suas notas,
# crie uma função que retorna uma lista de tuplas, onde cada tupla contém o nome do aluno e sua média de notas.
# Exemplo: {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
# Saída esperada: [("Ana", 8.0), ("Bruno", 5.33), ("Carlos", 9.67)]

def calcular_medias(alunos):
    return [(aluno, round(sum(notas) / len(notas), 2)) for aluno, notas in alunos.items()]

# Por exemplo:
notas_alunos = {"Ana": [8, 9, 7], "Bruno": [5, 6, 5], "Carlos": [10, 9, 10]}
print(calcular_medias(notas_alunos))
# Quarto Exercício: Contagem de Palavras
# Crie uma função que recebe uma string e conta quantas vezes cada palavra aparece nela.
# Retorne um dicionário onde a chave é a palavra e o valor é a quantidade de ocorrências.
# Exemplo: ["banana maçã banana laranja maçã maçã"]
# Saída esperada: {"banana": 2, "maçã": 3, "laranja": 1}

def contagem_palavras(texto):
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

# Por exemplo:
texto = "banana maçã banana laranja maçã maçã"
print(contagem_palavras(texto))
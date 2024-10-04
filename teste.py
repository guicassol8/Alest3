import nltk
from nltk.corpus import words
import random

# Carregue a lista de palavras
word_list = words.words()

# Filtrar palavras com até 5 letras
short_words = [word for word in word_list if len(word) == 5 and word.isalpha() and not word[0].istitle()]

word_list = list(set(short_words))

word_list.sort()

palavras = dict()

def verificarRepeticao(palavra):
    for i in range(len(palavra)):
        if palavra[i] in palavra[(i+1):]:
            return True
    return False


def verificarComum():
    for word in word_list:
        for letter in word:
            if letter not in palavras:
                palavras[letter] = 0
            palavras[letter] += 1
    maiorPalavra = ""
    maiorQuantidade = 0
    for word in word_list:
        if verificarRepeticao(word):
            continue
        quantidadeAtual = 0
        for letter in word:
            if letter in palavras:
                quantidadeAtual += palavras[letter]
        if quantidadeAtual > maiorQuantidade:
            maiorQuantidade = quantidadeAtual
            maiorPalavra = word

    return maiorPalavra

# Exibir as palavras
print(short_words)
print(len(short_words))
print(f"Primeira palavra: {word_list[random.randint(0, len(short_words) - 1)]}")
print(verificarComum())

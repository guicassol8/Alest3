import nltk
import unicodedata
from nltk.corpus import mac_morpho


def rem(texto):
    # Normaliza o texto e remove os acentos
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Carregue a lista de palavras
word_list = mac_morpho.words()

# Filtrar palavras com até 5 letras
short_words = [rem(word) for word in word_list if len(word) == 5 and word.isalpha()]

word_list = list(set(word_list))

# Exibir as palavras
print(short_words)
print(len(short_words))

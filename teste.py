import nltk
import unicodedata
from nltk.corpus import words

def rem(texto):
    # Normaliza o texto e remove os acentos
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Carregue a lista de palavras
word_list = words.words()

# Filtrar palavras com até 5 letras
short_words = [word for word in word_list if len(word) == 5 and word.isalpha() and not word[0].isupper()]

word_list = list(set(word_list))

word_list.sort()

# Exibir as palavras
print(short_words)
print(len(short_words))

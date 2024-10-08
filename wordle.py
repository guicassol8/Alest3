import os
import nltk
#nltk.download('words')
from nltk.corpus import words
import random

word_list = words.words()
descart_list = set()
for word in open("descarte.txt"):
    descart_list.add(word.strip())

short_words = [word.strip() for word in word_list if len(word) == 5 and word.isalpha() and not word[0].istitle() and word.strip() not in descart_list]

word_list = list(set(short_words))
for word in open("adicao.txt"):
    word_list.append(word)


listaOriginal = word_list.copy()

os.system("clear")

valorLetras = dict()
# Quantidade de repeticao de letras
def dicionarioRepeticao():
    for word in word_list:
        for letter in word:
            if letter not in valorLetras:
                valorLetras[letter] = 0
            valorLetras[letter] += 1
dicionarioRepeticao()

def verificarRepeticao(palavra):
    for i in range(len(palavra)):
        if palavra[i] in palavra[(i+1):]:
            return True
    return False

def valorPalavra(palavra):
    valorTotal = 0
    if verificarRepeticao(palavra):
        return 0
    for letra in palavra:
        if letra in valorLetras:
            valorTotal += valorLetras[letra]
    return -valorTotal

def valorPalavraSemRepeticao(palavra):
    valorTotal = 0
    for letra in palavra:
        if letra in valorLetras:
            valorTotal += valorLetras[letra]
    return -valorTotal

def melhorChute():
    for palavra in listaOriginal:
        melhorPalavra = True
        for letra in palavra:
            if letra in posicaoCorreta.values() or letra in letraCorreta:
                melhorPalavra = False
                break
        if melhorPalavra:
            return palavra    

word_list.sort()
word_list = sorted(word_list, key=valorPalavra)

# Chave index, Conteudo letra
posicaoCorreta = dict()

# Chave letra, Conteudo quantidade de aparicoes
letraCorreta = dict()

# Chave index, Conteudo lista de letras que nao estao ali
aliNao = dict()

# Caso esteja preenchido significa que o numero de letras eh aquele 100%
quantAbsoluta = set()

# Palavra com maior quantidade de letras comumm sem repeticoes
firstGuess = "arose"

# Lista de possíveis palavras
possiveisPalavras = []

# - (#) Nao tem
# - ($) Posicao errada
# - (@) Posicao certa

# Depois pensar em uma maneira mais bonita de fazer isso
def parseLinha(linha):
	quantLetra = dict()
	for i in range(0, len(linha), 2):
		if linha[i] == "$":
			if linha[i+1] not in quantLetra:
				quantLetra[linha[i+1]] = 0
			quantLetra[linha[i+1]] += 1
   
			if (i+1)//2 not in aliNao:
				aliNao[(i+1)//2] = []
			aliNao[(i+1)//2].append(linha[i+1])
   
		if linha[i] == "@":
			posicaoCorreta[linha[i+1]] = (i+1)//2
			if linha[i+1] not in quantLetra:
				quantLetra[linha[i+1]] = 0
			quantLetra[linha[i+1]] += 1	

def checarPalavra(palavra):
    for index in posicaoCorreta:
        if palavra[index] != posicaoCorreta[index]:
            print(palavra[index])
            print(posicaoCorreta[index])
            print("false 1")
            return False

    # Chave letra, Conteudo quantidade de aparicoes
    letrasAtuais = dict()
    i = 0
    for letra in palavra:
        if letra not in letrasAtuais:
            letrasAtuais[letra] = 0
        letrasAtuais[letra] += 1
        if i in aliNao:
            if letra in aliNao[i]:
                print("false 1")
                return False
        i += 1

    for letra in letraCorreta:
        if letra in letrasAtuais:
            if letra in quantAbsoluta:
                if letrasAtuais[letra] != letraCorreta[letra]:
                    print("false 4")
                    return False
            elif letrasAtuais[letra] < letraCorreta[letra]:
                print(letrasAtuais[letra] < letraCorreta[letra])
                print(letraCorreta[letra] == 0)
                print(letra)
                print("false 2")
                return False
        else:
            if letraCorreta[letra] == 0:
                continue
            print("false 3")
            return False
    return True


while True:
    escolha = input("1 - AddPosCorreta 2 - AddLetraCorreta 3 - Testar - 4 Sair 5 - AliNao 6 - Randomize 7 - QuantAbsoluta\n")
    if escolha == "1":
        index = int(input("Digite o index\n"))
        letra = input("Digite a letra\n")
        posicaoCorreta[index] = letra
    if escolha == "2":
        letra = input("Digite a letra\n")
        quantidade = int(input("Quantidade\n"))
        letraCorreta[letra] = quantidade
        if quantidade == 0:
            quantAbsoluta.add(letra)
    if escolha == "3":
        for palavra in word_list:
            if checarPalavra(palavra):
                possiveisPalavras.append(palavra)
        word_list = possiveisPalavras.copy()
        possiveisPalavras.clear()
        valorLetras.clear()
        dicionarioRepeticao()
        word_list = sorted(word_list, key=valorPalavra)
        listaOriginal = sorted(listaOriginal, key=valorPalavra)
        print(f"Palavras possiveis: {word_list}")
        print(melhorChute())
    if escolha == "5":
        index = int(input("Digite o index\n"))
        letra = input("Digite a letra\n")
        if index not in aliNao:
            aliNao[index] = []
        aliNao[index].append(letra)
    if escolha == "4":
        break
    if escolha == "6":
        print(word_list[random.randint(0, len(word_list) - 1)])
        print(valorLetras)
    if escolha == "7":
        letra = input("Digite a letra\n")
        quantAbsoluta.add(letra)
    if escolha == "8":
        parseLinha(input("Digite a linha:\n"))

#unit

# Mais um caso possivel eh quando tu tem certeza que aquela letra eh aquilo e pronto ai substituiria o or letraCorreta[letra] == 0 por um certeza, deixando ainda mais especifico

#Informacoes possives:
# - Posicao correta
# - Posicao incorreta
# - Quantas letras de um tipo tem
# - Caso tenha usado mais de uma vez, consegue garantir quantidade, caso seja 0 tambem garante
# - Fazer tambem funcao que caso chegue em um caso e nao achou, que faca por forca bruta ate acertar, caso nao acerte so pegue oq tem ali
# - Caso coloque duas letras iguais, e apenas uma fique acizentada, eu sei que a posicao tambem n eh na do acinzentado
# - Outra coisa que podia ser mais pra frente, é ordenar com o criterio de letras mais comuns, assim seria uma priority queue com o criterio sendo maior quantidade de letras comuns
#   - Por enquanto ta funcionado bem, mas caso queira postar isso no github vou também fazer questão de usar uma heap, já que po tem que mostra que sabe usar
#
# - Vejo duas estrategias possiveis, pegar sempre o primeiro da lista com maior quantidade de repeticao de letras sem repeticao ou maior repeticao em um geral
# - A segunda estrategia tem potencial de eliminar muitas que repetem a mesma letra, mas a grande questao eh que caso seja um caso com letras repetidas geralmente o mesmo problema
# vai se repetir, onde existem muitas palavras quase identicas e nao tem oque fazer, acho que a primeira eh melhor por eliminar mais opcoes no geral, caso a palavra seja muito repetida
# e tenha outras que sao quase iguais, ambas estrategias vao ter o mesmo problema, a segunda eh muito situacional e tem um ganho muuito menor comparado ao primeiro, vamos ficar com o pri
# Refazer o valor das letras pra quando fazer o sort se basear no novo valor atual, vai ajudar a pegar a pelavra que elimina mais outras
# 
# Na real uma estrategia muito interessante, eh pegar 3 palavras com as letras mais comuns que tem no alfabeto e usar as 3, dessa maneira vai ser possivel recolher muitas informacoes
# pq caso chute a primeira e parta dela, sempre tem uma letra (caso acerte algo) que vai estar sendo reutilizada desnecessariamente, no lugar de uma letra que poderia dar uma info nova
# Estrategia que acho AINDA melhor eh uma melhora dessa, eu vou dar o sort denovo no valor das palavras com as informacoes pegas do primeiro (arose) e a partir dai eu vou pegar uma pala
# vra que esta de acordo com o novo dicionario, mas nao repete nenhuma letra de arose, assim vou maximizar ainda mais as informacoes, pegando o valor relativo ao dicionario atual
#
# Depois alem da repeticao da pra fazer uma analise de posicoes mais comuns das letras, isso com certeza seria util
#
# Depois que integrar com site da pra testar varias, mas atualmente oque acredito que faz mais sentido eh, dar 3 chutes que nao repetem letras, mas esses chutes vem da palavra com
# maior repeticao de letras, mas baseado nas descobertas, assim a chance aumenta ainda mais de cortar casos corretos

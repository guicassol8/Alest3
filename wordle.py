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
    word_list.append(word.strip())


listaOriginal = word_list.copy()

os.system("cls")

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

# Lista de palavras que nao tem na lista
palavrasIncorretas = []

# Lista de possíveis palavras
possiveisPalavras = []

def dicionarioRepeticaoQuatro():
    for word in word_list:
        for letter in word:
            if letter not in valorLetras:
                valorLetras[letter] = 0
            if letter not in letraCorreta and letter not in posicaoCorreta.values():
            	valorLetras[letter] += 1

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
			posicaoCorreta[(i+1)//2] = linha[i+1]
			if linha[i+1] not in quantLetra:
				quantLetra[linha[i+1]] = 0
			quantLetra[linha[i+1]] += 1
               
	for letra in quantLetra:
		if letra in letraCorreta:
			if quantLetra[letra] <= letraCorreta[letra]:
				continue
		letraCorreta[letra] = quantLetra[letra]
          
	for i in range(0, len(linha), 2):
		if linha[i]	== "#":
			if linha[i+1] not in letraCorreta:
				letraCorreta[linha[i+1]] = 0
				quantAbsoluta.add(linha[i+1])
			elif letraCorreta[linha[i+1]] != 0:
				if (i+1)//2 not in aliNao:
					aliNao[(i+1)//2] = []
				aliNao[(i+1)//2].append(linha[i+1])
				quantAbsoluta.add(linha[i+1])

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

def printInfos():
	print("Posicoes Corretas:")
	for index in posicaoCorreta:
		print(f"Index: {index} / Palavra: {posicaoCorreta[index]}")
	print("Numero de Letras:")
	for letra in letraCorreta:
		print(f"Letra: {letra} / Quantidade: {letraCorreta[letra]}")
	print("Ali nao ta:")
	for index in aliNao:
		print(f"Index: {index} ", end="")
		for letra in aliNao[index]:
			print(f"Letra: {letra}",end="")
		print("")
	print("Quant Absoluta:")
	for letra in quantAbsoluta:
		print(f"Letra: {letra}")
          
def chuteQuatro():
    global listaOriginal
    valorLetras.clear()
    dicionarioRepeticaoQuatro()
    listaOriginal = sorted(listaOriginal, key=valorPalavra)
    if listaOriginal:
        print(f"Chute Quatro: {listaOriginal[0]}")

def palavraIncorreta(palavra):
	global palavrasIncorretas
	palavrasIncorretas.append(palavra)	

def resetAll():
	global word_list, listaOriginal, posicaoCorreta, letraCorreta, aliNao, quantAbsoluta, palavrasIncorretas, possiveisPalavras, valorLetras
	with open("descarte.txt", "a") as file:
		for palavra in palavrasIncorretas:
			file.write("\n" + palavra)
	palavrasIncorretas.clear()
	word_list = listaOriginal
	valorLetras.clear()
	word_list.sort()
	word_list = sorted(word_list, key=valorPalavra)
	posicaoCorreta.clear()
	letraCorreta.clear()
	aliNao.clear()
	quantAbsoluta.clear()
	possiveisPalavras.clear()

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
        printInfos()
        #print(f"Chute Sugerido: {melhorChute()}")
        chuteQuatro()
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
    if escolha == "9":
        valorLetras.clear()
        dicionarioRepeticaoQuatro()
        listaOriginal = sorted(listaOriginal, key=valorPalavra)
        if listaOriginal:
            print(listaOriginal[0])

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
#
# Talvez seja necessario penser melhor quando ele vai usar o chute ou não, talvez algo de quando chegar a um numero pequeno de opcoes ele muda a maneira
# Da pra fazer algo relacionado com similaridade de palavras, pra escolher a palavra que tem mais coisas comuns com as outras
#
# Alem disso pensar na estrategia pra ele automatizar
# - Comecar chutando 3
# - Caso tenha um chute igual a quantidade de tentativas possiveis so colocar todos e azar
# - Outro eh caso chegue em um numero x de palavras possiveis ja muda um pouco a maneira de pegar o chute (Talvez possa ser quando chega a 4 ou 3, talvez so 4)
# - Caso em algum dos 3 chutes basicos ele fique sem um melhor chute, ele vai pegar o primeiro da word_list, afinal ele tem a maior soma de letras comuns
#
# - Acho que o método atual ta bem valido, ta funcionando bem num geral, provavel que nao preciso mudar
# - Na minha visao o principal problema eh quando pega 4 letras iguais e tem só uma diferenca
#	- Pra esse caso da pra mudar o dicionario de valor de letras, e colocar so aquelas que se destacam do resto e tentar achar uma palavra que exclua o maximo dessas letras possivel
# - Por enquanto a ideia vai ser fazer isso tudo incialmente, mas caso chegue em 4 letras descobertas fazer essa ideia de ver as letras que se destacam e procurar palavras pra excluir
# - Talvez no futuro algo pra 3 letras, mas a principio n me parece necessario
# - De fato analisando a estrategia eh bem efetiva ate chegar 4 letras descobertas, depois so fica ruim, fazer sorte especial
# - Ultima decisao que falta tomar acredito que seja no caso de, nao achou as 4 letras, mas mesmo assim nao tem um chute recomendado, eu pego o primeiro do word_list (letras mais comuns) ou ja vou pro chute de 4
# 	acho que a opcao do quatro deve ser melhor, afinal caso chegue em um None, significa que em muitas letras repetidas já 3 x 2
# - Por fim acho que a partir de sei la, umas 10 palavras sobrando nao se usa mais o chute sugerido, caso chegue no 3 caso e esteja com muito poucas usar o chute 4
# 	da pra fazer algo se o chutePrincipal for diferente do chute 4 usar o chute 4

# - Os atuais dois embates sao, caso o chuteMain seja diferente do chute 4, devo usar o chute 4? Caso o chute principal seja None, uso o primeiro do word_list ou o chute 4?
# 	talvez ate por uma solucao mais simples eu coloque o chute 4, mas vou continuar analisando, por enquanto bem parecido
#
# - Caso eu queira testar depois eu troco as politicas e teste, mas por enquanto caso o chute 4 seja diferente do chute principal, uso o chute 4
# 	- Caso o chute pricipal seja None, se usa o chute 4 nao o primeiro da word_list, com o primeira regra isso ja vai acontecer
# - Motivo: talvez a primeira alteracao nao seja completamente necessaria, mas mesmo assim isso traz uma estabilidade maior pro algoritmo, pegar o primeiro da word_list eh complicado
# - Agora parando pra pensar eu não estou usando literalmente sempre o chute 4? Time que ganha não se mexe!
# - Todos chutes vao ser baseados no chute 4, que aparentemente eh muito copeiro real, servindo pra todos os casos bem
# - Nao vou exluir nada, so comentar, vai que serve depois
# - Unica coisa que falta nesse metodo eh caso a porra da palavra nao existir ele excluir ela e depois procurar a proxima e colocar na lista de descarte, vou colocar isso na funcao 9

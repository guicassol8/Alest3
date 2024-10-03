import os
import unicodedata


def remover_acento(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

os.system("cls")

listaPalavras = [linha.strip() for linha in open("palavras.txt", "r", encoding = "utf-8")]
listaPalavras = [remover_acento(linha) for linha in listaPalavras]

# Chave index, Conteudo letra
posicaoCorreta = dict()

# Chave letra, Conteudo quantidade de aparicoes
letraCorreta = dict()

# Chave index, Conteudo lista de letras que nao estao ali
aliNao = dict()

# Lista de possíveis palavras
possiveisPalavras = []

def checarPalavra(palavra):
    for index in posicaoCorreta:
        if palavra[index] != posicaoCorreta[index]:
            print(palavra[index])
            print(posicaoCorreta[index])
            print("false 1")
            return False

    # Chave letra, Conteudo quantidade de aparicoes
    letrasAtuais = dict()
    for letra in palavra:
        if letra not in letrasAtuais:
            letrasAtuais[letra] = 0
        letrasAtuais[letra] += 1

    for letra in letraCorreta:
        if letra in letrasAtuais:
            if letrasAtuais[letra] != letraCorreta[letra]:
                print("false 2")
                return False
        else:
            if letraCorreta[letra] == 0:
                continue
            if palavra == "terno":
                print(f"letraCorreta[letra]: {letraCorreta[letra]}")
                print(f"letra: {letra}")
                print(f"letrasAtuais[letra]: {letrasAtuais[letra]}")
                print("false 3")
            return False
    return True


while True:
    escolha = input("1 - AddPosCorreta 2 - AddLetraCorreta 3 - Testar - 4 Sair\n")
    if escolha == "1":
        index = int(input("Digite o index\n"))
        letra = input("Digite a letra\n")
        posicaoCorreta[index] = letra
    if escolha == "2":
        letra = input("Digite a letra\n")
        quantidade = int(input("Quantidade\n"))
        letraCorreta[letra] = quantidade
    if escolha == "3":
        for palavra in listaPalavras:
            if checarPalavra(palavra):
                possiveisPalavras.append(palavra)
        listaPalavras = possiveisPalavras.copy()
        possiveisPalavras.clear()
        print(f"Palavra possivel: {listaPalavras}")
    if escolha == "4":
        break

import random

def mensagem_de_abertura():
    print("*******************************************")
    print("****** Bem vindo ao jogo da forca *********")
    print("*******************************************")

def jogar():

    mensagem_de_abertura()

    arquivo = open("arquivo.txt","r")
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)


    arquivo.close()

    numero = random.randrange(0,len(palavra))
    palavra_escolhida = palavra[numero].lower()




    palavra_secreta = palavra_escolhida.lower()
    enforcou = False
    acertou = False
    letras_corretas = ["_" for letra in palavra_secreta]
    print(letras_corretas)
    erros = 0


    while(not enforcou and not acertou):
        chute = input("Digite uma letra : ")
        chute = chute.strip().lower()  # para remover os espaços

        if chute in palavra_secreta :
            index = 0
            for letra in palavra_secreta:
                if (chute.lower() == letra.lower()):  # para aceitar tanto letra minúscula quanto maiúscula #
                    letras_corretas[index] = letra
                index = index + 1
        else:
            erros = erros +1

        enforcou = erros == 6
        acertou = "_" not in letras_corretas
        print(letras_corretas)

    if (acertou):
        print("PARABÉNS!! VOCÊ ACERTOU")
    else:
        ("VOCÊ PERDEU!" )

    print("FIM DE JOGO")

if (__name__== "__main__"):
    jogar()

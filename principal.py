import forca
import adivinhacao

print("***************************************")
print("****** ESCOLHA O SEU JOGO *************")
print("***************************************")


print("escolha o jogo: 1 para forca e 2 para adivinhação ")
jogo_str = input("digite 1 ou 2 :")
jogo = int (jogo_str)

if jogo == 2:
    adivinhacao.jogar()
elif jogo == 1:
     forca.jogar()


import random

def jogar():

      print("*************************************************")
      print("************ Jogo da Adivinhação *****************")
      print("*************************************************")

      numero = random.randrange(1,101)
      tentativa = 0


      print("Escolha o nível do jogo : (1) Fácil, (2) Médio, (3) Dífícil ")
      nivel_str = input("Digite o número do nível : ")
      nivel = int(nivel_str)
      if nivel == 1:
         tentativa = 12
      elif nivel == 2:
         tentativa = 8
      elif nivel == 3:
         tentativa = 5
      else:
         print("Escolha 1, 2 ou 3 ")

      for rodada in range(1,tentativa+1):
         print("tentativa {} de {}".format(rodada, tentativa))
         chute_str = input("digite um número que esteja entre 1 e 100: ")
         chute = int(chute_str)
         if (chute < 1 or chute > 100):
            print("O número digitado não está entre 1 e 100")
            continue

         maior = chute >    numero
         menor = chute <    numero
         acertou = chute == numero

         if (maior):
            print("o número é muito alto")
         elif (menor):
            print("o número é muito baixo")
         else:
            print("Parabéns você acertou, o número é : {}".format(numero))
            break
      print("********** FIM DE JOGO **********")

if (__name__ == "__main__"):   #diferenciar o arquivo importado do executável
    jogar()
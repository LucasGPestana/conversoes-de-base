import os

def limpaTela():
    os.system('cls') or None

while True:
  
  limpaTela()
  
  print("1 - Binário para decimal")
  print("2 - Decimal para binário")

  conversao = int(input("Escolha o sistema de conversão: "))

  limpaTela()

  match conversao:
      case 1:
          multiplos = []
          numBin = []
          num = input("Digite um número binário: ")

          for bit in num:
              numBin.append(int(bit))
        
          numBin.reverse()

          for casa in range(len(numBin)):
              multiplos.append(numBin[casa] * 2 ** casa)

          numBin.reverse()
          
          numDec = sum(multiplos)

          print("A representação binária ", end="")
          for casa in range(len(numBin)):
                 print(numBin[casa], end="")
          print(f" corresponde a {numDec} em base decimal")

          break
      case 2:
          numBin = []

          numDec = int(input("Digite um número decimal: "))

          num = numDec

          while num != 0:
              
              if num % 2 == 0:
                  numBin.append(0)
              else:
                  numBin.append(1)
              
              num = num // 2

          numBin.reverse()

          print(f"A representação decimal {numDec} corresponde a ", end="")
          for casa in range(len(numBin)):
              print(f"{numBin[casa]}", end="")
          print(" em base binária")

          break
      case _:
          input("Valor inválido! Aperte a tecla \'enter\' para digitar novamente")
from time import sleep

print("Estou penando em um numero entre 0 e 5. Tente adivinhar qual numero estou pensando...")
sleep (2)
num = int(input("Digite um numero entre 0 e 5: "))

if (num==4):
    print("Processando...")
    sleep (1)
    print("Parabéns! Você acertou!")
else:
    print("Processando...")
    sleep (1)
    print("Poxa, você errou.")
nome = str(input("Informe o seu nome: "))
ano = int(input("Informe o ano que você nasceu: "))

idade = 2023 - ano

if (idade<18):
    saldo = 18 - idade
    print("{}, Ainda falta {} anos para você se alistar".format(nome,saldo))
    tempo = 2023 + saldo
    print("O ano do seu alistamento será em {}".format(tempo))

elif (idade==18):
    print("{}, já está na hora de você se alistar!".format(nome))

elif (idade>18):
    saldo = idade - 18
    print("{}, você deveria ter se alistado a {} anos".format(nome, saldo))
    tempo = 2023 - saldo
    print("O ano do seu alistamento foi {}".format(tempo))
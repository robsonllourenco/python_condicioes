nome = str(input("Informe seu nome: "))
nasc = int(input("Informe o ano do seu nascimento: "))

idade = 2023 - nasc

if idade<=9:
    print("{}, sua idade se encaixa na categoria MIRIN.".format(nome))
elif idade>9 and idade<=14:
    print("{}, sua idade se encaixa na categoria INFANTIL.".format(nome))
elif idade>14 and idade<=19:
    print("{}, sua idade se encaixa na categoria JUNIOR.".format(nome))
elif idade>19 and idade<=25:
    print("{}, sua idade se encaixa na categoria SÊNIOR.".format(nome))
else:
    print("{}, sua idade se encaixa na categoria MASTER.".format(nome))
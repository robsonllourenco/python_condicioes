salario = float(input("Informe o seu salario: R$ "))

aumento1 = salario + (salario * 10 / 100)
aumento2 = salario + (salario * 15 / 100)

if salario>1250:
    print("Você teve um aumento de 10%, sendo R$ {:.2f} seu novo salario".format(aumento1))

else:
    print("Você teve um aumento de 15%, sendo R$ {:.2f} seu novo salario".format(aumento2))
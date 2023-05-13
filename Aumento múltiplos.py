salario = float(input("Informe o valor do seu salário R$: "))

porcent1 = 10
cal1 = salario + (salario * 10 / 100)

porcent2 = 15
cal2 = salario + (salario * 15 / 100)

if salario > 1250:
    print("Você ganhou um aumento de 10%. Seu novo salário é R$: {:.2f}".format(cal1))
else:
    print("Você ganhou um aumento de 15%. Seu novo salário é R$: {:.2f}".format(cal2))
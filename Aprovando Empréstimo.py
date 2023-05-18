casa = float(input("Informe o valor da casa R$: "))
salario = float(input("Informe o valor do seu salário R$: "))
anos = int(input("Em quantos anos deseja financiar o imovel: "))

prestação = casa /(anos * 12)
minimo = salario * 30 / 100

print("Para pagar um imovel no valor de R$ {:.2f} em {} anos, a prestação será no valor de R$ {:.2f}".format(casa,anos,prestação))

if (prestação <= minimo):
    print("O financiamento foi APROVADO!")
else:
    print("O financiamento foi REPROVADO!")

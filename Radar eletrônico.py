radar = float(input("Informe a velocidade do carro: "))

multa = (radar-80) * 7

if (radar>80):
    print("VOCÊ ULTRAPASSOU A VELOCIDADE PERMITIDA")
    print("Você foi multado no valor de R$ {:.2f}!".format(multa))
else:
    print("Você está na velocidade permitida.")
radar = float(input("Informe a velocidade do carro: "))

multa = (radar-80) * 7

if radar>80:
    print("Você foi multado no valor de R$ {:.2f} por excesso de velocidade.".format(multa))

else:
    print("Você está na velocidade permitada.")
distancia = float(input("Informe a distancia em KM da sua viagem: "))

km1 = distancia * 0.50
km2 = distancia * 0.45

if(distancia<=200):
    print("O preço da passagem é R$ {:.2f}".format(km1))
else:
    print("O preço da passagem é R$ {:.2f}".format(km2))
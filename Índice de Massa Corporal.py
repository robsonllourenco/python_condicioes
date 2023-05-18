peso = float(input("Informe o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso / (altura ** 2)

print("Seu imc é de: {:.1f}".format(imc))

if imc <= 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc <=25:
    print("Você está no peso ideal")
elif imc >=25 and imc <=30:
    print("Você está com sobrepeso")
elif imc >= 30 and imc <= 40:
    print("Você estpa com Obesidade")
else:
    print("Você está com Obesidade mórbida")
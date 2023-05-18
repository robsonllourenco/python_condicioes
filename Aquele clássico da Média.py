num1 = float(input("Informe sua primeira nota: "))
num2 = float(input("Informe sua primeira nota: "))

media = (num1 + num2) / 2

if media<5.0:
    print("Infelizmente você REPROVOU.")
elif media>=7.0:
    print("Parabéns! Você foi APROVADO!")
elif media>5 and media<7:
    print("Infelizmente você está na RECUPERAÇÃO.")
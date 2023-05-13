num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

# Verificar número menor
menor = num1
if num2 < num1:
    menor = num2
if num3 < num2:
    menor = num3

# Verificar número maior
maior = num1
if num2 > num1:
    maior = num2
if num3 > num2:
    maior = num3

print("O número menor é {}".format(menor))
print("O número maior é {}".format(maior))
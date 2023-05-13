num = int(input("Digite um numero: "))

cal = num % 2

if(cal==0):
    print("O numero {} é PAR!".format(num))
else:
    print("O numero {} é ÍMPAR!".format(num))


#print("-----Bem vindo ao conversor decimal para binario-----")
#decimal=int(input("Digite o numero decimal a ser convertido: "))
#binario= bin(decimal)print("O Numero %d em Binário é: %s" %(decimal,binario[2:]) )

numero = ""
print("-----Bem Vindo ao conversor de Decimal para Hexadecimal-----")
digito=int(input("Digite o decimal a ser convertido: "))
valordeci = [10, 11, 12, 13, 14, 15 ]
valorhexa = ["a", "b", "c", "d", "e", "f"]

if digito <= 0:
    numero = "0"
else:
    while digito != 0:
        valorx = digito % 16
        digito = int(digito / 16)

        if valorx < 10:
            num = str(valorx)
        else:
            for i in range(7):
              if valorx == valordeci[i-1]:
                num = valorhexa[i-1]

        numero = num + numero

print("O valor decimal em hexadecimal é: ",numero)

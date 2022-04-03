#numero=int(input("Digite um numero: "))
#while numero<100:
    #print("\t " + str(numero))
   # numero= numero+1
#print("Laço encerrado")    

#nomes = ["Guilherme","Marcelo","João","Julia"]

#for i in nomes:
  #  print(i) 

#for numero in range(1,int(input("Digite o numero para determinar o fim: ")),1):
#    print("\t"+str(numero))

tabuada=int(input("Digite um numero para exibir a tabuada: "))
print("\tTabuada do número ", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))
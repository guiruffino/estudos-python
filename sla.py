s=float(input("Digite o valor do seu salario: "))

p=float(input("Digite o valor da prestação: "))

if p > 0.2 * s:
   print("emprestimo nao concedido")
else:
    print("emprestimo concedido")    
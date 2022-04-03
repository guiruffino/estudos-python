
resposta="SIM"  
while resposta=="SIM":
    nivel=input("Digite o nivel de acesso: ").upper()
    if nivel=="ADM" or nivel=="USR":
        genero=input("Digite o seu gênero: ").upper()
        if nivel=="ADM":
            if genero=="FEMININO":
                print("Olá Administradora")
            else:
                print("Olá Administrador") 
        else:
            if genero=="FEMININO":
                print("Olá usuária")
            else:
                print("Olá usuário")
    elif nivel=="GUEST":
        print("Olá Visitante")   
    else:
        print("\tUsuario não reconhecido ","\n\tOlá desconhecido")
    resposta=input("Digite SIM para continuar:  ").upper                     
            
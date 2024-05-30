print("*******CADASTRO DE CLIENTE*******")

while True:
    
    print("Escolha [1] - para [Cadastrar dados pessoais]:")
    print("Escolha [2] - para [Cadastrar endereço]:")
    print("Escolha [3] - para [Cadastrar dados profissionais]:")
    print("Escolha [0] - para [sair]:")
    print()
    
    menu = int(input("Escolha: "))
    print()

    if menu == 1:
        print("*********CADASTRO DE DADOS PESSOAIS:*********")
        nome = str(input("Digite seu nome: "))
        idade = int(input("Digite sua idade: "))
        cpf = int(input("Digite seu CPF: "))
        print()
        print(f"DADOS CADASTRADOS:")
        print(f"NOME: [{nome}]")
        print(f"IDADE: [{idade}]")
        print(f"CPF: [{cpf}]")
        print()
    
    if menu == 0:
        break


print()
print("----------------  FIM DO PROGRAMA!!!  ----------------")
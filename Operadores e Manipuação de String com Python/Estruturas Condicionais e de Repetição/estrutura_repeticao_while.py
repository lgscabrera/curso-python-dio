#Usado pra repetir um bloco de código n vezes
#Faz sentido usar o while quando não sabemos o número exato de vezes que o bloco deve ser executado

opcao = -1
while opcao != 0:
    opcao = int(input("Selecione uma opção: \n[1] Sacar \n[2] Extrato \n[0]Sair:  \n"))

    if opcao == 1:
        int(input("Digite o valor que deseja sacar: "))
    elif opcao == 2:
        print("Exibindo o extrato")
else:
    print("Obrigado por usar o sitema ")
    
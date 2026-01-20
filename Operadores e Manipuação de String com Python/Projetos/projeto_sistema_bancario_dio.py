"""
Deposito: 1 usuário, deposito valores positivos, depositos armazenados em uma variavel e exibido na operação de extrato
Saque: 3 saques diarios, limite de 500, se não tiver dinheiro o sistema exibi uma mensagem informando que não é possivel, deve ser exibido na operação de extrato
Extrato:Devew listar todos os depósitos e saques, no fim da listagem deve exibir o saldo da conta, os valores devem ser exibido utilizando R$
"""
menu = """
================Menu==================
Para realizar um deposito, digite: 1
Para realizar um saque, digite: 2
Para ver o extrato, digite: 3
Para sair, digite: 0
======================================
"""
saldo = 0.0
LIMITE_DE_SAQUE = 500.0
extrato = []
i = 0
SAQUES_DIARIOS = 3
j = 0
total_depositos = 0
total_saques = 0
x = 0



while True:
    escolha = input(menu)

    if escolha == "1":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo = saldo + valor
            extrato += [f"Deposito realizado no valor de: R$ {valor: .2f}"]
            print(f"Deposito no valor de R$ {valor: .2f} na sua conta")
            total_depositos = total_depositos + 1
            j = j + 1 
        
        else:
            print("Não foi possivel concluir a operação!")


    elif escolha == "2":

        valor = float(input(f"Essa é a {i+1}º de {SAQUES_DIARIOS} tentativa de saque do dia. Informe o valor do saque: "))

        maior_que_saldo = valor > saldo

        maior_que_limite = valor > LIMITE_DE_SAQUE

        muitos_saques = i >= SAQUES_DIARIOS


        if maior_que_saldo:
            print("Saldo Insuficiente!")
        elif maior_que_limite:
            print(f"Tentativa de saque maior que o limite de R${LIMITE_DE_SAQUE}")
        elif muitos_saques:
            print("Já realizou o maximo de saques permitidos!")
        elif valor > 0:
            saldo = saldo - valor
            extrato += [f"Saque realizado no valor de: R${valor: .2f}"]
            i = i + 1
            j = j + 1
            total_saques = total_saques + 1
            print(f"Saque no valor de: R$ {valor: .2f} na sua conta ")

        else:
            print("Falha!")


    elif escolha == "3":
        print("================================Extrato================================")
        if j > 0:
            for x in extrato:
                print(x)
        else:
            print("Não foram realizadas movimentações.")
        print(f"Saldo atual: R${saldo: .2f}")
        print(f"Foi realizado um total de {total_depositos} depositos na sua conta!")
        print(f"Foi realizado um total de {total_saques} saques na sua conta!")
        print("=======================================================================")

    elif escolha == "0":
        print("Obrigado por usar nosso sistema!")
        break
    else:
        print("Escolha uma das opções")
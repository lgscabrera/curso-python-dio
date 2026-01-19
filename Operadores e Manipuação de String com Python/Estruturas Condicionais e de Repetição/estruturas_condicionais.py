#Permitem o desvio de fluxo de controle quando determinadas expressões lógicas são atendidas.
#if - else - elif
#if, estrutura condicional simples, testa a expressão lógica, e em caso verdadeiro as ações do bloco if são executadas.

"""saldo = 2000.0
saque = float(input("Informe o valor do saque: "))
if saldo >= saque:
    print("Saque realizado")
if saldo < saque:
    print("Saldo Insuficiente")

saldo -= saque
print(f"Está guardado o valor de: {saldo}")

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))
if opcao == 1:
    valor = float(input("Informe a Quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato... ")

else:
    sys.exit("Opção Inválida")"""

"""MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

##Apenas IF

if idade >= MAIOR_IDADE:
    print("Maior de Idade!")

if idade < MAIOR_IDADE:
    print("Menor de Idade!")

#Com IF e ElSE

if idade >= MAIOR_IDADE:
    print("Maior de Idade!")

else:
    print("Menor de Idade!")

#Com IF, ELSE e ELIF

if idade >= MAIOR_IDADE:
    print("Maior de Idade")

elif idade == IDADE_ESPECIAL:
    print("Quase lá!")

else:
    print("Menor de Idade!")"""


#IF ANINHADO
#Adicionar estruturas IF/ELIF/ELSE dentro de blocos de IF/ELIF/ELSE
"""conta_universitaria= False
conta_normal = False
saldo = 2000
saque = 2500
cheque_especial = 450
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque < (saldo + cheque_especial):
        print("Saque realizado no cheque especial!")
    else:
        print("Saldo Insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado com sucesso!")
    else:
        print("Saldo Insuficiente")
else:
    print("Sistema não reconheceu o tipo de conta!")
"""

#IF ternário
#Permite escrever uma condição em uma única linha.
#Composto por 3 partes.
#1º retorno caso a expressão retorne verdadeiro.
#2º expressão lógica.
#3 retorno caso a expressão não seja atendida.

saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")


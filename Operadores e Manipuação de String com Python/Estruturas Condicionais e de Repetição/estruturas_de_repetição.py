#Utilizadas para repetir um certo bloco do código n vezes
#Exemplo

#Receba um número do teclado e exiba os 2 números seguintes
#sem estrutura de repetição
a = int(input("Informe um número: "))

a += 1
print(a)

a += 1
print(a)

#Com estrutura de repetição
a = int(input("Informe um número inteiro: "))
print(a)

"""repita 2 vezes:
    a += 1
    print(a)"""


#comando FOR
#texto = input("Informe um texto: ")
texto = " "
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print("Executa no final do laço") 

#RANGE
#Produzir uma sequência de números inteiros a partir de um indice
# i, i+1, i+2, i+n
#Recebe 3 argumentos stop(obrigatório), start(opcional) e step(opicional)
#start (Onde começa!)
#Stop (Onde termina!)
#step (vai de x em x pulando números)
for numero in range(0, 11):
    print(numero, end=" ")

print()

for numero in range(0, 51, 5):
    print(numero, end=" ")
    

#Brek e Continue
#while com break
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)
#for com break
for numero in range(100):
    if numero == 10:
        break

    print(numero, end=" ")


#for com Continue
for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")

#While com continue e break
while True:
    numero = int(input("Informe um número: "))
    if numero == 10:
        break
    if numero % 2 == 0:
        continue

    print(numero)

#While
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
    
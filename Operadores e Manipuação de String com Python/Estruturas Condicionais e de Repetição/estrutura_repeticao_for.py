#comando FOR
#Faz sentido usar o for quando sabemos o número exato de vezes que o bloco deve ser executado
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
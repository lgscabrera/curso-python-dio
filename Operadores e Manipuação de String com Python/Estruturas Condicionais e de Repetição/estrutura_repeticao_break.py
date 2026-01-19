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
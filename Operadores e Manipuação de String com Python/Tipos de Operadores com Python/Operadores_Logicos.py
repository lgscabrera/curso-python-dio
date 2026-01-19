##################### Operadores Lógicos #####################
#Retorna Booleano
saldo = 1000
saque = 200
limite = 100

saldo >= saque

saque <= limite

#Operador E, para retornar true, exige que todas as partes sejam verdadeiras, e para retornar false, apenas uma precisam ser falsas
saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite

#Operador OR, para retornar true, apenas uma das partes precisa ser verdade, e para retornar false, todas precisam ser falsas
saldo = 1000
saque = 200
limite = 100
saldo >= saque or saque <= limite

#Operador de Negação ( not ), sempre o contrario do que seria o correto
not 100 > 1500
#saida true

#Parênteses para precedencia
saldo = 1000
saque = 200
limite = 100
saldo >= saque and saque <= limite or saldo == saque
print((saldo >= saque and saque <= limite) or (saldo == saque))

#Exemplo
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
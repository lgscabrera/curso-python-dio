#Comparar se os objetos ocupam a mesma posição na memória
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200
curso is nome_curso
#saida True

curso is not nome_curso
#Saida False

saldo is limite
#Saida True

#exemplo
saldo = 1000
limite = 1000

print(saldo is limite)
print(saldo is not limite)
nome = "Luiz Gabriel da Silva Cabrera"

#[ x : y : z]
#x = inicio
#y = fim
#z = passo a passo

#truques
#pegar a ultima letra [-1] e assim vai, indo de trás pra frente

#pega o caractere na posição escolhida
print(nome[0])
#saida: L

#pega os caracteres ATÉ a posição escolhida
print(nome[:9])
#saida: Luiz Gabr

#pega os caracteres APÓS a posição escolhida
print(nome[9:])
#saida: iel da Silva Cabrera

#Pega os caracteres ENTRE as posições escolhidas
print(nome[5:15])
#saida: Gabriel da

#Step: vai de x em x entre os caracteres escolhidos
print(nome[10:16:2])

#Escreve tudo
print(nome[ : ])
#saida: Luiz Gabriel da Silva Cabrera

#espelha os caracteres
print(nome[:: -1])
#Saida: arerbaC avliS ad leirbaG ziuL
#Maiúscula, minúscula e título
curso = "pYtHon"

#coloca todos os caracteres em maiúsculo
print(curso.upper())

#coloca todos os caracteres em minúsculo
print(curso.lower())

#coloca o primeiro caracter em maiúsculo e o resto em minúsculo
print(curso.title())

#Eliminando espaços em branco.
curso = "           Python "
#Remove os espaço em branco da esquerda e da direita
print(curso.strip())
#Remove o espaço em branco da esquerda, left strip
print(curso.lstrip())
#Remove o espaço em branco da direita, right strip
print(curso.rstrip())

#Junção e centralização
curso = "Python"

#adiciona caracteres até ter x caracteres
print(curso.center(10, "#"))

#Cada vez que passar por um item, ele coloca o caractere escolhido
print(".".join(curso))
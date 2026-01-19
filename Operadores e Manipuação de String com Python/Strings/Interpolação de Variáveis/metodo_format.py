nome = "Luiz Gabriel"
idade = 28
profissao = "Estudante"
linguagem = "Python"

print("Olá, me chamo {}. Tenho {} anos de idade, sou {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Tenho {2} anos de idade, sou {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
print("Olá, me chamo {nome}. Tenho {idade} anos de idade, sou {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, profissao=profissao, linguagem=linguagem, idade=idade))
print("Olá, me chamo {nome}. Tenho {idade} anos de idade, sou {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))


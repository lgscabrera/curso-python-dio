nome = "Luiz Gabriel"
idade = 28
profissao = "Estudante"
linguagem = "Python"

dados = {"nome": "Luiz Gabriel", "idade": 20}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}" .format(nome, idade))
print("Nome: {0} Idade: {1}" .format(nome, idade))
print("Nome: {0} Idade: {1} Nome: {0}" .format(nome, idade))
print("Nome: {nome} Idade: {idade} Nome: {nome}" .format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"Nome: {nome} Idade: {idade} Nome: {nome}")
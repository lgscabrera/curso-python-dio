#São definidas informando 3 aspas simples, ou duplas durante a atribuição. Podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.
nome = "Luiz Gabriel da Silva Cabrera"

#Aspas Duplas
mensagem = f"""
Olá, meu nome é {nome},
Eu estou aprendendo Python
    Essa mensagem tem diferentes recuos.
"""
print(mensagem)

#Aspas Simples
mensagem = f'''
Olá, meu nome é {nome},
Eu estou aprendendo Python
    Essa mensagem tem diferentes recuos.
'''
print(mensagem)

#Ambos os tipos de aspas tem o mesmo comportamento


print("""
====================MENU====================
1 - Depositar
2 - Sacar
0 - Sair
                        Obrigado por usar nosso sistema!


""")
menu = "====================MENU===================="
menu += "\n"
menu += "1 - Depositar"
menu += "\n"
menu += "2 - Sacar"
menu += "\n"
menu += "0 - Sair"
menu += "\n"
menu += "                                     Obrigado por usar nosso sistema!"

print(menu)
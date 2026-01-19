#Como o interpretador Python utiliza a identação docódigo para delimitar os blocos de comandos.
############ Identação e Blocos de Comando ############
#Identação do Código, o interpretador determina onde um bloco de comando começa e onde termina.
#Aumenta a legibilidade e manutenibilidade do código
#Em python a Identação é feita não só para estética, mas também para funcionalidade

#Bloco de Comando (Função) em python (def)

def pegar(self, valor: float) -> None:
    if self.saldo >= valor:
        self.saldo-= valor
    


def sacar(valor: float):
    saldo = 500.0

    if saldo >= valor:
        print("Valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    else:
        print("Você não tem esse dinheiro, pobre!")
    print("Obrigado por ser nosso cliente.")



def depositar(valor):
    saldo = 500
    saldo += valor


sacar(1000)

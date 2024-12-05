class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0
        self.limite_saque_diario = 3
        self.valor_limite_saque = 500.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito realizado: R$ {valor:.2f}")
        else:
            print("Depósito não pode ser negativo!")

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saque_diario:
            print("Limite diário de saques atingido!")
        elif valor > self.valor_limite_saque:
            print(f"Saque não pode exceder R$ {self.valor_limite_saque:.2f} por operação!")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_realizados += 1
            print(f"Saque realizado: R$ {valor:.2f}")

    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def mostrar_extrato(self):
        print("=== Extrato ===")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("================")

# Função principal para interação com o usuário
def menu():
    banco = Banco()

    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar Saldo")
        print("4. Mostrar Extrato")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            banco.depositar(valor)
        
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            banco.sacar(valor)
        
        elif opcao == "3":
            banco.mostrar_saldo()
        
        elif opcao == "4":
            banco.mostrar_extrato()

        elif opcao == "5":
            print("Saindo do sistema. Obrigado!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Execução do menu interativo
menu()

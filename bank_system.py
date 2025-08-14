saldo = 0
limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

def formatar_valor(valor):
    return f"R$ {valor:.2f}"

while True:
    print("\n### Menu ###")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")
    opcao = input("Escolha uma opção: ").lower()

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: {formatar_valor(valor)}")
            print(f"Depósito de {formatar_valor(valor)} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 's':
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque: {formatar_valor(valor)}")
            numero_saques += 1
            print(f"Saque de {formatar_valor(valor)} realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 'e':
        print("\n### EXTRATO ###")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimentacao in extrato:
                print(movimentacao)
        print(f"\nSaldo atual: {formatar_valor(saldo)}")

    elif opcao == 'q':
        print("Saindo do sistema. Obrigado por usar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



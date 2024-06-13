print("Olá, bem vindo ao nosso Banco.")

item = -1
saldo = 0.0
extrato = ""
limite_saque = 3


# while item != 0:
#     item = int(input("Selecione a ação que deseja. 1 - Depositar\n2 - Sacar\n3 - Extrato\n0 - Sair\n"))
    
while item != 0:
    item = int(input("""
                     Selecione a ação que deseja. 
                     1 - Depositar
                     2 - Sacar
                     3 - Extrato
                     0 - Sair\n"""
                     ))
    if item == 1:
        
        valor_deposito = float(input("Quanto deseja Depositar ? "))
        if valor_deposito < 0:
            print(Exception("Valor inválido"))
        else:
            saldo += valor_deposito;
            extrato += str(f"""   Valor Depositado: R$ {valor_deposito:.2f} novo saldo: R$ {saldo:.2f}\n""")
        
    elif item == 2:
      
        if limite_saque <= 0:
            print("Saques diários esgotados. Volte amanhã")
        else:
            valor_saque = float(input("Quanto deseja Sacar ? "))
            if valor_saque < 0:
                print(Exception("Valor inválido"))
            elif valor_saque > 500:
                print("Valor limite atingido ! ")
            elif valor_saque > saldo:
                print("Saldo insuficiente ! ")
            else:
                saldo -= valor_saque;
                extrato += str(f"""   Valor de Saque: R$ {valor_saque:.2f} novo saldo: R$ {saldo:.2f}\n""")
                limite_saque -= 1 
        
    elif item == 3:
        print("        ============= EXTRATO =============\n")
        print(extrato)
    elif item == 0:
        print("Obrigado por usar nosso banco")
    else:
        print("Opção inválida")
        
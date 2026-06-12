def menu(df):

    while True:

        print("\n=== MENU ===")
        print("1 - Saldo pendente")
        print("2 - Clientes em atraso")
        print("3 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":

            saldo = df["Saldo_Aberto"].sum()

            print(f"\nSaldo total: R$ {saldo:,.2f}")

        elif opcao == "2":

            atrasados = df[df["Situacao"] == "Atrasada"]

            print(atrasados)

        elif opcao == "3":

            break
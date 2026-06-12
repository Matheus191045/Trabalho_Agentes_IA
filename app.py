import pandas as pd
from menu import menu

arquivo = "BaseFinanceiroAnalise.xlsx"

df = pd.read_excel(arquivo)

menu(df)

print("=" * 50)
print("ANÁLISE FINANCEIRA")
print("=" * 50)

print(f"\nQuantidade de registros: {len(df)}")

saldo_total = df["Saldo_Aberto"].sum()

print(f"\nSaldo pendente total: R$ {saldo_total:,.2f}")

print("\nSituações:")

print(df["Situacao"].value_counts())
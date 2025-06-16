
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Saúde Financeira - Matheus", layout="wide")

# Receita fixa mensal
receita_mensal = 17000.00

# Dados fixos de despesas
data = {
    "Despesa": [
        "Carro", "Aluguel", "Cartão Infinite", "Simples Nacional",
        "Master Inter", "Consórcio (Auto)", "Consórcio (Imóvel)",
        "Cruzeiro", "Contador", "Cartão Porto", "Claro",
        "Riachuelo", "Casas Bahia", "Brisa Net"
    ],
    "Valor (R$)": [
        2300.00, 1600.00, 1500.00, 1200.00, 1428.38, 850.00,
        641.40, 315.00, 250.00, 230.18, 152.14, 149.74,
        294.39, 89.99
    ],
    "Categoria": [
        "Transporte", "Moradia", "Cartão de Crédito", "Tributário",
        "Cartão de Crédito", "Investimento", "Investimento",
        "Lazer", "Serviço", "Cartão de Crédito", "Serviço",
        "Cartão de Crédito", "Cartão de Crédito", "Serviço"
    ]
}

df = pd.DataFrame(data)
df = df.sort_values(by="Valor (R$)", ascending=False)
df["% da Receita"] = (df["Valor (R$)"] / receita_mensal * 100).round(2)

st.title("📊 Saúde Financeira de Matheus")
st.markdown("Este painel apresenta um resumo interativo das suas despesas mensais com base na sua receita de R$ 17.000,00.")

col1, col2, col3 = st.columns(3)
col1.metric("💰 Receita Mensal", f"R$ {receita_mensal:,.2f}")
col2.metric("💸 Total de Despesas", f"R$ {df['Valor (R$)'].sum():,.2f}")
col3.metric("📈 Saldo Disponível", f"R$ {receita_mensal - df['Valor (R$)'].sum():,.2f}")

st.subheader("📂 Tabela de Despesas")
st.dataframe(df, use_container_width=True)

st.subheader("📉 Gráfico de Despesas por Categoria")
fig = px.pie(df, names="Categoria", values="Valor (R$)", title="Distribuição por Categoria")
st.plotly_chart(fig, use_container_width=True)

st.subheader("📊 Gráfico de Barras - Valor por Despesa")
fig_bar = px.bar(df, x="Valor (R$)", y="Despesa", orientation="h", color="Categoria", title="Despesas por Item")
st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")
st.markdown("Aplicativo desenvolvido por **ChatGPT** para uso exclusivo de Matheus.")

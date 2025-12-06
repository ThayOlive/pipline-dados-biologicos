import streamlit as st
import json
import matplotlib.pyplot as plt
import pandas as pd

# ======================
# CONFIGURAÇÃO DA PÁGINA
# ======================
st.set_page_config(
    page_title="Pipeline Biológico",
    page_icon="🧬",
    layout="wide"
)

# ======================
# TÍTULO
# ======================
st.title("🧬 Pipeline de Dados Biológicos")
st.write("Dashboard de visualização de sequências de DNA")

# ======================
# LEITURA DOS DADOS
# ======================
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO = os.path.join(BASE_DIR, "data", "processed", "resultados.json")

with open(CAMINHO, "r") as file:
    dados = json.load(file)
# ======================
# ORGANIZAÇÃO DOS DADOS
# ======================
ids = [d["id"][:40] for d in dados]
tamanhos = [d["tamanho"] for d in dados]
gc = [d["Porcentagem de GC"] for d in dados]
nomes = [d["Nome da Espécie"] for d in dados]

# limitar para evitar poluição visual
limite = 1000
ids = ids[:limite]
tamanhos = tamanhos[:limite]
gc = gc[:limite]
nomes = nomes[:limite]

df = pd.DataFrame({
    "Espécie": nomes,
    "Sequência": ids,
    "Tamanho": tamanhos,
    "GC (%)": gc
})

# ======================
# FILTROS NA SIDEBAR
# ======================
st.sidebar.header("🔎 Filtros")

tamanho_min = st.sidebar.slider(
    "Tamanho mínimo",
    min_value=min(tamanhos),
    max_value=max(tamanhos),
    value=min(tamanhos)
)

df_filtrado = df[df["Tamanho"] >= tamanho_min]

# ======================
# TABELA
# ======================
st.subheader("📋 Tabela das Sequências")
st.dataframe(df_filtrado, use_container_width=True)

# ======================
# GRÁFICO DE BARRAS
# ======================
st.subheader("📊 Tamanho das Sequências")
st.bar_chart(df_filtrado.set_index("Espécie")["Tamanho"])

# ======================
# GRÁFICO DE LINHA (GC%)
# ======================
st.subheader("📈 Porcentagem de GC")
fig, ax = plt.subplots()
ax.plot(df_filtrado["Espécie"], df_filtrado["GC (%)"], marker="o")
plt.xticks(rotation=45)
st.pyplot(fig)

import streamlit as st
import pandas as pd
from algoritmo import agrupar_turmas

st.set_page_config(
    page_title="Planejamento de Turmas | Senac PR",
    layout="wide"
)

# Carregar CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📊 Planejamento Inteligente de Turmas")
st.caption("Padrão Senac PR")

df = pd.read_excel("data/base.xlsx")

meta = st.sidebar.slider(
    "Meta de alunos por turma",
    min_value=30,
    max_value=60,
    value=45
)

resultado = agrupar_turmas(df, meta)
df_resultado = pd.DataFrame(resultado)

st.dataframe(df_resultado, use_container_width=True)

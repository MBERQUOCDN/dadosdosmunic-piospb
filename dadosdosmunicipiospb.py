import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar os dados
@st.cache_data
def load_data():
    # Substitua o caminho abaixo pelo caminho completo do arquivo CSV em seu sistema
    data = pd.read_csv(r'C:\Users\BERQUÓ\OneDrive\Documentos\Área de Trabalho\Tecnicas\dadosdosmunicípiospb.csv')  
    data['Indice_Receita'] = data['Indice_Receita'].str.rstrip('%').astype(float)  # Remove o símbolo % e converte para float
    return data

# Função para exibir o ranking dos municípios
def show_ranking(data, order='decrescente'):
    if order == 'crescente':
        data = data.sort_values(by='Indice_Receita', ascending=True)
    else:
        data = data.sort_values(by='Indice_Receita', ascending=False)
    
    st.write("### Ranking dos Municípios por Índice de Receita")
    st.write(data[['Ranking', 'Município', 'Indice_Receita', 'Receita_Selecionada', 'Receita_Total']])

    # Exibir gráfico de barras
    st.write("### Gráfico de Barras - Índice de Receita dos Municípios")
    fig, ax = plt.subplots()
    ax.barh(data['Município'], data['Indice_Receita'], color='skyblue')
    ax.set_xlabel('Índice de Receita (%)')
    ax.set_ylabel('Município')
    ax.invert_yaxis()  # Inverte para o maior ficar no topo
    st.pyplot(fig)

# Função principal para o app Streamlit
def main():
    st.title("Análise de Arrecadação Própria dos Municípios")
    
    # Carregar dados
    data = load_data()
    
    # Opções de ordenação
    order_option = st.selectbox("Ordenar por:", ['decrescente', 'crescente'])
    
    # Filtro por município
    municipio_selecionado = st.selectbox("Selecione um município para visualizar:", ['Todos'] + list(data['Município']))
    
    # Filtrar dados
    if municipio_selecionado != 'Todos':
        data = data[data['Município'] == municipio_selecionado]

    # Exibir ranking e gráfico
    show_ranking(data, order=order_option)

if __name__ == "__main__":
    main()

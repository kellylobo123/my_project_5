import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma')
fig1 = px.histogram(car_data, x="type") # criar um histograma
fig1.show() # exibindo


if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="type")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar Gráfico de dispersão')

if scatter_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.scatter(car_data, x="type", y="price")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(car_data, x="type", y="price") # criar um gráfico de dispersão
fig.show()

import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd

def gerar_grafico_barras():
    data = pd.read_csv('Data.csv')
    dados_agrupados = data.groupby('Year')['On Target Per Avg Match'].mean()
    plt.bar(dados_agrupados.index, dados_agrupados.values)
    plt.xlabel('Ano')
    plt.ylabel('Média de Acertos no Alvo')
    plt.title('Gráfico de Barras')
    plt.show()

def gerar_grafico_linhas():
    data = pd.read_csv('Data.csv')
    dados_agrupados = data.groupby('Year')['On Target Per Avg Match'].mean()
    plt.plot(dados_agrupados.index, dados_agrupados.values, marker='o')
    plt.xlabel('Ano')
    plt.ylabel('Média de Acertos no Alvo')
    plt.title('Gráfico de Linhas')
    plt.show()

def gerar_grafico_pizza():
    data = pd.read_csv('Data.csv')
    dados_agrupados = data.groupby('Year')['On Target Per Avg Match'].sum()
    plt.pie(dados_agrupados, labels=dados_agrupados.index, autopct='%1.1f%%', startangle=90)
    plt.title('Gráfico de Pizza')
    plt.show()

def criar_interface_graficos():
    janela = tk.Tk()
    janela.title('Gráficos')
    btn_grafico_barras = tk.Button(janela, text='Gráfico de Barras', command=gerar_grafico_barras)
    btn_grafico_barras.pack()
    btn_grafico_linhas = tk.Button(janela, text='Gráfico de Linhas', command=gerar_grafico_linhas)
    btn_grafico_linhas.pack()
    btn_grafico_pizza = tk.Button(janela, text='Gráfico de Pizza', command=gerar_grafico_pizza)
    btn_grafico_pizza.pack()
    janela.mainloop()

criar_interface_graficos()

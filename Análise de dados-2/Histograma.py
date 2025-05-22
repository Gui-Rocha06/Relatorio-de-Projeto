# (1) Carregamento de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada de dados
arquivo = "lista_dados.CSV"
dados_org = pd.read_csv(arquivo, header=1, delimiter=";")
dados = dados_org.to_dict('list')
ids = np.array(dados['ID da amostra'])

# (3) Processamento de dados

# ID para comparação
ids_comparacao = [428, 429, 430, 431]
mascara_comparacao = np.isin(ids, ids_comparacao)

# Separando dados de resistência
resistencia_comparacao = np.array(dados['Resistencia (kgf)'])[mascara_comparacao]
resistencia_restante = np.array(dados['Resistencia (kgf)'])[~mascara_comparacao]

plt.figure(figsize=(16, 12))
plt.suptitle("Histogramas das Variáveis", fontsize=16)

# Histograma de Diâmetro
plt.subplot(3, 2, 1)
dados_diametro = np.array(dados["Diametro (mm)"])
N_diametro = len(dados_diametro)
K_diametro = int(np.round(1.0 + 3.32 * np.log10(N_diametro)))
plt.hist(dados_diametro, K_diametro, edgecolor='black', color='red')
plt.title("Histograma de Diametro (mm)")
plt.xlabel("Diametro (mm)")
plt.ylabel("Frequência")

# Histograma de Altura
plt.subplot(3, 2, 2)
dados_altura = np.array(dados["Altura (mm)"])
N_altura = len(dados_altura)
K_altura = int(np.round(1.0 + 3.32 * np.log10(N_altura)))
plt.hist(dados_altura, K_altura, edgecolor='black', color='blue')
plt.title("Histograma de Altura (mm)")
plt.xlabel("Altura (mm)")
plt.ylabel("Frequência")

# Histograma de Massa
plt.subplot(3, 2, 3)
dados_massa = np.array(dados["Massa (g)"])
N_massa = len(dados_massa)
K_massa = int(np.round(1.0 + 3.32 * np.log10(N_massa)))
plt.hist(dados_massa, K_massa, edgecolor='black', color='green')
plt.title("Histograma de Massa (g)")
plt.xlabel("Massa (g)")
plt.ylabel("Frequência")

# Histograma de Resistencia (TODOS)
plt.subplot(3, 2, 4)
N_resistencia_todos = len(np.array(dados["Resistencia (kgf)"]))
K_resistencia_todos = int(np.round(1.0 + 3.32 * np.log10(N_resistencia_todos)))
plt.hist(np.array(dados["Resistencia (kgf)"]), K_resistencia_todos, edgecolor='black', color='purple')
plt.title("Histograma de Resistencia TODOS (kgf)")
plt.xlabel("Resistencia (kgf)")
plt.ylabel("Frequência")

# Histograma de Resistencia (IDs 428-431)
plt.subplot(3, 2, 5)
N_resistencia_comparacao = len(resistencia_comparacao)
K_resistencia_comparacao = int(np.round(1.0 + 3.32 * np.log10(N_resistencia_comparacao)))
plt.hist(resistencia_comparacao, K_resistencia_comparacao, edgecolor='black', color='orange')
plt.title("Histograma de Resistencia IDs 428-431 (kgf)")
plt.xlabel("Resistencia (kgf)")
plt.ylabel("Frequência")

# Histograma de Resistencia (RESTANTE)
plt.subplot(3, 2, 6)
N_resistencia_restante = len(resistencia_restante)
K_resistencia_restante = int(np.round(1.0 + 3.32 * np.log10(N_resistencia_restante)))
plt.hist(resistencia_restante, K_resistencia_restante, edgecolor='black', color='brown')
plt.title("Histograma de Resistencia RESTANTE (kgf)")
plt.xlabel("Resistencia (kgf)")
plt.ylabel("Frequência")

# (4) Visualização de dados
plt.tight_layout(rect=[0, 0, 1, 1]) # Ajusta layout para evitar sobreposição entre eles
plt.show()
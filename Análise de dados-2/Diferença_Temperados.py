# (1) Carregamento de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada de dados
arquivo = "lista_dados.CSV"
dados_org = pd.read_csv(arquivo, header=1, delimiter=";")
dados = dados_org.to_dict('list')
ids = np.array(dados['ID da amostra'])

# (3) tratamento de dados

# ID para comparação
ids_comparacao = [428, 429, 430, 431]
mascara_comparacao = np.isin(ids, ids_comparacao)

# Separando dados
resistencia_comparacao = np.array(dados['Resistencia (kgf)'])[mascara_comparacao] #Incluindo os temperados
resistencia_restante = np.array(dados['Resistencia (kgf)'])[~mascara_comparacao] #Excluinso o resto usando ~

diametro_comparacao = np.array(dados['Diametro (mm)'])[mascara_comparacao]#processo se repete
diametro_restante = np.array(dados['Diametro (mm)'])[~mascara_comparacao]

# Calcular a tensão de ruptura para o grupo temperado F / R
raio_comparacao = diametro_comparacao / 2
area_secao_comparacao = np.pi * (raio_comparacao ** 2) # np.pi multiplica o resto
tensao_ruptura_comparacao = np.where(area_secao_comparacao != 0, resistencia_comparacao / area_secao_comparacao, np.nan) # evitando a divisao por 0 e se for zero é sinalizado como np.nan para o boolean
tensao_ruptura_comparacao = tensao_ruptura_comparacao[~np.isnan(tensao_ruptura_comparacao)]

# Calcular tensão de ruptura para o resto
raio_restante = diametro_restante / 2
area_secao_restante = np.pi * (raio_restante ** 2)
tensao_ruptura_restante = np.where(area_secao_restante != 0, resistencia_restante / area_secao_restante, np.nan)
tensao_ruptura_restante = tensao_ruptura_restante[~np.isnan(tensao_ruptura_restante)]

# Mostrar os valores no terminal para visualizar valores mais exatos
print("Resistência (kgf)")
print("Valores do grupo IDs 428-431:", resistencia_comparacao)
print("Valores do restante da tabela:", resistencia_restante)

print("\nTensão de Ruptura (kgf/mm²)")
print("Valores do grupo IDs 428-431:", tensao_ruptura_comparacao)
print("Valores do restante da tabela:", tensao_ruptura_restante)

# Função para remover outliers usando o metodo IQR
def remove_outliers_iqr(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data >= lower_bound) & (data <= upper_bound)]

# Remover outliers da resistência restante
resistencia_restante_sem_outliers = remove_outliers_iqr(resistencia_restante)

# Remover outliers da tensão de ruptura restante
tensao_ruptura_restante_sem_outliers = remove_outliers_iqr(tensao_ruptura_restante)

# Criar um único plot com todos os boxplots
plt.figure(figsize=(18, 10))
plt.suptitle('Comparação da Resistência e Tensão de Ruptura', fontsize=16)

# Boxplot da Resistência (com outliers)
plt.subplot(2, 2, 1)
plt.boxplot([resistencia_restante, resistencia_comparacao],
labels=['Restante (com outliers)', 'IDs 428-431'])
plt.title('Resistência (kgf)')
plt.ylabel('Resistencia (kgf)')
plt.grid(True)

# Boxplot da Tensão de Ruptura (com outliers)
plt.subplot(2, 2, 2)
plt.boxplot([tensao_ruptura_restante, tensao_ruptura_comparacao],
labels=['Restante (com outliers)', 'IDs 428-431'])
plt.title('Tensão de Ruptura (kgf/mm²)')
plt.ylabel('Tensão de Ruptura (kgf/mm²)')
plt.grid(True)

# Boxplot da Resistência (sem outliers)
plt.subplot(2, 2, 3)
plt.boxplot([resistencia_restante_sem_outliers, resistencia_comparacao],
labels=['Restante (sem outliers)', 'IDs 428-431'])
plt.title('Resistência (kgf) - Sem Outliers')
plt.ylabel('Resistencia (kgf)')
plt.grid(True)

# Boxplot da Tensão de Ruptura (sem outliers)
plt.subplot(2, 2, 4)
plt.boxplot([tensao_ruptura_restante_sem_outliers, tensao_ruptura_comparacao],
labels=['Restante (sem outliers)', 'IDs 428-431'])
plt.title('Tensão de Ruptura (kgf/mm²) - Sem Outliers')
plt.ylabel('Tensão de Ruptura (kgf/mm²)')
plt.grid(True)

plt.show()
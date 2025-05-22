# (1) Carregamento de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada de dados
arquivo = "lista_dados.CSV"
dados_org = pd.read_csv(arquivo, header=1, delimiter=";")
dados = dados_org.to_dict('list')

# Converter colunas para facilitar o processo
diametro = np.array(dados['Diametro (mm)'])
altura = np.array(dados['Altura (mm)'])
massa = np.array(dados['Massa (g)'])
resistencia = np.array(dados['Resistencia (kgf)'])

# (3) Processamento de dados

# Calcular densidade usando broadcasting e np.where para lidar com possíveis divisões por zero
volume = np.pi * (diametro / 2) ** 2 * altura
densidade = np.where(volume != 0, massa / volume, np.nan)
dados['densidade (g/mm^3)'] = densidade.tolist()  # Atribui ao dicionário 'dados'

# Calcular tensão de ruptura usando broadcasting e np.where para lidar com possíveis divisões por zero
area_secao = np.pi * (diametro / 2) ** 2
tensao_ruptura = np.where(area_secao != 0, resistencia / area_secao, np.nan)
dados['tensao de ruptura (kgf/mm^2)'] = tensao_ruptura.tolist() # Atribui ao dicionário 'dados'

# (4) Visualização de dados
plt.figure(figsize=(16, 12))
plt.suptitle("Gráficos de dispersão", fontsize=16)

plt.subplot(2, 2, 1)
plt.scatter( dados["densidade (g/mm^3)"], dados["tensao de ruptura (kgf/mm^2)"], s=20, c='b', marker='o') # S = Tamanho da marcação / C = Cor / Marker = Formato da marcação
plt.title("Tensão de Ruptura (kgf/mm²) x Densidade (g/mm³)")
plt.xlabel("Densidade (g/mm³)")
plt.ylabel("Tensão de Ruptura (kgf/mm²)")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.scatter( dados["Altura (mm)"], dados["Resistencia (kgf)"], s=20, c='r', marker='o')
plt.title("Resistencia (kgf) x Altura (mm)  ")
plt.xlabel("Altura (mm)")
plt.ylabel("Resistencia (kgf)")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.scatter(dados["Diametro (mm)"], dados["Resistencia (kgf)"],  s=20, c='r', marker='o')
plt.title("Resistencia (kgf) x Diametro (mm)")
plt.xlabel("Diametro (mm)")
plt.ylabel("Resistencia (kgf)")
plt.grid(True)

x = dados['Diametro (mm)']
y = dados['Resistencia (kgf)']
plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r")

plt.subplot(2, 2, 4)
plt.scatter(dados["Massa (g)"], dados["Resistencia (kgf)"],  s=20, c='b', marker='o')
plt.title("Resistencia (kgf) x Massa (g)")
plt.xlabel("Massa (g)")
plt.ylabel("Resistencia (kgf)")
plt.grid(True)

x = dados['Massa (g)']
y = dados['Resistencia (kgf)']
plt.scatter(x, y)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r")

plt.show()

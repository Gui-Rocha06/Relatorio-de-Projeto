# (1) Carregamento de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada de dados
arquivo = "lista_dados.CSV"
dados_org = pd.read_csv(arquivo, header=1, delimiter=";")
dados = dados_org.to_dict('list')



# Boxplot dos dados principais
coluna_alt = dados["Altura (mm)"]
plt.boxplot(coluna_alt)
plt.title("Altura (mm)")
plt.show()

coluna_dia = dados["Diametro (mm)"]
plt.boxplot(coluna_dia)
plt.title("Diâmetro (mm)")
plt.show()

coluna_massa = dados["Massa (g)"]
plt.boxplot(coluna_massa)
plt.title("Massa (g)")
plt.show()

coluna_resis = dados["Resistencia (kgf)"]
plt.boxplot(coluna_resis)
plt.title("Resistência (Kgf)")
plt.show()

# Boxplot de densidade
densidade = []
tamanho = len(dados["Resistencia (kgf)"])
contador = range(tamanho)
for i in contador:
    raio = dados["Diametro (mm)"][i] / 2
    massa = dados["Massa (g)"][i]
    altura = dados["Altura (mm)"][i]
    vol = np.pi*(raio**2)*altura
    valor = massa/vol
    densidade.append(valor)

id = dados["ID da amostra"]
print("ID das amostras: ", id)
print("Densidade: ", densidade)
plt.boxplot(densidade)
plt.title("Densidade (g/mm^2)")
plt.show()

# Boxplot de masssa absoluta
massa_absoluta = []
for i in contador:
    raio = dados["Diametro (mm)"][i] / 2
    altura = dados["Altura (mm)"][i]
    vol = np.pi * (raio ** 2) * altura
    m_abs = densidade[i] * vol
    massa_absoluta.append(m_abs)

print("Massa absoluta: ", massa_absoluta)
plt.boxplot(massa_absoluta)
plt.title("Massa Absoluta (g/mm^3)")
plt.show()

# Boxplot da relação de altura e diâmetro
T = []
for i in contador:
    dia = dados["Diametro (mm)"][i]
    altura = dados["Altura (mm)"][i]
    relacao = altura / dia
    T.append(relacao)

print("Altura / Diâmetro: ",T)
plt.boxplot(T)
plt.title("T = Altura / Diâmetro")
plt.show()

# Boxplot de àrea
area = []
for i in contador:
    raio = dados["Diametro (mm)"][i]
    a = np.pi * (raio ** 2)
    area.append(a)

print("Área: ", area)
plt.boxplot(area)
plt.title("Área (mm^2)")
plt.show()

# Boxplot de volume
volume = []
for i in contador:
    raio = dados["Diametro (mm)"][i] / 2
    altura = dados["Altura (mm)"][i]
    vol = np.pi * (raio ** 2) * altura
    volume.append(vol)

print("Volume: ", volume)
plt.boxplot(volume)
plt.title("Volume (mm^3)")
plt.show()

# Boxplot que calcula aproximado a tensão de ruptura das amostras
tensao_ruptura = []
for i in contador:
    forca = dados["Resistencia (kgf)"][i]
    raio = dados["Diametro (mm)"][i] / 2
    area_secao = np.pi * (raio ** 2)
    tensao = forca / area_secao
    tensao_ruptura.append(tensao)

print("Tensão de ruptura (kgf/mm²): ", tensao_ruptura)
plt.boxplot(tensao_ruptura)
plt.title("Tensão de Ruptura (kgf/mm²)")
plt.show()







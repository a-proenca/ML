import seaborn as sea
import pandas as pd
from matplotlib import pyplot as plt

dados = pd.read_csv('bank-full.csv', sep=';')

# Ver missing values
print(dados.info())
print(dados.count())

# Identificar se há null values no dataset (apesar do anterior já dar para ver)
print(dados.isnull().sum())

# Identificar se a nan values no dataset
print(dados.isna().sum())
# Identificar se há possiveis valores duplicados no dataset
print(dados.duplicated().sum())

# Ver estatisticas dos dados numericos(min,nax,media,quartis...etc) do nosso dataset
print(dados.describe())

# Analisar o target
dados.y.value_counts()
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sea.countplot(data=dados, x='y')
plt.title('Target Count')
plt.subplot(1, 2, 2)
labels = dados['y'].value_counts(sort=True).index
sizes = dados['y'].value_counts(sort=True)
plt.pie(sizes, labels=labels, autopct='%.2f')
plt.title('Target Yes and No')
plt.show()

# Analizar os empregos
plt.figure(figsize=(14, 22))
plt.subplot(2, 1, 1)
sea.countplot(data=dados, x='job')
plt.title('Distribuição de Empregos')
plt.subplot(2, 1, 2)
labels = dados['job'].value_counts(sort=True).index
sizes = dados['job'].value_counts(sort=True)
plt.pie(sizes, labels=labels, autopct='%.2f')
plt.title('Percentual de cada tipo de Emprego')
plt.show()

# Analisar o estado civil
print(dados.marital.value_counts())
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sea.countplot(data=dados, x='marital')
plt.title('Distribuição do estado civil')
plt.subplot(1, 2, 2)
labels = dados['marital'].value_counts(sort=True).index
sizes = dados['marital'].value_counts(sort=True)
plt.pie(sizes, labels=labels, autopct='%.2f')
plt.title('Percentual de cada tipo de estado civil')
plt.show()

# Analisar a educacao
print(dados.education.value_counts())
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sea.countplot(data=dados, x='education')
plt.title('Distribuição da Educação')
plt.subplot(1, 2, 2)
labels = dados['education'].value_counts(sort=True).index
sizes = dados['education'].value_counts(sort=True)
plt.pie(sizes, labels=labels, autopct='%.2f')
plt.title('Percentual de cada tipo de Educação')
plt.show()

# Analisar Credito a habitaçao
print(dados.housing.value_counts())
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sea.countplot(data=dados, x='housing')
plt.title('Credito a habitacao')
plt.subplot(1, 2, 2)
labels = dados['housing'].value_counts(sort=True).index
sizes = dados['housing'].value_counts(sort=True)
plt.pie(sizes, labels=labels, autopct='%.2f')
plt.title('Credito a habitaçao')
plt.show()

# Analisar Creditos ao consumo
print(dados.loan.value_counts())
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sea.countplot(data=dados, x='loan')
plt.title('Credito ao consumo')
plt.subplot(1, 2, 2)
labels = dados['loan'].value_counts(sort=True).index
sizes = dados['loan'].value_counts(sort=True)
plt.pie(sizes, labels=labels, autopct='%.2f')
plt.title('Credito ao Consumo')
plt.show()

# Analisar a forma de contacto
print(dados.contact.value_counts())
# MUDAR AS CORES OU MUDAR A ORDEM DO X DO SEAPLT COUNT
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sea.countplot(data=dados, x='contact')
plt.title('Tipo de Contacto')
plt.subplot(1, 2, 2)
labels = dados['contact'].value_counts(sort=True).index
sizes = dados['contact'].value_counts(sort=True)
plt.pie(sizes, labels=labels, autopct='%.2f')
plt.title('Tipo de contacto feito')
plt.show()

# Distribuicoes dos dados numericos com regressao linear
plt.figure(figsize=(10,10))

for i, col in enumerate(dados.select_dtypes(include=['int64']).columns):
    ax = plt.subplot(3,3, i+1)
    sea.histplot(x = dados[col], ax=ax, kde = True)

plt.suptitle('Distribuições das variaveis quantitativas')
plt.tight_layout()
plt.show()

# Matrix das correlaçoes
plt.subplots(figsize = (18,13))
hmap = sea.heatmap(data = dados.corr(), annot=True , linewidths=0.5)
plt.title("Correlation Matrix", fontsize=15)
plt.tight_layout()
plt.show()

# Vizualização das variaveis numericas por faixa etária
# Vamos fazer distribuições de 5 em 5 anos
plt.figure(figsize=(18,25))
plt.subplot(3,2,1)
faixaidades=[15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]
duracao_chamada_idades = dados.groupby(pd.cut(dados.age,faixaidades)).duration.mean().plot.bar()
plt.ylabel('Media de duracao da chamada')
plt.title('Distribuição da média da duração de uma chamada por faixa etária')
plt.subplot(3,2,2)
avg_balance_idades = dados.groupby(pd.cut(dados.age,faixaidades)).balance.mean().plot.bar()
plt.ylabel('Media de Saldo Anual em euros')
plt.title('Distribuição média do Saldo anual em euros por faixa etária')
plt.subplot(3,2,3)
##Ver melhor!!
last_day_month_contact_idades = dados.groupby(pd.cut(dados.age,faixaidades)).day.mean().plot.bar()
plt.ylabel('Ultio dia de contato do mês')
plt.title('Distribuição do ultimo dia de contato do mês por faixa etária')
plt.subplot(3,2,4)
campaign_contact_per_client_idades = dados.groupby(pd.cut(dados.age,faixaidades)).campaign.mean().plot.bar()
plt.ylabel('Numero de contactos realizados durante esta campanha para um cliente')
plt.title('Distribuição numero de contactos realizados durante esta campanha para um cliente por faixa etária')
plt.subplot(3,2,5)
campaign_contact_per_client_afterlastcampaign_idades = dados.groupby(pd.cut(dados.age,faixaidades)).pdays.mean().plot.bar()
plt.ylabel('Numero medio de dias que passou após o cliente ser contactado na ultima campanha')
plt.title('Distribuição do numero medio de dias que passou após o cliente ser contactado na ultima campanha por faixa etária')
plt.subplot(3,2,6)
number_contacts_beforethiscampaign_idades = dados.groupby(pd.cut(dados.age,faixaidades)).previous.mean().plot.bar()
plt.ylabel('Numero médio de contactos antes desta campanha para um cliente')
plt.title('Distribuição do numero médio de contactos antes desta campanha para um cliente')
plt.show()
#%%

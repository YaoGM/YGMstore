import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

def rand_color():
  c = "#"+"".join(map(hex,random.choices(range(256), k=3))).replace("0x","")
  if len(c) != 7:
    return rand_color()
  return c

data = pd.read_csv('Life Expectancy Data.csv')
data.describe().transpose()
data.describe(include="object").transpose()

#print(data.info())
obj_cols = data.select_dtypes(include='object').columns.tolist()
num_cols = data.select_dtypes(exclude='object').columns.drop("Life expectancy ").tolist()

plt.figure(figsize=(12,8))
sns.distplot(data['Life expectancy '], color="#008dce")
plt.show()

plt.figure(figsize=(12,8))
sns.countplot(data=data, y= 'Status', order=data["Status"].value_counts().index, palette= "husl")
plt.show()

data1=data.drop(labels='Country',axis=1).drop(labels='Status',axis=1)
plt.figure(figsize=(20,12))
sns.heatmap(data1.corr(),annot=True)
plt.show()
pd.DataFrame(abs(data1.corr()['Life expectancy '].drop('Life expectancy ')*100).sort_values(ascending=False)).plot.bar(figsize = (12,8))
plt.show()

num_cols = ['Year','Schooling','Income composition of resources','Adult Mortality']
for col in num_cols:
    print("\n")
    fig, ax =plt.subplots(1,2, figsize=(15,8))
    sns.boxplot(data=data1, y=col, ax=ax[0], color=rand_color())
    sns.scatterplot(data=data1,x = 'Life expectancy ', s = 100, y=col, ax=ax[1], color = rand_color())
    plt.show()
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import gcf, figure
import pandas as pd
import seaborn as sns
from sklearn import tree
from sklearn.linear_model import Ridge
from sklearn.ensemble import GradientBoostingClassifier
import mglearn
%matplotlib inline

data = pd.read_csv(r'/media/nikita/ML/pipes/ML_pipes/info/Informatsia.csv')
#data = pd.read_csv(r'H:/Machine_learning/info/Informatsia.csv')

pipes = pd.DataFrame(data)

pipes_for_lin_reg = pipes.head(1200).tail(300).append(pipes.tail(1200).head(300))

pipes = pipes.head(1200).append(pipes.tail(1200))

map_to_int = {name: n for n, name in enumerate(pipes["Вид прокладки тепловой сети"].unique())}
pipes["Вид прокладки тепловой сети"] = pipes["Вид прокладки тепловой сети"].replace(map_to_int)
pipes_for_lin_reg["Вид прокладки тепловой сети"] = pipes_for_lin_reg["Вид прокладки тепловой сети"].replace(map_to_int)
def encode_target(pipes, target_column):
    pipes_mod = pipes.copy()
    targets = pipes[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets)}
    pipes_mod["Target"] = pipes_mod[target_column].replace(map_to_int)
    
    return(pipes_mod, targets)

del pipes['Unnamed: 25']
del pipes['Unnamed: 26']
del pipes['Unnamed: 27']
del pipes_for_lin_reg['Unnamed: 25']
del pipes_for_lin_reg['Unnamed: 26']
del pipes_for_lin_reg['Unnamed: 27']

pipes2, targets = encode_target(pipes, "Аварийность")
pipes_for_lin_reg2, targets2 = encode_target(pipes_for_lin_reg, "Аварийность")

for i in range(len(pipes.columns)):
   print(i, ":", pipes.columns[i])

disblance = pipes['Аварийность'].value_counts()
print(disblance[1]/disblance[0])


"""
Надземная = 0
Подземная канальная = 1
Подземная бесканальная = 2
Подвальная = 3
"""

"""
Таргеты:

Без аварии - 0
Авария - 1


"""

#print(pipes2.info())

clmns = list(pipes2.columns[5:24])
#print(pipes2.info())

cr = clmns + list(pipes2.columns[24:25])

for i in range(len(cr)):
   print(i, ":", cr[i])


sns.heatmap(pipes.corr('kendall'), cmap="seismic", vmin=-1, vmax=1) ;


corr = pipes[cr].corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)

new_clmns = list(clmns[1:15])
for i in new_clmns: print(i)
cr = new_clmns + list(pipes2.columns[24:25])
corr = pipes[cr].corr()
corr.style.background_gradient(cmap='coolwarm').set_precision(2)

X, y = pipes[new_clmns], pipes2['Target']

X_test, y_test = pipes_for_lin_reg[new_clmns], pipes_for_lin_reg2['Target']

sns.violinplot(x='Аварийность', y='Год ввода в эксплуатацию', data=pipes);

pipes['Год ввода в эксплуатацию'].hist();

sns.violinplot(x='Аварийность', y='Шероховатость подающего трубопровода, мм', data=pipes);

ct = pd.crosstab(pipes['Шероховатость подающего трубопровода, мм'], pipes['Аварийность'])
ct.plot.bar();

ct = pd.crosstab(pipes['Год ввода в эксплуатацию'], pipes['Аварийность'])
ct.plot.bar();

dt = tree.DecisionTreeClassifier(min_samples_split=450)
dt.fit(X, y)
figure(num=None, figsize=(22, 10), dpi=80, facecolor='w', edgecolor='k')
#feature_names=clmns для вывода названий таблиц
tree.plot_tree(dt, filled=True, fontsize=10, rounded=True, max_depth=6)
for i in range(len(clmns)):
   print(i, ":", clmns[i])
plt.show()

#предугадывание шанса аварии
#print(dt.predict_proba([[0.5, 0.5, 2020]])[0])

lr = Ridge().fit(X, y)
print(lr.coef_)
print(lr.intercept_)

print(X_test.shape, y_test.shape)

print(lr.score(X, y))
print(lr.score(X_test, y_test))

gbrt = GradientBoostingClassifier(random_state=0, learning_rate=0.01, max_depth=15)
gbrt.fit(X, y)
print(gbrt.score(X, y))
print(gbrt.score(X_test, y_test))

def plot_feature_importances(model):
 n_features = X.shape[1]
 plt.barh(range(n_features), model.feature_importances_, align='center')
 plt.yticks(np.arange(n_features), new_clmns)
 plt.xlabel("Важность признака")
 plt.ylabel("Признак")
plot_feature_importances(gbrt)
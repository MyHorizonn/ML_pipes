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

def pipes(arr):

   data = pd.read_csv(r'/home/nikita/ML/pipes/ML_pipes/info/Informatsia.csv')
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
   clmns = list(pipes2.columns[5:24])
   new_clmns = list(clmns[1:15])

   X, y = pipes[new_clmns], pipes2['Target']

   X_test, y_test = pipes_for_lin_reg[new_clmns], pipes_for_lin_reg2['Target']

   gbrt = GradientBoostingClassifier(random_state=0, learning_rate=0.01, max_depth=15)
   gbrt.fit(X, y)
   #predict
   return(gbrt.score(X_test, y_test))

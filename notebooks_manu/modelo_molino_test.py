# -*- coding: utf-8 -*-
"""Modelo Molino Test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zKHBvyjYbQWtJgzJxp55OEsvBZFUbuUp
"""

import tensorflow as tf
import numpy as np
import pandas as pd
from urllib import request

url="INSERTAR URL DEL DATASET DE TESTEO ACA"

f = request.urlopen(url)
dataset = pd.read_csv(f)

#@title Funciones auxiliares
def normalizar(dataset, dataset_train):
  return (dataset - dataset_train.mean()) / dataset_train.std()

def ecm(original, prediccion):
  return ((original-prediccion)**2).mean()

def separar_en_x_e_y(dataset):
  return (dataset.iloc[:,:-2], dataset.iloc[:,-2:])

model = tf.keras.models.load_model('modelo_molinos.h5')

dataset_curado = dataset[(dataset.iloc[:,:-2] >= 0).any(axis=1)]
dataset_curado.shape


velocidad_x = dataset_curado['Velocity']*dataset_curado['Direction'].map(lambda x: -np.sin(np.pi*x/180))
velocidad_y = dataset_curado['Velocity']*dataset_curado['Direction'].map(lambda x: -np.cos(np.pi*x/180))

dataset_velocidad_cartesiana = dataset_curado.iloc[:,:-2].copy()

dataset_velocidad_cartesiana['Velocity X'] = velocidad_x
dataset_velocidad_cartesiana['Velocity Y'] = velocidad_y

X, y = separar_en_x_e_y(dataset_velocidad_cartesiana)

y_pred = model.predict(X)
print(ecm(y_pred, y))
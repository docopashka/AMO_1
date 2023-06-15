# -*- coding: utf-8 -*-
"""model_preprocessing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ijl4toJXLYrPGSlNhYlfhV5EAD_3DSDg
"""

import pandas as pd

df_train=pd.read_csv('/content/train/train.csv')
df_test=pd.read_csv('/content/test/test.csv')

def boolConvert(prec):
    if(prec==True):
        return 1
    elif(prec==False):
        return 0
    return

df_train['precipitation']=df_train['precipitation'].apply(lambda x: boolConvert(x))
df_test['precipitation']=df_test['precipitation'].apply(lambda x: boolConvert(x))

def Year(date):
    return date.split('-')[0]
def Month(date):
    return date.split('-')[1]
def Day(date):
    return date.split('-')[2]
def Hour(time):
     return time.split(':')[0]
def Minute(time):
     return time.split(':')[1]
def Second(time):
     return time.split(':')[2]

df_train['Year']=df_train['date'].apply(lambda x: Year(x))
df_test['Year']=df_test['date'].apply(lambda x: Year(x))

df_train['Month']=df_train['date'].apply(lambda x: Month(x))
df_test['Month']=df_test['date'].apply(lambda x: Month(x))

df_train['Day']=df_train['date'].apply(lambda x: Day(x))
df_test['Day']=df_test['date'].apply(lambda x: Day(x))

df_train['Hour']=df_train['time'].apply(lambda x: Hour(x))
df_test['Hour']=df_test['time'].apply(lambda x: Hour(x))

df_train['Minute']=df_train['time'].apply(lambda x: Minute(x))
df_test['Minute']=df_test['time'].apply(lambda x: Minute(x))

df_train['Second']=df_train['time'].apply(lambda x: Second(x))
df_test['Second']=df_test['time'].apply(lambda x: Second(x))

df_train=df_train.drop('date', axis=1)
df_test=df_test.drop('date', axis=1)
df_train=df_train.drop('time', axis=1)
df_test=df_test.drop('time', axis=1)

df_train[['Year','Month', 'Day', 'temperature', 'precipitation']]=df_train[['Year','Month', 'Day', 'temperature', 'precipitation']].astype(int)
df_test[['Year','Month', 'Day', 'temperature', 'precipitation']]=df_test[['Year','Month', 'Day', 'temperature', 'precipitation']].astype(int)

df_train.to_csv(r'/content/train/train_preprocessing.csv', index=False)
df_test.to_csv(r'/content/test/test_preprocessing.csv', index=False)
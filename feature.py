import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

train=pd.read_csv("ai4i2020.csv")
train.head()


train.info()


pd.get_dummies(train['Type'],drop_first=True).head

Type = pd.get_dummies(train['Type'],drop_first=True)
train.drop(['Product ID','Type','Machine failure','TWF','HDF','PWF','OSF','RNF'],axis=1,inplace=True)

train.head()
train = pd.concat([Type],axis=1)
train.head()

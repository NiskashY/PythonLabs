"""
import pandas as pd
from matplotlib import pyplot as plt


init_data = pd.read_csv('test.csv')
sample_data= init_data.sample(n=1000, replace='False')
print(sample_data)

series = sample_data.isnull().sum()

print("Amount of NaN elements:", sum([item for item in series if item != 0]))



# plt.boxplot() - ящик с усами (boxwhisker)

"""

import numpy as np
import pandas as pd
import pickle  # save model

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img
import seaborn as sns

# divide dataset
from sklearn.model_selection import train_test_split, KFold, GridSearchCV

# models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# import metrics
from sklearn.metrics import mean_squared_error as mse, r2_score as r2

from scipy.stats import mode
import datetime

matplotlib.rcParams.update({'font.size': 10})


# get data from test.csv
DATA_TEST_PATH = 'test.csv'
init_data = pd.read_csv(DATA_TEST_PATH)
# mix value in init_data and get 1000 of them
df = init_data.sample(n=1000)

# show amount of NaN elements in each category
print("Amount of nulls in each category:")
print(df.isna().sum())

PREPARED_DATASET_PATH = './price_prepared.csv'
"""
df.DistrictId = df.DistrictId.astype(object)
df.Id = df.Id.astype(object)
df.info()
print(df.describe())
"""

# insert into plt hisotgram of data
digital_features = df.select_dtypes(exclude=[object])
digital_features.hist(figsize=(18,12), bins=30)

# insert into plt boxplot of data
plt.figure(figsize=(16, 8), num='BoxplotData')
sns.boxplot(data=df[['Square', 'LifeSquare', 'KitchenSquare']], orient='h')
plt.xscale('symlog')
plt.xlim(left=-1)

# show histogram and boxplot
plt.show()

"""
df.loc[df['Rooms'].isin([0, 10, 19]), 'Rooms'] = int(df['Rooms'].median())
print(df.describe())
"""

# show charasterictics before
print(df.describe())

df.loc[(df['LifeSquare'] > (3 / 2) * df['LifeSquare'].median) | ((df['LifeSquare'] < 0.5 * df['LifeSquare'].median)), 'LifeSquare'] = df['LifeSquare'].median()
df.loc[(df['Square'] > (3 / 2) * df['Square'].median) | ((df['Square'] < 0.5 * df['Square'].median)), 'Square'] = df['Square'].median()
df.loc[(df['KitchenSquare'] > (3 / 2) * df['KitchenSquare'].median) | ((df['KitchenSquare'] < 0.5 * df['KitchenSquare'].median)), 'KitchenSquare'] = df['KitchenSquare'].median()

# show charasterictics after
df.describe()

digital_features = df.select_dtypes(exclude=[object])
digital_features.hist(figsize=(18,12), bins=30)

#plt.show()




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

DATA_TEST_PATH = 'test.csv'
df = pd.read_csv(DATA_TEST_PATH)

PREPARED_DATASET_PATH = './price_prepared.csv'

df.DistrictId = df.DistrictId.astype(object)
df.Id = df.Id.astype(object)
df.info()
print(df.describe())

digital_features = df.select_dtypes(exclude=[object])
digital_features.hist(figsize=(18,12), bins=30)
plt.show()



# import matplotlib.pyplot as plt
# import pandas as pd
# import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std


#read csv file
# df = pd.read_csv('./kospi.csv', encoding='utf8')
# df = pd.read_csv('./kosdaq.csv', encoding='utf8')
df = pd.read_excel('./large_model2.xlsx', 'Sheet1')
# df = pd.read_csv('./kosdaq.csv', encoding='utf8')
small_kospi = pd.read_excel('./small_model2.xlsx', '코스피')
small_kosdaq = pd.read_excel('./small_model2.xlsx', '코스닥')

mid_kospi = pd.read_excel('./mid_model2.xlsx', 'kospi')
mid_kosdaq = pd.read_excel('./mid_model2.xlsx', 'kosdaq')

small_df = pd.concat([small_kospi, small_kosdaq])
mid_df = pd.concat([mid_kospi, mid_kosdaq])

total_df = pd.concat([df, small_df, mid_df])

index = total_df['index']

print (len(index)) # 160 + 160 + 160


for i, idx in enumerate(index):
  # companydummy[idx] = [0] * i*4 + [1] * (4) + [0] * (160-4*i)
  if (i%4 == 0):
    # print (idx, i)
    total_df[idx] = [0] * (i) + [1] * (4) + [0] * (480 - 4-i)
    # print (X)
  else:
    continue
 
total_df = total_df.dropna(subset=['per'], axis=0, how='any')
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print (df['per'])

total_df.to_csv('./total_model3.csv', sep=',', index=False)

Y = total_df['베타값']
X = total_df.drop(['베타값', 'index'], axis=1)
print (np.where(pd.isnull(X)))

X.astype(float)
Y.astype(float)
# print (Y)

model = sm.OLS(Y, X)
results = model.fit()
sys.stdout = open("total_model3.txt", "w")
print(results.summary())
sys.stdout.close()

# df.to_csv('./kospi.csv', sep=',', index=False)

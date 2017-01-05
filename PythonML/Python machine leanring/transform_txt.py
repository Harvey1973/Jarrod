import pandas as pd
import numpy as np
df = pd.read_csv('TEST.csv',sep=',')
x = df.iloc[0:4,[0,1]].values
Y=df.iloc[0:4,3].values
Y=np.array(Y)

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("/Users/luke/Desktop/python_project/GitClone/scientific-computing-archive/optics/LR1/p-half.csv")

print(df)

plt.plot(df['Time - Plot 0'], df['Amplitude - Plot 0'])
plt.show()
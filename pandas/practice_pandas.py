import pandas as pd
import numpy as np
import random

file = r"D:\\Archivos\\MOCK_DATA.csv"

dataset = pd.read_csv(file,header=0,index_col=0,encoding='ISO-8859-1',sep=',',na_values=' ',low_memory=False)
dataset.index.name = 'ID'
print(dataset[dataset['country'] == 'Argentina'])
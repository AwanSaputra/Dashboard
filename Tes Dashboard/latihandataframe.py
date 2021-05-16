import numpy as np
import pandas as pd

df = pd.read_excel('masukan.xlsx')
print(df.No.count())
for x in range(4):
    print(df.IPK[x])

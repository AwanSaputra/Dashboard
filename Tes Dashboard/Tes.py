# from tes2 import Ui_MainWindow
from pyxlsb import open_workbook as open_xlsb
import matplotlib.pyplot as plt
import pandas as pd
import os.path
import datetime
import numpy as np
d1 = datetime.datetime(2021, 2, 28)
# path_to_file = "d:\KALBE\FPP.xlsb"
# date_cols = ["TGL"]
df = pd.read_excel(r'd:\KALBE\FPPFKP.xlsx', index_col=None,
                   sheet_name='FPP', skiprows=4, usecols="B,D,O")
# df = pd.read_excel(path_to_file, index_col=None, na_values=[
#                    'NA'], engine='pyxlsb', sheet_name='FPP', usecols="B,D,O", skiprows=4)

print(df)
# print("setelah format tanggal")
# df['TGL'] = pd.to_datetime(df.TGL, format="%Y-%m-%d")

# with open_xlsb(path_to_file) as wb:
#     with wb.get_sheet('FPP') as sheet:
#         for row in sheet.rows(5):
#             df.append([item.v for item in row])

# df = pd.DataFrame(df[1:], columns=df[0])
# df.loc['2018']

# df["messageDate"] = pd.to_datetime(df["messageDate"])
# time_mask = (df['messageDate'].dt. >= 13) & \
#             (df['messageDate'].dt.hour <= 15)
# pd.concat([df])

mask = df['TGL'].map(lambda x: x.month) == 1
df_with_good_dates = df.loc[mask]
print(df_with_good_dates)
month_list = [i.strftime("%b-%y")
              for i in df_with_good_dates['TGL']]

print("Tes")
x = df_with_good_dates[df_with_good_dates.tier1 == 'planning'].groupby(
    [df_with_good_dates.TGL.dt.year, df_with_good_dates.TGL.dt.month]).agg({"tier1": "count"}).values.tolist()

var = [i[0] for i in x]
print(var)

y = df_with_good_dates[df_with_good_dates.tier1 == 'ADMINISTRASI'].groupby(
    [df_with_good_dates.TGL.dt.year, df_with_good_dates.TGL.dt.month]).count().values.tolist()
print(sorted(set(month_list)))
print("tes2")
print(x)
print(y)
print("tes3")
print(df_with_good_dates[df_with_good_dates.tier1 == 'planning'].groupby(
    [df_with_good_dates.TGL.dt.year, df_with_good_dates.TGL.dt.month]).count())
# # X = df_with_good_dates.count()

# # print(X)
# # print(df['tier1'].drop_duplicates())
# # print(df.tier1.sort_values().count())
# # bool_series = pd.notnull(df["tier1"])
# # print("biar ga bingung ya kan")
# # print(df.count())
# # # print(df.tier1['planning'].count())
# # print(df.loc[df['tier1'] == 'planning'].count())
# # print(df.loc[df['tier1'] == 'ADMINISTRASI'].count())
# # print(df.loc[df['tier1'].isNull()].count())
# # print(df[bool_series].count())
# planning = df_with_good_dates.loc[df_with_good_dates['tier1'] == 'planning'].count()[
#     0]
# ADMINISTRASI = df_with_good_dates.loc[df_with_good_dates['tier1'] == 'ADMINISTRASI'].count()[
#     0]


# labels = ['planning', 'ADMINISTRASI']
# values = [planning, ADMINISTRASI]


# bars = plt.bar(labels, values)
# plt.bar(labels, values, color=['purple', 'blue'])
# plt.xticks(labels, labels, rotation='vertical')
# plt.title('DATA FPP', fontdict={'fontweight': 'bold', 'fontsize': 18})
# # plt.show()

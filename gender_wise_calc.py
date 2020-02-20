import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

empsal_df=pd.read_csv('empsalupdated.csv',index_col='empno')
print('\n\nSum Details(M/F):\n\n')
print(empsal_df.groupby(['sex'])['salary','hra','conv','total'].sum())
print('\n\nMean Details(M/F):\n\n')
print(empsal_df.groupby(['sex'])['salary','hra','conv','total'].mean())
print('\n\nStandard Deviation Details(M/F):\n\n')
print(empsal_df.groupby(['sex'])['salary','hra','conv','total'].std())



x=input('\n\nPress Enter to Continue')

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

empsal_df=pd.read_csv('empsalupdated.csv',index_col='empno')
expyr=empsal_df['expyr']
salary=empsal_df['salary']
plt.scatter(expyr,salary,color='green',label='Salary')
plt.title('Experience vs Salary')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()

x=input('Press Enter to Continue')

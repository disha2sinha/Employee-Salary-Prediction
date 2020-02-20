from tkinter import *
from tkinter import messagebox as msg
import pandas as pd
from pandastable import Table
import datetime
from datetime import date

class updt_df:
    def __init__(self, root):
        self.f = Frame(root, height=500, width=500) 
        self.f.pack()

        self.message_label=Label(self.f,text='Display Updated Dataframe',font=('Roman',24,'bold'),fg='navy blue')
        self.confirm_button=Button(self.f,text='Display',font=('Arial',14),bg='light green',fg='White',command=self.update_df,activeforeground='green')
        self.exit_button=Button(self.f,text='Exit',font=('Arial',14),bg='pink',fg='White',command=root.destroy,activeforeground='red')

        self.message_label.grid(row=1,column=1)
        self.confirm_button.grid(row=3,column=0)
        self.exit_button.grid(row=3,column=2)
    def update_df(self):
        try:
            empsal_df=pd.read_excel("Empsal.xlsx",index_col='empno')
            def age_cal(dob):
                today=date.today()
                Age=today.year-dob.year-((today.month,today.day)<(dob.month,dob.day))
                return Age
            empsal_df['Age']=empsal_df['dob'].apply(age_cal)

            empsal_df['conv']=0.1 * empsal_df['salary']
            empsal_df['total']=empsal_df['salary'] + empsal_df['hra'] + empsal_df['conv']
            print(empsal_df.head(10))
            empsal_df.to_csv('empsalupdated.csv')
            if(len(empsal_df)==0):
                msg.showinfo('Warning','No records')
            else:
                msg.showinfo('Message','Pandas df created')
                
            self.f = Frame(root, height=300, width=800) 
            self.f.pack(fill=BOTH,expand=1)
        
            self.table = Table(self.f,dataframe=empsal_df, read_only=True)
            self.table.show()
        except FileNotFoundError as e:
            msg.showerror('Error in Finding File',e)
#---------------------------------
root = Tk()
root.title('Updated Dataframe with conv and total')
root.geometry('800x800')
obj=updt_df(root)
root.mainloop()

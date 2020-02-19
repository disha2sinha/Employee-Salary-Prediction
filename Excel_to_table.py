from tkintertable import TableCanvas, TableModel
from tkinter import *
from tkinter import messagebox as msg
import pandas as pd
from pandas import ExcelWriter
from pandastable import Table
class excel_to_df():
    def __init__(self, root):
        self.f = Frame(root, height=350, width=500) 
        self.f.pack()

        self.message_label=Label(self.f,text='Excel file to Pandas DF/tkintertable:',font=('Roman',24,'bold'),fg='navy blue')
        self.confirm_button=Button(self.f,text='Convert',font=('Arial',14),bg='light green',fg='White',command=self.conv_to_df,activeforeground='green')
        self.exit_button=Button(self.f,text='Exit',font=('Arial',14),bg='pink',fg='White',command=root.destroy,activeforeground='red')

        self.message_label.grid(row=1,column=1)
        self.confirm_button.grid(row=3,column=0)
        self.exit_button.grid(row=3,column=2)
    def conv_to_df(self):
        try:
            empsal_df=pd.read_excel('empsal_excel.xlsx', index_col='empno')
            if(len(empsal_df)==0):
                msg.showinfo('Warning','Excel file has no records')
            else:
                msg.showinfo('Message','Pandas df created')
                print("Pandas Dataframe:")
                print(empsal_df)

            self.f = Frame(root, height=300, width=300) 
            self.f.pack(fill=BOTH,expand=1)
        
            self.table = Table(self.f,dataframe=empsal_df, read_only=True)
            self.table.show()
        except FileNotFoundError as e:
            msg.showerror('Error in opening file',e)                
#---------------------------------
root = Tk()
root.title('Excel to DF')
root.geometry('800x800')
obj=excel_to_df(root)
root.mainloop()

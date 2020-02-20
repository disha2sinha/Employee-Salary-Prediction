from tkintertable import TableCanvas, TableModel
from tkinter import *
from tkinter import messagebox as msg
import pandas as pd
from pandas import ExcelWriter
class csv_to_excel():
    def __init__(self, root):
        self.f = Frame(root, height=500, width=500) 
        self.f.pack()

        self.message_label=Label(self.f,text='Conversion of CSV to Excel file:',font=('Roman',24,'bold'),fg='navy blue')
        self.confirm_button=Button(self.f,text='Convert',font=('Arial',14),bg='light green',fg='White',command=self.conv_to_xls,activeforeground='green')
        self.exit_button=Button(self.f,text='Exit',font=('Arial',14),bg='pink',fg='White',command=root.destroy,activeforeground='red')

        self.message_label.grid(row=1,column=1)
        self.confirm_button.grid(row=3,column=0)
        self.exit_button.grid(row=3,column=2)
    def conv_to_xls(self):
        try:
            empsal_df=pd.read_csv('empsal.csv', index_col='empno')
            print(empsal_df)
            if(len(empsal_df)==0):
                msg.showinfo('Warning','CSV has no rows')
            else:
                writer=ExcelWriter('Empsal.xlsx')
                empsal_df.to_excel(writer,'Sheet1')
                writer.save()
                msg.showinfo('Message','Excel file created')
        except FileNotFoundError as e:
            msg.showerror('Error in opening file',e)
                
        
                  
#---------------------------------
root = Tk()
root.title('CSV to Excel File')
root.geometry('800x800')
obj=csv_to_excel(root)
root.mainloop()

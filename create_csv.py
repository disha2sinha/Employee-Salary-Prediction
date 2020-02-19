from tkintertable import TableCanvas, TableModel
from tkinter import *
from tkinter import messagebox as msg
import pandas as pd
class create_csv():
    def __init__(self, root):
        self.f = Frame(root, height=500, width=500) 
        self.f.pack()

        self.message_label=Label(self.f,text='Display the Empsal CSV:',font=('Roman',24,'bold'),fg='navy blue')
        self.confirm_button=Button(self.f,text='Display',font=('Arial',14),bg='light green',fg='White',command=self.conv_to_csv,activeforeground='green')
        self.exit_button=Button(self.f,text='Exit',font=('Arial',14),bg='pink',fg='White',command=root.destroy,activeforeground='red')

        self.message_label.grid(row=1,column=1)
        self.confirm_button.grid(row=3,column=0)
        self.exit_button.grid(row=3,column=2)
    def conv_to_csv(self):
        self.f = Frame(root, height=300, width=300) 
        self.f.pack(fill=BOTH,expand=1)
        
        self.table = TableCanvas(self.f, read_only=True)
        self.table.importCSV('empsal.csv')
        self.table.show()
        
                  
#---------------------------------
root = Tk()
root.title('Create CSV')
root.geometry('800x800')
obj=create_csv(root)
root.mainloop()

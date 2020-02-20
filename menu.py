# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:45:56 2020

@author: Debanjana
"""
import sys
import os
import subprocess
from tkinter import *

class empsal:
    def __init__(self,root):
        
        self.mainLabel=Label(root,text='Employee HR Database : Query by using Python and ML',font=('Arial',-15,'bold underline'))
        self.mainLabel.place(x=200,y=300)
        
        
        self.menubar=Menu(root)
        root.config(menu=self.menubar)
        
        self.mysql_menu=Menu(root,tearoff=0)
        self.menubar.add_cascade(label='CSV/DF File Maintenance',menu=self.mysql_menu)
        self.mysql_menu.add_command(label='Build/Display Csv File',command=self.create_csv)
        self.mysql_menu.add_command(label='Convert Csv to excel',command=self.csv_to_excel)
        self.mysql_menu.add_command(label='Display Data from Excel',command=self.excel_to_table)
        
        self.mysql_menu.add_separator()
        self.mysql_menu.add_command(label='Exit',command=root.destroy)
        
        self.reports_menu=Menu(root,tearoff=0)
        self.menubar.add_cascade(label='Reports/Data Visualization',menu=self.reports_menu)
        self.reports_menu.add_command(label='Display Updated DF',command=self.disp_updt_df)
        self.reports_menu.add_command(label='State Wise Mean Expenses,Bar Graph',command=self.state_wise_mean)
        self.reports_menu.add_command(label='Gender wise sum,mean,std. Deviation',command=self.gender_wise_calc)
        self.reports_menu.add_command(label='State Wise Total Expenses ,Bar Graph',command=self.state_wise_total)
        self.reports_menu.add_command(label='Scatter plot of experience in years(x) v/s Salary(y)',command=self.scatter_plot)
        
        
        self.predict_menu=Menu(root,tearoff=0)
        self.menubar.add_cascade(label='Prediction',menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict Salary given experience',command=self.predict_salary)
        
        
    def create_csv(self):
        os.system("python.exe create_csv.py")
    def csv_to_excel(self):
        os.system("python.exe csv_to_xls.py")
    def excel_to_table(self):
        os.system("python.exe Excel_to_table.py")
    
    def disp_updt_df(self):
        os.system("python.exe disp_updt_df.py")
    def state_wise_mean(self):
        os.system("python.exe state_wise_mean.py")
        
    def state_wise_total(self):
        os.system("python.exe state_wise_total.py")
    def gender_wise_calc(self):
        os.system("python.exe gender_wise_calc.py")
    def scatter_plot(self):
        os.system("python.exe scatter_plot.py")
    def predict_salary(self):
        os.system("python.exe predict_salary.py")
        

        

root=Tk()
root.title("Employee HR Database Query System using Python ,ML")
root.geometry("800x800")
obj=empsal(root)
root.mainloop()  
        

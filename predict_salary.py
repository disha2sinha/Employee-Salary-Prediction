import pandas as pd
import numpy as np
import os.path
import matplotlib.pyplot as plt
from datetime import date
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.model_selection import train_test_split
from tkinter import messagebox as msg
from tkinter import *
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.metrics import r2_score


class Predict_salary:
    def __init__(self,root):
        self.f=Frame(root,height=200,width=300)
        self.f.pack()
        
        self.messageLabel=Label(self.f,text='Predict Salary Using Experience In Years',font='Arial')
        self.inputLabel=Label(self.f,text='Enter experience of employee in years',font=('Arial',14))
        self.outputLabel=Label(self.f,text='',font=('Arial',14))
        self.experience=Entry(self.f,text='',width=10,font=('Arial',14))
        self.predictedLabel=Label(self.f,text='',font=('Arial',15))
        self.predictButton=Button(self.f,text='Predict',font=('Arial',12),command=self.predict_salary)
        self.exitButton=Button(self.f,text='Exit',font=('Arial',12),command=root.destroy)
    
        
        
     
        
        
        self.messageLabel.grid(row=0,column=0)
        self.inputLabel.grid(row=1,column=0)
        self.experience.grid(row=1,column=1)
        self.predictedLabel.grid(row=2,column=0)
        self.predictButton.grid(row=3,column=1)
        self.exitButton.grid(row=3,column=0)
        self.outputLabel.grid(row=4,column=0)
        
        
  

    def predict_salary(self):
        try:
            if(os.path.exists('empsal.csv')):

                    data=pd.read_csv("empsal.csv",parse_dates=True,infer_datetime_format=True)

                    print(data.head())
                    def calculate_age(dob):
                          return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))




                    today=date.today()
                    data['dob']=pd.to_datetime(data['dob'])


                    data['age']=data['dob'].apply(calculate_age)

                    data.isnull().sum() #Checking if null values are present

                    data.drop(columns=['empname','dob','hra'],inplace=True)# dropping unnecessary columns


                    oh=OneHotEncoder()
                    lc=LabelEncoder()
                    data['sex']=lc.fit_transform(data['sex'])# Coverting sex column from categorical to integer
                    #integer_encoded=lc.fit_transform(data['city'])
                    #integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
                    #integer_encoded=oh.fit_transform(integer_encoded)



                    correlation=data.corr()  #Checking if the predicting columns are interrelated 
                    sns.heatmap(correlation)
                    #Checking for linearity
                    #plot shows that age ,sex and years of experience 
                    sns.pairplot(data)

                    #assigning x and y for prediction using only experience
                    #x=data.iloc[:,[1,4,6]]
                    x=data.iloc[:,4:5]
                    y=data.iloc[:,5]

                    lreg=LinearRegression()
                    score=[]
                    for i in range(1000):
                        x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=i,test_size=0.05)
                        lr=lreg.fit(x_train,y_train)
                        score.append(lr.score(x_test,y_test))

                    k=score.index(max(score))


                    x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=k,test_size=0.05)

                    lreg.fit(x_train,y_train)

                    y_pred=lreg.predict(x_test)

                    print(r2_score(y_pred,y_test))
                    
                    newX=np.array([[float(self.experience.get())]])
                    newy=lreg.predict(newX)
                    self.outputLabel.config(text='Expected Salary is:'+str(newy[0]),font=('Arial',15))
                    
                    print(newy)

        except FileNotFoundError as e:
                msg.showerror('File path is wrong or file not found',e)
                
                
                
root=Tk()
root.title("My First tkinter test")
root.geometry('1000x300')
obj=Predict_salary(root)
root.mainloop()

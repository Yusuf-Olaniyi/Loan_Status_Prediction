# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:16:17 2024

@author: YUSUF
"""
import uvicorn
from fastapi import FastAPI
from applicant_details import applicant_detail
#import numpy as np
import pickle
import pandas as pd

app = FastAPI()
loan_status_predictor = open('loan_status_classifier.pkl','rb')
classifier = pickle.load(loan_status_predictor)

def loan_predict(Dependents,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History, Property_Area ,Gender,Graduate,Married,Self_Employed):
    if Property_Area == 'Rural':
        Property_Area = 0
    elif Property_Area == 'Semiurban':
        Property_Area = 1
    else:
        Property_Area = 2
    
    
    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0
    
    if Graduate == 'Graduate':
        Graduate= 1
    else:
        Graduate = 0
        
    if Married == 'Married':
        Married = 1
    else:
        Married = 0
        
    if Self_Employed == 'Yes':
        Self_Employed =1
    else:
        Self_Employed = 0
        
    df = pd.DataFrame({'Dependents': Dependents,'ApplicantIncome':ApplicantIncome,'CoapplicantIncome':CoapplicantIncome
                       ,'LoanAmount': LoanAmount,'Loan_Amount_Term':Loan_Amount_Term,'Credit_History':Credit_History
                       ,'Property_Area':Property_Area,'Gender_Male':Gender,'Education_Not Graduate':Graduate,'Married_Yes':Married
                       ,'Self_Employed_Yes':Self_Employed},index= pd.Series(1) )
    return classifier.predict(df)

#Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.post('/predict')
def predict_status(data:applicant_detail):
    data = data.dict()
    dependent=data['dependent']
    income=data['income']
    co_app_income=data['co_app_income']
    loan_amt=data['loan_amt']
    loan_term=data['loan_term']
    cred_hist=data['cred_hist']
    prop_area=data['prop_area']
    gender = data['gender']
    grad = data['grad']
    marr = data['marr']
    self_emp = data['self_emp']
    prediction = loan_predict(dependent,income,co_app_income,loan_amt,
                       loan_term,cred_hist,prop_area,gender,
                      grad,marr,self_emp)
    
    return {'prediction' : prediction[0]}
    #print(dependent,income,co_app_income,loan_amt,loan_term,cred_hist,prop_area,gender,grad,marr,self_emp)
    
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
   
    #if(prediction[0]>0.5):
     #   prediction="Fake note"
    #else:
     #   prediction="Its a Bank note"
    #return {
     #   'prediction': prediction
    #}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn fast_api_loan:app --reload


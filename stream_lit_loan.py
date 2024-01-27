# -*- coding: utf-8 -*-

"""
Created on Sat Jun 11 08:56:52 2022

@author: YUSUF
"""

import streamlit as st
import pickle
import pandas as pd


loan_status_predictor = open('loan_status_classifier.pkl','rb')
classifier = pickle.load(loan_status_predictor)

def loan_predict(Dependents,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History, Property_Area ,Gender,Graduate,Married,Self_Employed):
    
    df = pd.DataFrame({'Dependents': Dependents,'ApplicantIncome':ApplicantIncome,'CoapplicantIncome':CoapplicantIncome
                       ,'LoanAmount': LoanAmount,'Loan_Amount_Term':Loan_Amount_Term,'Credit_History':Credit_History
                       ,'Property_Area':Property_Area,'Gender_Male':Gender,'Education_Not Graduate':Graduate,'Married_Yes':Married
                       ,'Self_Employed_Yes':Self_Employed},index= pd.Series(1) )
    return classifier.predict(df)
print(loan_predict(1,5720,0,110,360,1,2,1,0,1,0))
def main():
    #dependent = st.number_input('Dependents',0,4)
    dependent = st.selectbox('Number of Dependent', [0,1,2,3])
    income = st.slider('Applicant Income',150,82000,4000)
    co_app_income = st.slider('Co-Applicant Income',0,42000,1200)
    loan_amt = st.slider('Loan Amount',5,130,800)
    loan_term = st.slider('Loan Term',10,480,300)
    cred_hist = st.selectbox('Credit History',[1,0])
    prop_area = st.radio('Property Area',['Rural','Semiurban','Urban'])
    if prop_area == 'Rural':
        prop_area = 0
    elif prop_area == 'Semiurban':
        prop_area = 1
    else:
        prop_area = 2
    
    gender = st.radio('Gender',['Male','Female'])
    if gender == 'Male':
        gender = 1
    else:
        gender = 0
        
    grad = st.radio('Graduate',['Graduate','Not a graduate'])
    if grad == 'Graduate':
        grad= 1
    else:
        grad = 0
        
    marr = st.radio('Marital status',['Married','Single'])
    if marr == 'Married':
        marr = 1
    else:
        marr = 0
        
    self_emp = st.radio('Are you Self Employed',['Yes','No'])
    if self_emp == 'Yes':
        self_emp =1
    else:
        self_emp = 0
    result = ''  
    if st.button('Predict'):
        result = loan_predict(dependent,income,co_app_income,loan_amt,
                              loan_term,cred_hist,prop_area,gender,
                              grad,marr,self_emp)
    st.success('The Status is {}'.format(result))
    
if __name__=='__main__':
    main()
    

import streamlit as st
import numpy as np
import pandas as pd
import pickle
with open('KNN.pkl', 'rb') as file:
    model=pickle.load(file)




st.title("Does loan be pain off?")
st.write(""" ##### Please input the parameters for the customer """)


principal=st.number_input('The amount of money borrowed', format='%f')
terms=st.number_input("Terms (repayment of money, can be weekly, monthly and so on (write in days)", format='%f')
age=st.number_input('Age', format='%f')
gender=st.selectbox("Gender", ("Male", "Female"))
weekend=st.selectbox('Did money got borrowed at the weekend?', ('Yes', 'No'))
education=st.selectbox("Education", ('Bacherlor', 'High school or below','College'))
g=1 if gender=='Female' else 0
b=0
h=0
c=0
if education=='Bachelor':
    b=1
elif education=='College':
    c=1
else:
    h=1
w=1 if weekend=="Yes" else 0
df=pd.DataFrame({'Principal':[principal],'Terms':[terms],'Age':[age],'Gender':[g], 'Weekend':[w],'Bachelor':[b], 'High school or below':[h], 'College':[c]})

if st.button('Calculate'):
    pre=model.predict(df)
    if pre[0]=="PAIDOFF":
        st.write('The borrowed money will probably be returned')
    else:
        st.write('The borrowed money will probably not be returned')





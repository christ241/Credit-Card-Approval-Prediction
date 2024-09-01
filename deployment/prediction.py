import streamlit as st
import pandas as pd
import numpy as np
import json
import pickle
from sklearn import *

with open('best_models_knc.pkl', 'rb') as file_3:
  knc_model = pickle.load(file_3)

with open('best_models_svc.pkl', 'rb') as file_6:
  svc_model = pickle.load(file_6)

with open('best_models_logreg.pkl', 'rb') as file_7:
  logreg_model = pickle.load(file_7)

def run():
    st.title('Prediction Credit Card Default or Not')

    with st.form('form_credit_card'):
       limit_balance = st.slider('Limit Balance', min_value = 0, max_value = 500000, value = 150000, help='Slide limit balance anda')
       pay_amt_1 = st.slider('Input Payment 1', min_value = 0, max_value = 300000, value = 150000, help='Slide jumlah payment pertama anda')
       pay_amt_2 = st.slider('Input Payment 2', min_value = 0, max_value = 300000, value = 150000, help='Slide jumlah payment kedua anda')
       pay_amt_3 = st.slider('Input Payment 3', min_value = 0, max_value = 300000, value = 150000, help='Slide jumlah payment ketiga anda')
       pay_amt_4 = st.slider('Input Payment 4', min_value = 0, max_value = 300000, value = 150000, help='Slide jumlah payment keempat anda')
       pay_amt_5 = st.slider('Input Payment 5', min_value = 0, max_value = 300000, value = 150000, help='Slide jumlah payment kelima anda')
       pay_amt_6 = st.slider('Input Payment 6', min_value = 0, max_value = 300000, value = 150000, help='Slide jumlah payment keenam anda')
       education_level = st.slider('Education Level', min_value = 0, max_value = 6, value = 3, help='Slide education level anda')
       pay_0 = st.slider('Input Payment 1', min_value = -2, max_value = 9, value = 3, help='Slide status payment pertama anda')
       pay_2 = st.slider('Input Payment 2', min_value = -2, max_value = 9, value = 3, help='Slide status payment kedua anda')
       pay_3 = st.slider('Input Payment 3', min_value = -2, max_value = 9, value = 3, help='Slide status payment ketiga anda')
       pay_4 = st.slider('Input Payment 4', min_value = -2, max_value = 9, value = 3, help='Slide status payment keempat anda')
       pay_5 = st.slider('Input Payment 5', min_value = -2, max_value = 9, value = 3, help='Slide status payment kelima anda')
       pay_6 = st.slider('Input Payment 6', min_value = -2, max_value = 9, value = 3, help='Slide status payment keenam anda')
       bill_amt_1 = st.slider('Input Jumlah Tagihan 1', min_value = 0, max_value = 500000, value = 150000, help='Slide jumlah tagihan pertama anda')
       bill_amt_2 = st.slider('Input Jumlah Tagihan 2', min_value = 0, max_value = 500000, value = 150000, help='Slide jumlah tagihan kedua anda')
       bill_amt_3 = st.slider('Input Jumlah Tagihan 3', min_value = 0, max_value = 500000, value = 150000, help='Slide jumlah tagihan ketiga anda')
       bill_amt_4 = st.slider('Input Jumlah Tagihan 4', min_value = 0, max_value = 500000, value = 150000, help='Slide jumlah tagihan keempat anda')
       bill_amt_5 = st.slider('Input Jumlah Tagihan 5', min_value = 0, max_value = 500000, value = 150000, help='Slide jumlah tagihan kelima anda')
       bill_amt_6 = st.slider('Input Jumlah Tagihan 6', min_value = 0, max_value = 300000, value = 150000, help='Slide jumlah tagihan keenam anda')

       #submit button
       submitted = st.form_submit_button('Predict')

    data_inf = {
    "limit_balance"  :               limit_balance,
    "pay_amt_1"      :                pay_amt_1,
    "pay_amt_2"      :                pay_amt_2,
    "pay_amt_3"      :                pay_amt_3,
    "pay_amt_4"      :                pay_amt_4,
    "pay_amt_5"      :                pay_amt_5,
    "pay_amt_6"      :                pay_amt_6,
    "education_level":          education_level,
    "pay_0"          :                   pay_0,
    "pay_2"          :                   pay_2,
    "pay_3"          :                   pay_3,
    "pay_4"          :                   pay_4,
    "pay_5"          :                   pay_5,
    "pay_6"          :                   pay_6,
    "bill_amt_1"     :               bill_amt_1,
    "bill_amt_2"     :               bill_amt_2,
    "bill_amt_3"     :               bill_amt_3,
    "bill_amt_4"     :               bill_amt_4,
    "bill_amt_5"     :               bill_amt_5,
    "bill_amt_6"     :               bill_amt_6
    }       

    data_inf = pd.DataFrame([data_inf])
    data_inf

    if submitted:

        y_pred_inf = logreg_model.predict(data_inf)
        y_pred_inf

        st.write('### Default Payment Next Month: ', str(int(y_pred_inf)))


if __name__ == "__main__":
    run()
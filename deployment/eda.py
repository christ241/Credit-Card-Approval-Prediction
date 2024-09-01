import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from PIL import Image

def run():

    #Membuat judul
    st.title('Credit Card Analysis and Prediction')

    image = Image.open('credit_card.jpeg')
    st.image(image, caption='Credit Card')

    st.markdown('------')

    #Sub judul untuk Exploratory Data Analysis
    st.subheader('Exploratory Data Analysis Credit Card')

    #Memanggil dataset
    credit_card_data = pd.read_csv('P1G5_Set_1_Christopher.csv')
    credit_card_data

    st.write("#### Penggunaan Credit Card berdasarkan Age")
    fig = plt.figure(figsize=(20, 15))
    sns.countplot(credit_card_data, x="age")
    st.pyplot(fig)

    st.write("#### Limit Balance menurut Education Level")
    limit_by_education = credit_card_data.groupby('education_level')['limit_balance'].sum().sort_values(ascending=False).reset_index()
    fig, ax = plt.subplots(figsize=(20, 10))

    ax.bar(limit_by_education.education_level, limit_by_education.limit_balance, label=limit_by_education.limit_balance)

    ax.set_ylabel('Education Level')
    ax.set_title('Limit Balance')
    ax.legend(title='Limit Balance menurut Education Level')
    st.pyplot(fig, ax)

    st.write("#### Limit Balance menurut Age")
    limit_by_age = credit_card_data.groupby('age')['limit_balance'].sum().sort_values(ascending=False).reset_index()
    fig, ax = plt.subplots(figsize=(20, 10))

    ax.bar(limit_by_age.age, limit_by_age.limit_balance)

    ax.set_ylabel('Education Level')
    ax.set_title('Limit Balance')
    ax.legend(title='Limit Balance menurut Education Level')
    st.pyplot(fig, ax)

if __name__ == "__main__":
    run()
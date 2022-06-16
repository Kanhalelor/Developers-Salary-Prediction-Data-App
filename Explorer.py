# Explorer page
import streamlit as st
import requests, zipfile, io
import pandas as pd
import matplotlib.pyplot as plt

from Helpers import clean_ed_level, clean_years_code_pro, shorten_categories

# load data
@st.cache
def load_data():
    # get survey data from stackoverflow
    url = "https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip"
    file = requests.get(url)
    zipf = zipfile.ZipFile(io.BytesIO(file.content))
    expracted_data = zipf.extractall('./')
    # read data from a csv file
    df = pd.read_csv('/content/survey_results_public.csv')
    df = df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df['Salary'].notnull()]
    df = df.dropna()
    df.isnull().sum()
    df = df[df['Employment'] == 'Employed full-time']
    df = df.drop('Employment', axis=1)

    # clean dataframe
    country_map = shorten_categories(df.Country.value_counts(), 300)
    df['Country'] = df['Country'].map(country_map)
    # keep salary cap at 2.5k
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df['Country'] != 'Other']
    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_years_code_pro)
    df['EdLevel'] = df['EdLevel'].apply(clean_ed_level)
    return df

df = load_data()

def explorer():
    st.header("Explore SWE Salaries")

    st.write("According to the Stackoverflow Developer Survey 2021")

    st.write("---")

    st.subheader("Pie Chart of Number of Developers by country.")
    data = df.Country.value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%",shadow=True, startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)

    st.write("---")
    st.subheader("Developer's Mean Salary by Country")
    data = df.groupby(['Country'])['Salary'].mean().sort_values(ascending=True)
    st.bar_chart(data)
    st.write("---")
    st.subheader("Developer's Mean Salary by Experience")
    data = df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=True)
    st.line_chart(data)

# --------------------------------------------------------------------------------------

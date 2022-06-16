# Predictions page
import streamlit as st
import numpy as np
import pickle
import pandas as pd

#load saved model
def load_saved_model():
    with open('saved_steps.pkl', 'rb') as  file:
        data = pickle.load(file)
        return data
    
data = load_saved_model()
regression_model = data['model']
label_encoded_country = data['le_country']
label_encoded_education = data['le_education']

def prediction_page():
    st.title("Stackoverflow Developer Salary Predictions")
    st.write("Using Stackoverflow's annual developer survey data, we'll build a machine \
         learning model to predict Developer salaries based on certain features in the dataset.")


    countries = ("United States of America", "India", "Germany", 
    "United Kingdom of Great Britain and Northern Ireland", "Canada"                                          
    "France", "Brazil", "Spain", "Netherlands", "Australia", "Poland", 
    "Italy", "Russian", "Federation", "Sweden", "Turkey", "Switzerland", "Israel", "Norway",
    "Mexico", "Ukraine", "Iran", "Islamic Republic of...", "Denmark", "Belgium",
    "Finland", "Austria", "Argentina", "Pakistan", "South Africa")

    education_level = ("Master’s degree", "Bachelor’s degree", "Post grad",
        "Less than a Bachelors")


    country = st.selectbox("Country", countries)

    education = st.selectbox("education Level", education_level)

    yearsOfExp =  st.slider("Years of Experience", 0, 46, 2)

    clicked = st.button("Predict Salary")

    if clicked:
        X = pd.DataFrame({"Country":[country],
                    "EdLevel": [education],
                    "YearsCodePro": [yearsOfExp]})

        X['Country'] = label_encoded_country.fit_transform(X['Country'])
        X['EdLevel'] = label_encoded_education.fit_transform(X['EdLevel'])
        X.YearsCodePro = X['YearsCodePro'].astype(float)

        salary = regression_model.predict(X)
        st.subheader(f"The predicted Salary is: {salary[0]:.2f}")
        

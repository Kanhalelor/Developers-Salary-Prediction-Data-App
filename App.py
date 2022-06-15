# main page
import streamlit as st
from Predict import prediction_page
from Explorer import explorer

current_page = st.sidebar.selectbox("Explore or Predict", ("Explorer", "Predict"))
def choice():
    if current_page == "Explorer":
        explorer()
    else:
        prediction_page()


if __name__ == '__main__':
    choice()
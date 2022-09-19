import streamlit as st
import pandas as pd
import altair as alt

def get_data():
        df = pd.read_csv("../data/relations_dev_train.csv")
        BearerID= st.multiselect(
            "BearerID", list(df.index)
        )
        st.bar_chart.head()


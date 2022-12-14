import streamlit as st
import pandas as pd
import plotly.express as px
import back

df = pd.read_csv('PA OFFICE.csv')

data = st.container()
plot = st.container()
table = st.container()

with st.sidebar:
    add_selectbox = st.selectbox(
        "Choose what you want to see",
        ("Total number of events per person", "Histogram of events by user", "Line plot by time", "All events by time with delta")
    )

    if 'Total number of events per person' in add_selectbox:
    	with data:
    		st.table(back.new_data(df))

    elif 'Histogram of events by user' in add_selectbox:
    	with plot:
    		st.write(back.plot())

    elif 'Line plot by time' in add_selectbox:
        with plot:
            st.write(back.line_plot())
    else:
        with data:
            user = st.selectbox(
                'User name',
                (back.users())
                )
            st.write('you selected user:', user)
            st.text(back.one(user))

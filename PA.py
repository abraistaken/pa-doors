import streamlit as st
import pandas as pd
import plotly.express as px
import back

df = pd.read_csv('PA OFFICE.csv')

data = st.container()
plot = st.container()

with st.sidebar:
    add_radio = st.selectbox(
        "Choose what you want to see",
        ("Total number of events per person", "Histogram", "All events by time", "Line plot by time")
    )

    if 'Total number of events per person' in add_radio:
    	with data:
    		st.table(back.new_data())

    elif 'Histogram' in add_radio:
    	with plot:
    		st.write(back.plot())

    elif 'Line plot by time' in add_radio:
        with plot:
            st.write(back.line_plot())
    else:
        with data:
            st.table(back.final())
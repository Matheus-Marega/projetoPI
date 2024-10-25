import pandas as pd
import streamlit as st


def get_chart():
    import plotly.express as px

    df = px.data.tips()
    fig = px.pie(df, values='tip', names='sex', color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout(template="seaborn")

    st.plotly_chart(fig)
    

def get_chart_2():
    import plotly.express as px

    df = px.data.tips()
    fig = px.bar(df, x="sex", y="total_bill", color='time')

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)

def get_chart_3():
    import plotly.express as px

    df = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(df, x='year', y='pop',
                 labels={'pop':'population of Canada'}, height=400)

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit")
    with tab2:
        st.plotly_chart(fig, theme=None)
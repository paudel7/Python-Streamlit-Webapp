import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.title ("Projects")
st.subheader(":blue[Earthquake Data Explorer] :sunglasses:")
st.text('Get ready for exploring Earthquake Data')

def home(uploaded_file):
    if uploaded_file:
        st.header('Use Navigation for Exploring Data')
    
def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data')

#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select one to display:', ['Home', 'Data Summary','Data Header', 
                                                      'Scatter Plot','Charting'])
# Check if file has been uploaded
if upload_file is not None:
    def load_data(nrows):
        df = pd.read_csv(upload_file)
        return df
else:
    df = pd.read_csv('database.csv')
        #df = load_data(100)

if st.checkbox("Show Raw Data",False):
    st.subheader('Raw Data')
    st.write(df)

# Data Showcasing

# map
lowercase = lambda x: str(x).lower()
df.rename(lowercase, axis='columns', inplace=True)
magnitude_measured = st.slider("Magnitude of Earthquake", 5, 9)
st.map(df.query("magnitude >= @magnitude_measured")[["latitude","longitude"]].dropna(how="any"))


# Define a function to display a bar chart or column chart
def display_chart(df, chart_type):
    if chart_type == 'bar':
        chart = alt.Chart(df).mark_bar().encode(
            x='date:T',
            y='magnitude:Q',
            tooltip=['date:T', 'magnitude:Q']
        ).properties(
            width=600,
            height=400,
            title='Earthquake Magnitude by Date (Bar Chart)'
        )
    elif chart_type == 'column':
        chart = alt.Chart(df).mark_bar().encode(
            x='date:T',
            y='magnitude:Q',
            tooltip=['date:T', 'magnitude:Q']
        ).properties(
            width=600,
            height=400,
            title='Earthquake Magnitude by Date (Column Chart)'
        ).configure_mark(
            opacity=0.5
        )
    # Show the chart
    st.altair_chart(chart)
# Ask the user which chart type they want to display
chart_type = st.selectbox("Select Chart Type", ['bar', 'column'])


def displayplot():
    st.header('Plot of Data')
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['depth'], y=df['magnitude'])
    ax.set_xlabel('depth')
    ax.set_ylabel('magnitude')

    st.pyplot(fig)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Scatter Plot':
    displayplot()
elif options == 'Charting':
    display_chart(df, chart_type)
    

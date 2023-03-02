import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title ("Projects")
st.subheader(":blue[Earthquake Data Explorer] :sunglasses:")
st.text('Get ready for exploration of Earthquake Data')
#new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
#st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')

#st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Use Navigation for Exploring Data')
    else:
        st.header('To begin upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())


def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot():
    st.header('Plot of Data')

    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data')
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Charting', 'Data Header', 'Scatter Plot'])

# Check if file has been uploaded
if upload_file is not None:
    def load_data(nrows):
        df = pd.read_csv(upload_file)
        return df
df = load_data(100)


if st.checkbox("Show Raw Data",False):
    st.subheader('Raw Data')
    st.write(df)

# Data Showcasing
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE','CRASH_TIME']])
#     data.dropna(subset=['LATITUDE','LONGITUDE'], inplace=True)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data.rename(columns={'crash_date_crash_time': 'date/time'},inplace=True)
#     return data
# # data = load_data(100)

# charting ==NOT WORKING PROPERLY
def charting():
    st.header('Charting')
    chart_data = pd.DataFrame(
    #np.random.randn(20, 3),
    #columns=[x = df['Date'], y = df['Magnitude']]
    columns = ['Date', 'Magnitude']
    x, y = df[columns]
    st.bar_chart(columns)

# map
lowercase = lambda x: str(x).lower()
df.rename(lowercase, axis='columns', inplace=True)
magnitude_measured = st.slider("Magnitude of Earthquake", 5, 9)
st.map(df.query("magnitude >= @magnitude_measured")[["latitude","longitude"]].dropna(how="any"))

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
    charting()


def displayplot():
    st.header('Plot of Data')

    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)

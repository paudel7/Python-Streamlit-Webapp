import PIL
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="My Webpage", page_icon=":tada:", layout = "wide"
)

with st.container():
    #st.write("---")
    left_col1, right_col1, right_col2,right_col3,right_col4 = st.columns(5)

    right_col4.metric(label = "Temp.", value = "1 deg.celc", delta = "5 deg.celc.")
    left_col1.title("Main Page")
    st.sidebar.success("Select a page above")
    st.sidebar.title("Navigation")
#For more emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

#Loading Assets
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

#Load Assets
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")
lottie_coding1 = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_qxdvwwgs.json")
#images
img_tableau = PIL.Image.open("images/tableauProj_1.png")
img_powerBI = PIL.Image.open("images/incomeStat_PowerBI.png")

#Header
#Container for organizing
with st.container():
    st.subheader("Hi, I am dD :wave:")
    st.title("A Business Analyst from Canada")
    st.write("I am passionate about finding ways for business problems towards data or productivity tools")
    st.write("[Want to learn more? >](https://paudel7.mystrikingly.com)")

#Another para
with st.container():
    st.write("---")
    left_column, right_column1, right_column2 = st.columns(3)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("I am an expert in grant financial management with experience in Business Analysis and skills in Business Intelligence/Data Analysis")
        with st.expander("Click to read more..."):
            st.write(
                """
                I am an experienced financial management professional:
                    - expertise in grant financial management
                    - expertise in data analysis with excel, google sheet and python
                    - expertise in Business Intelligence Analysis
                    - skills in Business Analysis-requirements gathering,use case,process flow modelling etc
                    - expertise in VBA Macro and App Scripting for automating tasks

                Should there be anything that interests you, consider emailing me, will provide the link at the bottom of the page
                """
                )
        st.write("[Some visual snaps of my projects here>](https://public.tableau.com/app/profile/paudel7)")

    with right_column2:
        uploaded_photo = right_column2.file_uploader("Upload Your Picture")
        camera_photo = right_column2.camera_input("Take Picture")
        right_column2.success("Picture uploaded successfully")

    with right_column1:
        st_lottie(lottie_coding, height = 300, key = "coding")
        #how to use two obj here?
        #st_lottie1 = new st_lottie
        #st_lottie1(lottie_coding1, height = 300, key = "coding")



#Showcasing projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
    #inserting images
        st.image(img_tableau)
        st.image(img_powerBI)

    with text_column:
    #inserting text
        st.subheader(" Project Title - 'Most Popular Ride Stations: Tableau Dashboard' ")
        st.write(
        """
        Project Description -1

        """
    )
        st.markdown("[Full link]>(https://public.tableau.com/app/profile/paudel7/viz/MostPopularRideStations/May212020)")

    #pillow installed after this

with st.container():

    image_column,text_column = st.columns((1,2))
    with image_column:
    #inserting images
        #st.image(img_powerBI)
    with text_column:
    #inserting text
        st.subheader(" The Project Title - 2")
        st.write(
        """
        Project Description - 2

        """
    )
        st.markdown("[Full link]>(https://github.com/paudel7)")

#Contact
with st.container():
    st.write("---")
    st.header("Let's get in touch !")
    st.write("##")
    #https://formsubmit.co if we need fully functional contact format

    contact_form = """
    <form action="https://formsubmit.co/ddaemon2023@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name = "message" placeholder="Your Message Here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

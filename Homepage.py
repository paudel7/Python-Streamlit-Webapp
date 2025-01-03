import PIL
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from datetime import datetime

st.set_page_config(
    page_title="Kiran's Streamlit Webpage", page_icon=":tada:", layout = "wide"
)

# Function to get current temperature and feels like temperature by location
def get_temperature(location):
    api_key = "a8f64ad9ea821df9706a8244914ecb74"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + location + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if response.status_code == 200 and "main" in data:
        main = data["main"]
        temperature = main["temp"]
        feels_like = main["feels_like"]
        return temperature, feels_like
    else:
        return None, None

with st.container():
    st.title("Welcome to Kiran's Streamlit Webpage !")
    #st.write("---")
    left_col1, right_col1, right_col2, right_col3, right_col4 = st.columns(5)

    with right_col1:
        location = st.selectbox("Select Location", ["Toronto", "Waterloo", "New York", "London", "Tokyo", "Sydney", "Kathmandu"])  # Add more locations as needed
    temperature, feels_like = get_temperature(location)
    if temperature is not None and feels_like is not None:
        right_col4.metric(label=f"Temp. in {location}", value=f"{temperature} °C", delta=f"Feels like {feels_like} °C")
    else:
        right_col4.metric(label=f"Temp. in {location}", value="N/A")

    with right_col2:
        # Show today's date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"Today's date and time: {current_datetime}")

    #left_col1.title("Main Page")
    st.sidebar.success("Select a page above")
    st.sidebar.title("Navigation")
# For more emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

# Loading Assets
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

# Load Assets
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")
lottie_coding1 = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_qxdvwwgs.json")
# images
img_tableau = PIL.Image.open("images/tableauProj_1.png")
img_powerBI = PIL.Image.open("images/incomeStat_PowerBI.png")

# Add a selection box for Lottie animations
animation_choice = st.sidebar.selectbox(
    "Choose an animation",
    ("Coding Animation", "Another Animation")
)

# Header
# Container for organizing
with st.container():
    st.subheader("Hi, I am Kiran 👋")
    st.markdown("""
        <div style="text-align: justify;">
            <h2>A Business Analyst from Canada</h2>
            <p>I am passionate about identifying and implementing data-driven solutions and productivity tools to address business challenges.</p>
            <p><a href="https://paudel7.mystrikingly.com" target="_blank" style="color: #1f77b4; text-decoration: none;">Want to learn more? ></a></p>
        </div>
    """, unsafe_allow_html=True)

# Another para
with st.container():
    st.write("---")
    left_column, right_column1, right_column2 = st.columns(3)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.markdown("""
            <div style="text-align: justify;">
                <p>I am an expert in grant financial management, with extensive experience in business analysis and a strong skill set in business intelligence and data analysis.</p>
            </div>
        """, unsafe_allow_html=True)
        with st.expander("Click to read more..."):
            st.markdown("""
                <div style="text-align: justify;">
                    <ul>
                        <li>Expertise in grant financial management</li>
                        <li>Expertise in data analysis with Excel, Google Sheets, and Python</li>
                        <li>Expertise in Business Intelligence Analysis</li>
                        <li>Skills in Business Analysis - requirements gathering, use case, process flow modeling, etc.</li>
                        <li>Expertise in VBA Macro and App Scripting for automating tasks</li>
                    </ul>
                    <p>Should there be anything that interests you, consider emailing me. I will provide the link at the bottom of the page.</p>
                </div>
            """, unsafe_allow_html=True)
        
        st.write("##")
        st.header("Featured Projects")
        project_desc_col, project_link_col = st.columns([4, 1])
        with project_desc_col:
            project_description = st.text_area("Project Description", height=100)
        with project_desc_col:
            project_link = st.selectbox(
                "Select a Project",
                [
                    "Most Popular Ride Stations: Tableau Dashboard",
                    "Income Statement Analysis: Power BI",
                    "Excel Dashboard",
                    "SQL Data Development",
                    "R Analysis",
                    "Python Streamlit Project"
                ]
            )
            project_links = {
                "Most Popular Ride Stations: Tableau Dashboard": [
                    "https://public.tableau.com/app/profile/paudel7/viz/MostPopularRideStations/May212020"
                ],
                "Income Statement Analysis: Power BI": [
                    "https://public.tableau.com/app/profile/paudel7/viz/IncomeStatementAnalysis/IncomeStatement"
                ],
                "Excel Dashboard": [
                    "https://public.tableau.com/app/profile/paudel7/viz/ExcelDashboard/ExcelDashboard"
                ],
                "SQL Data Development": [
                    "#"
                ],
                "R Analysis": [
                    "#"
                ],
                "Python Streamlit Project": [
                    "#"
                ]
            }
            for link in project_links.get(project_link, []):
                st.markdown(f"[View Project]({link})")

    with right_column2:
        uploaded_photo = right_column2.file_uploader("Upload Your Picture")
        camera_photo = right_column2.camera_input("Take Picture")
        if uploaded_photo is not None:
            st.image(uploaded_photo, width=150)
            right_column2.success("Picture uploaded successfully")
        elif camera_photo is not None:
            st.image(camera_photo, width=150)
            right_column2.success("Picture uploaded successfully")

    with right_column1:
        if animation_choice == "Coding Animation":
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st_lottie(lottie_coding1, height=300, key="coding1")

# Showcasing projects
with st.container():
    st.write("---")
    st.header("My Projects")
    
    st.write("##")
    # Add a dropdown to select project category and subcategory side by side
    category_col, subcategory_col = st.columns(2)
    with category_col:
        project_category = st.selectbox(
            "Select Project Category",
            ("Excel", "SQL", "R", "Tableau", "Power BI", "Python")
        )

    with subcategory_col:
        project_subcategory = None
        if project_category == "Excel":
            project_subcategory = st.selectbox(
                "Select Subcategory",
                ("Dashboard", "Pivot", "VBA")
            )
        elif project_category == "SQL":
            project_subcategory = st.selectbox(
                "Select Subcategory",
                ("Data Development", "ETL", "Analysis", "Reporting")
            )
        elif project_category == "R":
            project_subcategory = st.selectbox(
                "Select Subcategory",
                ("Analysis", "Visualization")
            )
        elif project_category == "Tableau":
            project_subcategory = st.selectbox(
                "Select Subcategory",
                ("SQL & Tableau", "Excel & Tableau")
            )
        elif project_category == "Power BI":
            project_subcategory = st.selectbox(
                "Select Subcategory",
                ("SQL & Power BI", "Excel & Power BI")
            )
        elif project_category == "Python":
            project_subcategory = st.selectbox(
                "Select Subcategory",
                ("Python Only", "Streamlit Python", "tKinter Python")
            )

    st.write("##")
    # Placeholder for default demo image for each category
    if project_category == "Excel":
        st.image("default_image/default_R_image_2yrs'MOM.jpg", width=300)
    elif project_category == "SQL":
        st.image("default_image/default_R_image_2yrs'MOM.jpg", width=300)
    elif project_category == "R":
        st.image("default_image/default_R_image_2yrs'MOM.jpg", width=300)
    elif project_category == "Tableau":
        st.image("default_image/default_Tableau_image_exedash.jpg", width=300)
    elif project_category == "Power BI":
        st.image("default_image/default_R_image_2yrs'MOM.jpg", width=300)
    elif project_category == "Python":
        st.image("default_image/default_R_image_2yrs'MOM.jpg", width=300)

    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        if project_subcategory:
            subcategory_cleaned = project_subcategory.lower().replace(' ', '_').replace('&', 'and')
            image_path = f"images/{subcategory_cleaned}_{project_category.lower()}.jpg"
            st.subheader(f" Project Title - '{project_subcategory} {project_category}' ")
            st.image(image_path, width=300)
    with text_column:
        if project_subcategory:
            if project_category == "Tableau":
                st.write(
                    """
                    Project Description -1
                    """
                )
                st.markdown("[Full link](https://public.tableau.com/app/profile/paudel7/viz/MostPopularRideStations/May212020)")
            elif project_category == "SQL":
                st.write("SQL Project Description")
                st.markdown("[Full link 1](#)")
                st.markdown("[Full link 2](#)")
                st.markdown("[Full link 3](#)")
            elif project_category == "R":
                st.write("R Project Description")
                st.markdown("[Full link 1](#)")
                st.markdown("[Full link 2](#)")
                st.markdown("[Full link 3](#)")

# Contact
with st.container():
    st.write("---")
    st.header("Let's get in touch !")
    st.write("##")
    st.markdown("You can reach me at [kiran1.paudel2@gmail.com](mailto:kiran1.paudel2@gmail.com)")
    st.markdown("Alternatively, you can fill out the [contact form](3_Contact) to get in touch.")

import streamlit as st
st.set_page_config(page_title="TechWillxOlympics", layout="wide",initial_sidebar_state="collapsed")
from streamlit_navigation_bar import st_navbar
import pages as pg
import time
from pages.security_login import update_visitor_count

#from pages.security_login import basic_stats, update_visitor_count
st.logo("logo.gif")
st.markdown("""
            <style>
            .stLogo {
                width: 50px;
                height: 50px;
            }
            </style>
            """, unsafe_allow_html=True)
pages = ["Home", "Dataset", "Information", "Prediction", "Chatbot", "Tutorial", "Aakash"]
#logo_path = ("logo.svg")
urls = {"Aakash": "https://linkedin.com/in/aakash-kharb"}
options={"use_padding": False, "show_menu":False}

styles = {
    "nav": {
        "background-color": "#FCB131",  # Background color of the navigation bar
        "height": "4rem",  # Set the total height of the navigation bar
        "display": "flex",  # Use flexbox for layout
        "align-items": "center",  # Vertically center the items
        "justify-content": "space-around",  # Spread out the headings evenly
        "padding": "0 1rem",  # Add padding to the left and right of the navigation bar
        "overflow-x": "auto",  # Enable horizontal scrolling if the content overflows
        "white-space": "nowrap",  # Prevent items from wrapping to a new line
    },
    "div": {
        "max-width": "72rem",  # Limit the maximum width of the navigation bar content
    },
    "span": {
        "border-radius": "0.5rem",  # Rounded corners for the headings
        "color": "rgb(49, 51, 63)",  # Text color of the headings
        "margin": "0 0.125rem",  # Margin around each heading
        "padding": "0.4375rem 0.625rem",  # Padding inside each heading
        "font-size": "1.1rem",  # Increase the font size of the headings
        "font-weight": "bold",  # Make the headings bold
        "text-transform": "uppercase",  # Convert heading text to uppercase
    },
    "active": {
        "background-color": "rgba(252, 177, 49, 0.35)",  # Background color for the active heading
    },
    "hover": {
        "background-color": "rgba(252, 177, 49, 0.35)",  # Background color on hover
    },
}

# Inject custom CSS for mobile responsiveness
st.markdown("""
    <style>
        /* Mobile responsiveness */
        @media (max-width: 900px) {
            .stNavBar-nav {
                overflow-x: scroll;  /* Enable scrolling on smaller screens */
                flex-wrap: nowrap;    /* Prevent wrapping of items */
                padding: 0.5rem;      /* Adjust padding for mobile */
            }
            .stNavBar-span {
                font-size: 0.9rem;      /* Slightly reduce font size for mobile */
            }
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("""<style>.stApp {padding-top: 6rem !important;}</style>""", unsafe_allow_html=True)
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"  # Default to Home page on first load
page = st_navbar(pages, urls=urls, styles=styles, options=options) #logo_path=logo_path

if page != st.session_state.current_page:
    st.session_state.current_page = page

#visitor
if 'first_access' not in st.session_state:
    st.session_state.first_access = True
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 0
if 'display_count' not in st.session_state:
    st.session_state.display_count = True

if st.session_state.first_access:
    st.session_state.visitor_count = update_visitor_count()

if st.session_state.display_count:
    st.toast(f"Visitor Count : {st.session_state.visitor_count}")
    st.session_state.display_count = False

if st.sidebar.button("Site Stats",use_container_width=True):
    visitor_count = update_visitor_count()
    st.sidebar.subheader(f"Total Visitors : {visitor_count}")
    st.toast(f"Total visitors: {visitor_count}")

#st.sidebar.markdown("---")  # Adds a separator
st.markdown(
    """
    <style>
        .sidebar-button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            color: black;
            background-color: rgba(252,178,49,1); /* Orange */
            border: 2px solid #000000;
            border-radius: 15px;
            cursor: pointer;
            margin-bottom: 5px;
            text-align: center;
            display: block;
            text-decoration: none; /* Remove underline */
            transition: all 0.3s ease;
        }

        .sidebar-button:hover {
            background-color: rgba(0,0,0,1); /* Darker red */
            border-color: rgba(252,178,49,1)
            color: rgba(255,255,255,1)
        }

        .sidebar-button:hover {
            text-decoration: none; /* Ensure no underline on hover */
            color: rgba(255,255,255,1)
        }
    </style>
    """,
    unsafe_allow_html=True,
)

olympics_resources = {
    "Olympics Official Website": "https://olympics.com",
    "IOC (International Olympic Committee)": "https://olympic.org",
    "Olympic Database": "https://www.olympicdatabase.com",
    "Olympic Channel": "https://www.olympicchannel.com",
    "Tokyo 2020 Official Website": "https://tokyo2020.org/en",
    "Paris 2024 Official Website": "https://www.paris2024.org/en",
    "LA 2028 Official Website": "https://la28.org",
    "Olympic Museum": "https://www.olympic.org/museum",
    "World Anti-Doping Agency (WADA)": "https://www.wada-ama.org",
    "Athletes Commission (IOC)": "https://olympics.com/ioc/athletes-commission",
    "International Paralympic Committee (IPC)": "https://www.paralympic.org",
    "Sports Illustrated – Olympics Coverage": "https://www.si.com/olympics",
    "Olympic History & Results": "https://www.sports-reference.com/olympics"
}

st.sidebar.title("Important Resources")
for name, link in olympics_resources.items():
    st.sidebar.markdown(
    f'<a href="{link}" target="_blank" style="text-decoration: none;" class="sidebar-button">{name}</a>',
    unsafe_allow_html=True)
    
functions = {
    "Home": pg.home_page,
    "Dataset": pg.dataset_page,
    "Information": pg.info_page,
    "Prediction": pg.predict_page,
    "Chatbot": pg.chat_page,
    "Tutorial": pg.tutorial_page
}

go_to = functions.get(st.session_state.current_page)
if go_to:
    go_to()

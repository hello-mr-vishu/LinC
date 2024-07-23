
import os
import json
import streamlit as st
import openai
import webbrowser

# Set Streamlit page configuration as the first command
st.set_page_config(
    page_title="Bujji",
    page_icon="💬",
    layout="centered"
)

# Define URLs for navigation
home_page_url = 'http://127.0.0.1:5000/#'
ats_page_url = 'http://127.0.0.1:5000/ats'
resume_builder_url = 'http://127.0.0.1:5000/resume'


# Add a sidebar with navigation buttons and title
st.sidebar.markdown("""
    <style>
   
    .sidebar-content {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 30px; /* Adjust margin as needed */
    }
    

    .sidebar-icon {
        margin-right: 10px; 
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar title and navigation buttons
st.sidebar.markdown('<h1 class="sidebar-content"><span class="sidebar-icon"></span>ResumeAI</h1>', unsafe_allow_html=True)

button_style = """
    <style>
    .stButton > button {
        height: 50px;
        width: 250px;
        font-size: 16px;
    }
    </style>
"""

# Inject the button style into the sideb
st.sidebar.markdown(button_style, unsafe_allow_html=True)

# Navigation buttons
if st.sidebar.button('🏠 Home Dashboard'):
    webbrowser.open(home_page_url)

if st.sidebar.button('📊 Application Tracker'):
    webbrowser.open(ats_page_url)

if st.sidebar.button('📄 Resume Builder'):
    webbrowser.open(resume_builder_url)


# Configuring OpenAI API key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))

OPENAI_API_KEY = config_data['OPENAI_API_KEY']
openai.api_key = OPENAI_API_KEY

# Initialize chat session in Streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Page title
st.title("🤖 Bujji")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user's message
user_prompt = st.chat_input("Job queries")

if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Send user's message to GPT-3.5 and get a response
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are an expert assistant specializing in job opportunities, resume building, career advice, and educational qualifications. Provide detailed and relevant information on these topics only."},
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message["content"]
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # Display GPT-3.5's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)

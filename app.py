

# Importing the necessary modules from the Streamlit and LangChain packages
import streamlit as st
from langchain.llms import OpenAI
import random

placeholders = ["Ask any question", "Type your message", "Say something", "What's on your mind?"]
# Setting the title of the Streamlit application
st.title('Clever GPT App')

# Creating a sidebar input widget for the OpenAI API key, input type is password for security
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Creating a sidebar input widget for the OpenAI API key, input type is password for security
st.sidebar.text_input('Welcome to Clever GPT', type='default', placeholder=random.choice(placeholders), key='name')
st.sidebar.image('ai.png', caption='Sunrise by the mountains')
st.balloons()

# Defining a function to generate a response using the OpenAI model
def generate_response(input_text):
    # Initializing the OpenAI model with a specified temperature and API key
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    # Displaying the generated response as an informational message in the Streamlit app
    st.info(llm(input_text))

# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input with a default prompt
    text = st.text_area('Enter text:', '', placeholder=random.choice(placeholders), key='text')
    # Adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    # Displaying a warning if the entered API key does not start with 'sk-'
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    # If the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)



 #streamlit run app.py

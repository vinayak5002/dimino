import streamlit as st
import requests
import time

# Define the API URL
api_url = "https://co7d6ntic7.execute-api.us-east-1.amazonaws.com/test/fetchLoadSonic"

# Create a function to fetch data from the API
def fetch_data():
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            st.error(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

# Create a title for the Streamlit app
st.title('DIMINO DETECTOR 1.0')

# Add a horizontal line to partition the content
st.markdown("<hr>", unsafe_allow_html=True)

# Create two columns to split the UI
col1, col2 = st.columns(2)

# Add content to the left column
with col1:
    st.header('LOAD CELL')
    load_cell_depletion_rate = st.empty()
    pl1 = st.empty()
    load_cell_time = st.empty()

# Add content to the right column
with col2:
    st.header('ULTRASONIC')
    ultrasonic_depletion_rate = st.empty()
    pl2 = st.empty()
    ultrasonic_time = st.empty()

# Continuously update the values
while True:
    data = fetch_data()
    if data:
        load_cell_depletion_rate.subheader('depletion rate:')
        load_cell_depletion_rate.header(data.get('load'))
        pl1.header('Predicted time:')
        load_cell_time.subheader("coming soon")

        ultrasonic_depletion_rate.subheader('depletion rate:')
        ultrasonic_depletion_rate.header(data.get('distance'))
        pl2.header('Predicted time:')
        ultrasonic_time.subheader("coming soon")

    time.sleep(2)  # Update every 5 seconds
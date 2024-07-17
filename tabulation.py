import streamlit as st

# Page Title
st.title('Learning Needs Analysis - eLearning Preferences')

# Input fields
full_name = st.text_input('Full Name')
current_position = st.text_input('Current Position (Write in full including parenthetical, if any)')
office_agency = st.text_input('Office/Agency (Write in full, including Region and Field, if any)')
position_level = st.selectbox('Position Level', ['1st Level', '2nd Level Non-Supervisory', 'Supervisory', 'Managerial'])
province = st.text_input('Province')
device = st.selectbox('Device Used for e-Learning', ['Computer/Laptop', 'Tablet', 'Smartphone'])
learning_mode = st.selectbox('Preferred Learning Mode', ['Synchronous Face-to-Face', 'Asynchronous', 'Blended'])

# Submit button
if st.button('Save'):
    st.write("Full Name:", full_name)
    st.write("Current Position:", current_position)
    st.write("Office/Agency:", office_agency)
    st.write("Position Level:", position_level)
    st.write("Province:", province)
    st.write("Device Used for e-Learning:", device)
    st.write("Preferred Learning Mode:", learning_mode)
    st.success('Information saved successfully!')

if st.button('Reset'):
    st.caching.clear_cache()
    st.experimental_rerun()

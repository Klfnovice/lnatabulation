import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

# Set background color for the main window and justify the title
st.markdown(
    """
    <style>
    .reportview-container {
        background: linear-gradient(to bottom, #87CEEB, #FFFFFF);
        position: relative;
    }
    .title {
        text-align: justify;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set background color for the sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background: #000080;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define usernames and passwords
users = {
    "admin": "password1",
    "dmantiado": "hrlcwd2024",
    "user2": "password3"
}

# Function for user authentication
def authenticate(username, password):
    return username in users and users[username] == password

# Function to store data in an Excel file
def store_data_to_excel(df, file_name):
    df.to_excel(file_name, index=False)

# Function to store data in a CSV file
def store_data_to_csv(df, file_name):
    df.to_csv(file_name, index=False)

# Function to create table in SQLite database if it doesn't exist
def create_table_if_not_exists(table_name):
    conn = sqlite3.connect("competencies.db")
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS [{table_name}] (CURRENT_COMPETENCIES_IDENTIFIED TEXT, Basic INTEGER, Intermediate INTEGER, Advanced INTEGER, Superior INTEGER, Not_yet_Acquired INTEGER)")
    conn.commit()
    conn.close()

# Function to retrieve data from SQLite database
def retrieve_data_from_database(table_name):
    create_table_if_not_exists(table_name)  # Ensure table exists
    conn = sqlite3.connect("competencies.db")
    df = pd.read_sql(f"SELECT * FROM [{table_name}]", conn)
    conn.close()
    return df

# Function to check file extension
def check_file_extension(file_name, extension):
    return os.path.splitext(file_name)[1] == extension

# Initialize session state if not initialized
if "username" not in st.session_state:
    st.session_state.username = None
    st.session_state.page = None  # Initialize page variable
    st.session_state.competency_data = {"Current_Competencies": pd.DataFrame(),
                                        "Developmental_Competencies": pd.DataFrame()}

# Load uploaded data from file
def load_uploaded_data(competency_type):
    return st.session_state.competency_data[competency_type]

# Add heading title to login page
st.title("LCWD Human Resource Section LNA Tabulation")

# Authentication form if user hasn't logged in
if st.session_state.username is None:
    login_form = st.form("login_form")
    login_form.write("### Login")
    username = login_form.text_input("Username")
    password = login_form.text_input("Password", type="password")
    submit_button = login_form.form_submit_button("Submit")

    # Directly authenticate the user
    if submit_button:
        if authenticate(username, password):
            st.session_state.username = username
            st.success("Login successful!")
            login_form.empty()  # Clear login form
        else:
            st.error("Authentication failed. Please check your username and password.")

# Logout if requested
if st.session_state.username is not None:
    st.write(f"Logged in as: {st.session_state.username}")

    # Check if the user is an admin
    is_admin = st.session_state.username == "admin"

    # Display navigation options for users
    if not is_admin:
        competency_type = st.sidebar.radio("Navigation", ["Current_Competencies", "Developmental_Competencies"])
        st.write(f"You are viewing: {competency_type}")
        uploaded_data = retrieve_data_from_database(competency_type)

        if uploaded_data is not None and not uploaded_data.empty:
            st.write("Tabulation Table:")
            st.write(uploaded_data, index=False)  # Display DataFrame without row numbers

            # Display uploaded file as column chart
            selected_columns = st.multiselect("Select columns to display", uploaded_data.columns)
            if selected_columns:
                selected_data = uploaded_data[selected_columns]
                st.bar_chart(selected_data)

    else:
        st.session_state.page = st.sidebar.radio("For Uploading", ["Current_Competencies", "Developmental_Competencies"])
        uploaded_data = st.session_state.competency_data.get(st.session_state.page)

        # Upload CSV file if the user is an admin
        if st.session_state.page is not None:
            uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel File", type=["csv", "xlsx"])

            # Process the uploaded file if exists
            if uploaded_file is not None:
                if uploaded_file.name.endswith('csv'):
                    df = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith('xlsx'):
                    df = pd.read_excel(uploaded_file)
                else:
                    st.error("File format not supported. Please upload a CSV or Excel file.")
                    df = None

                if df is not None:
                    st.session_state.competency_data[st.session_state.page] = df  # Store uploaded data

                    # Store uploaded data in SQLite database
                    conn = sqlite3.connect("competencies.db")
                    df.to_sql(st.session_state.page, conn, if_exists="replace", index=False)  # Add index=False here
                    conn.close()

                    uploaded_data = df  # Update uploaded data for display

                    st.success("File uploaded successfully!")

        # Display uploaded file content based on selected radio button
        if uploaded_data is not None and not uploaded_data.empty:
            st.write("Uploaded Data:")
            st.write(uploaded_data, index=False)  # Display DataFrame without row numbers

            # Display uploaded file as column chart
            st.write("Column chart of uploaded data:")
            selected_columns = st.multiselect("Select columns to display", uploaded_data.columns)
            if selected_columns:
                selected_data = uploaded_data[selected_columns]
                st.bar_chart(selected_data)

# Render logout button in sidebar
if st.session_state.username is not None:
    if st.sidebar.button("Logout"):
        st.session_state.username = None
        st.session_state.page = None
        st.session_state.clear()  # Clear session state
        st.experimental_rerun()  # Rerun the app to reset everything

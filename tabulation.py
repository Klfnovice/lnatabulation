import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import os

# URL of the logo image in your GitHub repository
logo_url = "https://raw.githubusercontent.com/Klfnovice/lnatabulation/main/lcwd%20logo.png?token=GHSAT0AAAAAACTIRZDV7W6H5NX7VZGDEZ44ZTCKAOA"

# Add the logo and title with a border using HTML and CSS
st.markdown(f"""
    <div style="text-align: center;">
        <img src="{logo_url}" width="100" alt="Logo">
        <h1>
            Human Resource Section LNA/IDP Tabulation
        </h1>
    </div>
    """, unsafe_allow_html=True)

# Set background color for the sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background: #000080;
        color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define usernames and passwords
users = {
    "admin": "pass123",
    "dmantiado": "hrlcwd2024",
    "user1": "password1"
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
    cursor.execute(f"CREATE TABLE IF NOT EXISTS [{table_name}] (COMPETENCIES_IDENTIFIED TEXT, Basic INTEGER, Intermediate INTEGER, Advanced INTEGER, Superior INTEGER, Not_yet_Acquired INTEGER)")
    conn.commit()
    conn.close()

# Function to retrieve data from SQLite database
def retrieve_data_from_database(table_name):
    create_table_if_not_exists(table_name)  # Ensure table exists
    conn = sqlite3.connect("competencies.db")
    df = pd.read_sql(f"SELECT * FROM [{table_name}]", conn)
    conn.close()
    if 'CURRENT COMPETENCIES IDENTIFIED' in df.columns:
        df.set_index('CURRENT COMPETENCIES IDENTIFIED', inplace=True)
    elif 'DEVELOPMENTAL COMPETENCIES IDENTIFIED' in df.columns:
        df.set_index('DEVELOPMENTAL COMPETENCIES IDENTIFIED', inplace=True)
    return df

# Initialize session state if not initialized
if "username" not in st.session_state:
    st.session_state.username = None
    st.session_state.page = None  # Initialize page variable
    st.session_state.competency_data = {"Current_Competencies": pd.DataFrame(),
                                        "Developmental_Competencies": pd.DataFrame()}

# Load uploaded data from file
def load_uploaded_data(competency_type):
    return st.session_state.competency_data[competency_type]

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
            st.experimental_rerun()  # Refresh the app after login to load the authenticated view
        else:
            st.error("Authentication failed. Please check your username and password.")
else:
    # Display navigation options for users
    if st.session_state.username != "admin":
        competency_type = st.sidebar.radio("Navigation", ["Current_Competencies", "Developmental_Competencies"])
        st.write(f"You are viewing: {competency_type}")
        uploaded_data = retrieve_data_from_database(competency_type)
        if uploaded_data is not None and not uploaded_data.empty:
            st.write("Tabulation Table:")
            st.write(uploaded_data)  # Display DataFrame without row numbers
            # Display uploaded file as column chart
            selected_columns = st.multiselect("Select level of competency to display in chart", uploaded_data.columns)
            if selected_columns:
                selected_data = uploaded_data[selected_columns]

                # Example of using matplotlib for customized plots
                if st.button("Show Chart"):
                    fig, ax = plt.subplots(figsize=(20, 10))  # Adjust the figure size
                    selected_data.plot(kind='bar', ax=ax)
                    title = competency_type.replace("_", " ").title() + " Identified"  # Dynamically set the title
                    ax.set_title(title, pad=20, fontsize=16)  # Add title above the chart with specified font size
                    ax.set_xlabel("")  # Remove x-axis label from the bottom
                    ax.set_xticklabels(selected_data.index, rotation=45, ha='right', fontsize=12)  # Rotate and align x-tick labels
                    ax.legend(fontsize=14)  # Adjust the legend font size
                    st.pyplot(fig)
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
                    if 'CURRENT COMPETENCIES IDENTIFIED' in df.columns:
                        df.set_index('CURRENT COMPETENCIES IDENTIFIED', inplace=True)
                    elif 'DEVELOPMENTAL COMPETENCIES IDENTIFIED' in df.columns:
                        df.set_index('DEVELOPMENTAL COMPETENCIES IDENTIFIED', inplace=True)
                    st.session_state.competency_data[st.session_state.page] = df  # Store uploaded data

                    # Store uploaded data in SQLite database
                    conn = sqlite3.connect("competencies.db")
                    df.to_sql(st.session_state.page, conn, if_exists="replace")  # Remove index=False here
                    conn.close()

                    uploaded_data = df  # Update uploaded data for display
                    st.success("File uploaded successfully!")

        # Display uploaded file content based on selected radio button
        if uploaded_data is not None and not uploaded_data.empty:
            st.write("Uploaded Data:")
            st.dataframe(uploaded_data)  # use st.dataframe instead of st.write
            # Display uploaded file as column chart
            selected_columns = st.multiselect("Select level of competency to display in chart", uploaded_data.columns)
            if selected_columns:
                selected_data = uploaded_data[selected_columns]
                st.bar_chart(selected_data)

                # Example of using matplotlib for customized plots
                if st.button("Show Chart"):
                    fig, ax = plt.subplots(figsize=(20, 10))  # Adjust the figure size
                    selected_data.plot(kind='bar', ax=ax)
                    title = st.session_state.page.replace("_", " ").title() + " Identified"  # Dynamically set the title
                    ax.set_title(title, pad=20, fontsize=16)  # Add title above the chart with specified font size
                    ax.set_xlabel("")  # Remove x-axis label from the bottom
                    ax.set_xticklabels(selected_data.index, rotation=45, ha='right', fontsize=12)  # Rotate and align x-tick labels
                    ax.legend(fontsize=14)  # Adjust the legend font size
                    st.pyplot(fig)

    # Logout if requested, move to the bottom
    if st.sidebar.button("Logout"):
        st.session_state.username = None
        st.session_state.page = None
        st.session_state.clear()  # Clear session state
        st.experimental_rerun()  # Rerun the app to reset everything

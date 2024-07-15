import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

# URL of the logo image in your GitHub repository
logo_url = "https://raw.githubusercontent.com/Klfnovice/lnatabulation/main/lcwd%20logo.png?token=GHSAT0AAAAAACTIRZDV7W6H5NX7VZGDEZ44ZTCKAOA"

# Set sidebar background color
def set_sidebar_style():
    st.markdown("""
        <style>
        .sidebar .sidebar-content {
            background: #000080;
            color: blue;
        }
        </style>
    """, unsafe_allow_html=True)

# User authentication
def authenticate(username, password):
    users = {
        "admin": "pass123",
        "dmantiado": "hrlcwd2024",
        "user1": "password1"
    }
    return username in users and users[username] == password

# Store data to Excel
def store_data_to_excel(df, file_name):
    df.to_excel(file_name, index=False)

# Store data to CSV
def store_data_to_csv(df, file_name):    
    df.to_csv(file_name, index=False)

# Create table in SQLite database if it doesn't exist
def create_table_if_not_exists(table_name):
    conn = sqlite3.connect("competencies.db")
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS [{table_name}] (
            COMPETENCIES_IDENTIFIED TEXT, 
            Basic INTEGER, 
            Intermediate INTEGER, 
            Advanced INTEGER, 
            Superior INTEGER, 
            Not_yet_Acquired INTEGER
        )
    """)
    conn.commit()
    conn.close()

# Retrieve data from SQLite database
def retrieve_data_from_database(table_name):
    create_table_if_not_exists(table_name)
    conn = sqlite3.connect("competencies.db")
    df = pd.read_sql(f"SELECT * FROM [{table_name}]", conn)
    conn.close()
    if 'CURRENT COMPETENCIES IDENTIFIED' in df.columns:
        df.set_index('CURRENT COMPETENCIES IDENTIFIED', inplace=True)
    elif 'DEVELOPMENTAL COMPETENCIES IDENTIFIED' in df.columns:
        df.set_index('DEVELOPMENTAL COMPETENCIES IDENTIFIED', inplace=True)
    return df

# Initialize session state
def initialize_session_state():
    if "username" not in st.session_state:
        st.session_state.username = None
        st.session_state.page = None
        st.session_state.competency_data = {"Current_Competencies": pd.DataFrame(),
                                            "Developmental_Competencies": pd.DataFrame()}

# Login form
def login_form():
    with st.form("login_form"):
        st.write("### Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Submit")
        return username, password, submit_button

# Display logo and title
def display_logo_and_title():
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{logo_url}" width="100" alt="Logo">
            <h1>Human Resource Section LNA/IDP Tabulation</h1>
        </div>
    """, unsafe_allow_html=True)

# Display data and chart
def display_data_and_chart(uploaded_data, competency_type):
    if uploaded_data is not None and not uploaded_data.empty:
        st.write("Tabulation Table:")
        st.write(uploaded_data)
        selected_columns = st.multiselect("Select the level of competency to display in chart", uploaded_data.columns)
        if selected_columns:
            selected_data = uploaded_data[selected_columns]
            if st.button("Show Chart"):
                fig, ax = plt.subplots(figsize=(26, 10))
                selected_data.plot(kind='bar', ax=ax)
                title = competency_type.replace("_", " ").title() + " Identified"
                ax.set_title(title, pad=20, fontsize=16)
                ax.set_xlabel("")
                ax.set_xticklabels(selected_data.index, rotation=45, ha='right', fontsize=14)
                ax.legend(fontsize=14)
                
                # Formatter function to show integer values on the y-axis
                def int_formatter(x, pos):
                    return f'{int(x)}'
                
                ax.yaxis.set_major_formatter(FuncFormatter(int_formatter))
                
                # Set the y-axis major locator to have ticks at every 1 unit
                ax.yaxis.set_major_locator(MultipleLocator(1))
                
                # Add horizontal gridlines
                ax.grid(axis='y')

                st.pyplot(fig)

# Upload file
def upload_file(page):
    uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel File", type=["csv", "xlsx"])
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
            st.session_state.competency_data[page] = df
            conn = sqlite3.connect("competencies.db")
            df.to_sql(page, conn, if_exists="replace")
            conn.close()
            st.success("File uploaded successfully!")
            return df
    return None

# Main application logic
def main():
    display_logo_and_title()
    set_sidebar_style()
    initialize_session_state()

    if st.session_state.username is None:
        username, password, submit_button = login_form()
        if submit_button:
            if authenticate(username, password):
                st.session_state.username = username
                st.success("Login successful!")
                st.experimental_rerun()
            else:
                st.error("Authentication failed. Please check your username and password.")
    else:
        if st.session_state.username != "admin":
            competency_type = st.sidebar.radio("Navigation", ["Current_Competencies", "Developmental_Competencies"])
            st.write(f"You are viewing: {competency_type}")
            uploaded_data = retrieve_data_from_database(competency_type)
            display_data_and_chart(uploaded_data, competency_type)
        else:
            st.session_state.page = st.sidebar.radio("For Uploading", ["Current_Competencies", "Developmental_Competencies"])
            uploaded_data = upload_file(st.session_state.page)
            if uploaded_data is None:
                uploaded_data = retrieve_data_from_database(st.session_state.page)
            display_data_and_chart(uploaded_data, st.session_state.page)

        if st.sidebar.button("Logout"):
            st.session_state.username = None
            st.session_state.page = None
            st.session_state.clear()
            st.experimental_rerun()

if __name__ == "__main__":
    main()

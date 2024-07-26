import os
import pandas as pd
import sqlite3
import streamlit as st
import matplotlib.pyplot as plt
# import webbrowser
# from fpdf import FPDF

# Function to make labels bold
# def bold_label(label):
#     return f"<div style='font-weight: bold;'>{label}</div>"

# Function to save data to the database
def save_data(user_id, device, learning_mode, competencies):
    with conn:
        for competency in competencies:
            c.execute('''
            INSERT INTO elearning_preferences (
                user_id, device, learning_mode, select_competency, competency_level
            ) VALUES (?, ?, ?, ?, ?)''', 
            (user_id, device, learning_mode, competency['name'], competency['level']))
        conn.commit()

# Function to generate PDF report
# def generate_pdf(data, filename):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.cell(200, 10, txt="e-Learning Preferences Report", ln=True, align='C')
#     pdf.ln(10)

#     for row in data:
#         pdf.cell(200, 10, txt=f"Device: {row[1]}", ln=True)
#         pdf.cell(200, 10, txt=f"Learning Mode: {row[2]}", ln=True)
#         pdf.cell(200, 10, txt=f"Competency: {row[3]}", ln=True)
#         pdf.cell(200, 10, txt=f"Competency Level: {row[4]}", ln=True)
#         pdf.ln(10)

#     pdf_output_path = os.path.join(os.getcwd(), filename)
#     pdf.output(pdf_output_path)
#     return pdf_output_path

# # Function to generate a marksheet PDF for a specific user
# def generate_marksheet(user_data):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
    
#     pdf.cell(200, 10, txt="Marksheet", ln=True, align='C')
#     pdf.ln(10)
    
#     pdf.cell(200, 10, txt=f"Device: {user_data[1]}", ln(True)
#     pdf.cell(200, 10, txt=f"Learning Mode: {user_data[2]}", ln(True)
#     pdf.cell(200, 10, txt=f"Competency: {user_data[3]}", ln(True)
#     pdf.cell(200, 10, txt=f"Competency Level: {user_data[4]}", ln(True)
#     pdf.ln(10)

#     pdf_output_path = os.path.join(os.getcwd(), f"{user_data[2]}_marksheet.pdf")
#     pdf.output(pdf_output_path)
#     return pdf_output_path

# Function to delete data from the database
def delete_data(user_id):
    with conn:
        c.execute('DELETE FROM elearning_preferences WHERE user_id = ?', (user_id,))
        conn.commit()

# Competency descriptions
competency_descriptions = {
    "Accounting": 
        {
        "Description": """The ability to record, analyze, classify, summarize and interprets financial transactions to be able to prepare for a sound financial report and manage the accounts of the organization.""",
        "Basic":
        "Intermediate":
        "Advanced":
        "Superior":
        },
    
    "Accounting Reconciliation": 
        {
        "Description": """The ability to carry out timely and accurate reconciliation of accounting control statements, including bank reconciliations, control accounts, revenue reconciliations, advances, and deposits.""",
        "Basic":
        "Intermediate":
        "Advanced":
        "Superior":
        },
    
    "Air-Conditioning Servicing":
        {
        "Description": """Explain basic principles of electrical and mechanical aspects of the Air-Conditioning Unit to safely install, commission, service and maintain air conditioning system.""",
        "Basic":
        "Intermediate":
        "Advanced":
        "Superior":
        },

    "Applying Internal Control Functions":
        {
        "Has the ability to integrate effective design and develop financial management system that address issues related to financial management and operations to safeguard government assets, check the accuracy and reliability of accounting data, adhere to management policies, comply with laws and regulations and ensure efficient, ethical and economical operations.""",
        "Basic":
        "Intermediate":
        "Advanced":
        "Superior":
        },
    
    "AutoCAD":
        {
    
    },
}

# Database connection
conn = sqlite3.connect('elearning_preferences.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS elearning_preferences (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    device TEXT,
    learning_mode TEXT,
    select_competency TEXT,
    competency_level TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

# Create users table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    full_name TEXT,
    password TEXT,
    designation TEXT,
    position_level TEXT
)
''')
conn.commit()

# Function to authenticate users
def authenticate_user(username, password):
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    return user

# Login functionality
st.sidebar.title('Login')

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.sidebar.text_input('Username', key='login_username')
    password = st.sidebar.text_input('Password', type='password', key='login_password')
    login_button = st.sidebar.button('Login', key='login_button')
    
    if login_button:
        user = authenticate_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.user_id = user[0]  # Assuming the user ID is the first column in the users table
            st.session_state.username = username
            st.session_state.full_name = user[2]  # Assuming the full name is the third column in the users table
            st.session_state.designation = user[4]  # Assuming the designation is the fifth column in the users table
            st.session_state.position_level = user[5]  # Assuming the position level is the sixth column in the users table
            st.experimental_rerun()
        else:
            st.sidebar.error('Invalid username or password')
else:
    st.sidebar.success(f'Logged in as {st.session_state.full_name}')
    if st.sidebar.button('Logout'):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.experimental_rerun()

if st.session_state.logged_in:
    if st.session_state.username == 'admin':
        st.title('Admin Dashboard')

        st.markdown("## Stored Data")
        c.execute('SELECT * FROM elearning_preferences')
        rows = c.fetchall()
        df = pd.DataFrame(rows, columns=["ID", "User ID", "Device", "Learning Mode", "Competency", "Competency Level"])
        st.dataframe(df)

        if st.button('Generate PDF Report for All Data'):
            pdf_path = generate_pdf(rows, "all_elearning_preferences.pdf")
            webbrowser.open(f"file://{pdf_path}")
            st.success(f"PDF Report generated: {pdf_path}")

        selected_user = st.selectbox('Select a user to generate marksheet', df['User ID'].unique())
        if st.button('Generate Marksheet for Selected User'):
            user_data = df[df['User ID'] == selected_user].values[0]
            pdf_path = generate_marksheet(user_data)
            webbrowser.open(f"file://{pdf_path}")
            st.success(f"Marksheet PDF generated for {selected_user}: {pdf_path}")

        st.markdown("## Display Charts")
        chart_type = st.selectbox('Select Chart Type', ['Individual User', 'All Users'])

        if chart_type == 'Individual User':
            selected_user_for_chart = st.selectbox('Select a user', df['User ID'].unique())
            if st.button('Generate Chart for User'):
                user_data = df[df['User ID'] == selected_user_for_chart]
                if not user_data.empty:
                    user_chart_data = user_data['Competency Level'].value_counts()
                    fig, ax = plt.subplots()
                    user_chart_data.plot(kind='bar', ax=ax)
                    ax.set_title(f"Competency Levels for User {selected_user_for_chart}")
                    ax.set_xlabel("Competency Level")
                    ax.set_ylabel("Count")
                    st.pyplot(fig)

        if chart_type == 'All Users':
            if st.button('Generate Chart for All Users'):
                all_users_chart_data = df['Competency Level'].value_counts()
                fig, ax = plt.subplots()
                all_users_chart_data.plot(kind='bar', ax=ax)
                ax.set_title("Competency Levels for All Users")
                ax.set_xlabel("Competency Level")
                ax.set_ylabel("Count")
                st.pyplot(fig)

        st.sidebar.title('Admin Actions')
        st.sidebar.markdown("## Delete User Data")
        user_to_delete = st.sidebar.selectbox('Select a user to delete', df['User ID'].unique())
        if st.sidebar.button('Delete User'):
            delete_data(user_to_delete)
            st.experimental_rerun()
            st.sidebar.success(f"Data for User ID {user_to_delete} has been deleted.")
    else:
        st.title('User Dashboard')
        st.write(f"Welcome, {st.session_state.full_name}!")

        # Initialize session state for the survey_started and competencies variables
        if 'survey_started' not in st.session_state:
            st.session_state.survey_started = False
        if 'competencies' not in st.session_state:
            st.session_state.competencies = []

        if not st.session_state.survey_started:
            if st.button('Start LNA Survey'):
                st.session_state.survey_started = True
                st.experimental_rerun()

        if st.session_state.survey_started:
            # Inputs with bold labels
            st.markdown(('Device Used for e-Learning'), unsafe_allow_html=True)
            device = st.selectbox(' ', ['Computer/Laptop', 'Tablet', 'Smartphone'], key='device')
            st.markdown(('Preferred Learning Mode'), unsafe_allow_html=True)
            learning_mode = st.selectbox(' ', ['Synchronous Face-to-Face', 'Asynchronous', 'Blended'], key='learning_mode')
            st.markdown(('Select Competency'), unsafe_allow_html=True)
            select_competency = st.selectbox(' ', ['Select Competency'] + list(competency_descriptions.keys()), key='select_competency')
            
            st.markdown(('My Level for this Competency'), unsafe_allow_html=True)
            competency_level = st.selectbox(' ', ['Basic', 'Intermediate', 'Advanced', 'Superior', 'Not yet acquired'], key='competency_level')

            if st.button('Add Competency'):
                st.session_state.competencies.append({'name': select_competency, 'level': competency_level})
                st.experimental_rerun()

            if st.session_state.competencies:
                st.markdown("## Added Competencies")
                competencies_df = pd.DataFrame(st.session_state.competencies)
                st.dataframe(competencies_df)

            col1, col2 = st.columns([1, 1])

            with col1:
                if st.button('Save All'):
                    save_data(st.session_state.user_id, device, learning_mode, st.session_state.competencies)
                    st.success('Information saved successfully!')
                    st.session_state.competencies = []  # Clear the competencies list after saving
                    st.experimental_rerun()

            with col2:
                if st.button('Reset'):
                    st.session_state.competencies = []
                    st.experimental_rerun()

else:
    st.warning('This site is currently under construction, please stand by.')

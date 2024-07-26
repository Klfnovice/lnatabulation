import os
import pandas as pd
import sqlite3
import streamlit as st
from fpdf import FPDF
import webbrowser

# Competency descriptions
competency_descriptions = {
    "Accounting": {
        "Description": """The ability to record, analyze, classify, summarize and interprets financial transactions to be able to prepare for a sound financial report and manage the accounts of the organization.""",
        "Basic": """
            - Receives and records all claims for processing, evaluation and certification of the unit.
            - Checks completeness of documents/attachments needed for the transaction and validates accuracy of computation.
            - Prepares certification or statement of employees' contributions and remittances.
            - Maintains index of records of compensation, benefits, allowances, mandatory deductions and remittances.
            - Prepares journal entries and certificates of taxes withheld.
            - Writes simple pro-forma communications on accounting transactions.
        """,
        "Intermediate": """
            - Validates and records journal entries of financial transactions.
            - Records financial transactions in the book of accounts and maintains files of financial reports/documents.
            - Prepares certificate of remittances, schedule of remittances and all other requirements for remittances.
            - Updates records of receipts and expenditures funds to monitor balance of funds and verifies records of funds availability.
            - Reconciles general and subsidiary ledgers of accounts.
            - Prepares replies to queries on accounting transactions.
        """,
        "Advanced": """
            - Reviews monthly deductions and remittances to national government agencies.
            - Reviews ledger, general ledger accounts and schedules of the financial reports.
            - Validates and reconciles reciprocal accounts for the central/regional offices.
            - Prepares financial reports, schedules and all other reports of all funds as required by the regulatory agencies and the Commission.
            - Approves journal entries.
            - Develops or enhances existing policies, guidelines and processes on accounting and auditing procedures.
        """,
        "Superior": """
            - Certifies funds availability of disbursements, supporting documents are complete and proper and the necessary deductions are effected and monitors timely remittance of all deductions and payments made.
            - Identifies trends and developments in accounting and auditing and recommends enhancement of policies, procedures, systems and processes.
            - Develops communication plan and policies, guidelines and issuances on accounting rules and regulations.
            - Reviews and recommends policies, guidelines and processes on accounting and auditing procedures.
            - Prepares financial report for management and recommends appropriate financial internal control measures for the allocation and sourcing of funds.
        """,
    },
    # Add other competencies here...
}

# Database connection
conn = sqlite3.connect('elearning_preferences.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS elearning_preferences (
    id INTEGER PRIMARY KEY,
    full_name TEXT,
    current_position TEXT,
    position_level TEXT,
    device TEXT,
    learning_mode TEXT,
    select_competency TEXT,
    competency_level TEXT
)
''')
conn.commit()

# Users dictionary
user_passwords = {
    'admin': 'admin',
    'a.abad': 'empid1',
    'm.abellano': 'empid2',
    'a.abiera': 'empid3',
    'a.abrique': 'empid4',
    # Add more users here...
}

user_display_names = {
    'admin': 'Admin',
    'a.abad': 'Alessandro Abad',
    'm.abellano': 'Mark Abellano',
    'a.abiera': 'Arthur Abiera',
    'a.abrique': 'Anthony Abrique',
    # Add more user display names here...
}

# Login functionality
st.sidebar.title('Login')

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    username = st.sidebar.text_input('Username', key='login_username')
    password = st.sidebar.text_input('Password', type='password', key='login_password')
    login_button = st.sidebar.button('Login', key='login_button')
    
    if login_button:
        if username in user_passwords and user_passwords[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.experimental_rerun()
        else:
            st.sidebar.error('Invalid username or password')
else:
    st.sidebar.success(f'Logged in as {user_display_names[st.session_state.username]}')
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
        df = pd.DataFrame(rows, columns=["ID", "Full Name", "Current Position", "Position Level", "Device", "Learning Mode", "Competency", "Competency Level"])
        st.dataframe(df)
        
        if st.button('Generate PDF Report for All Data'):
            pdf_path = generate_pdf(rows, "all_elearning_preferences.pdf")
            webbrowser.open(f"file://{pdf_path}")
            st.success(f"PDF Report generated: {pdf_path}")

        selected_user = st.selectbox('Select a user to generate marksheet', df['Full Name'])
        if st.button('Generate Marksheet for Selected User'):
            user_data = df[df['Full Name'] == selected_user].values[0]
            pdf_path = generate_marksheet(user_data)
            webbrowser.open(f"file://{pdf_path}")
            st.success(f"Marksheet PDF generated for {selected_user}: {pdf_path}")
        
        st.sidebar.title('Admin Actions')
        st.sidebar.markdown("## Delete User Data")
        user_to_delete = st.sidebar.selectbox('Select a user to delete', df['Full Name'])
        if st.sidebar.button('Delete User'):
            delete_data(user_to_delete)
            st.experimental_rerun()
            st.sidebar.success(f"Data for {user_to_delete} has been deleted.")
    else:
        st.title('User Dashboard')
        st.write(f"Welcome, {user_display_names[st.session_state.username]}!")
        
        # Initialize session state for the survey_started variable
        if 'survey_started' not in st.session_state:
            st.session_state.survey_started = False

        # Display the survey form if the survey has been started and agreed
        if st.session_state.survey_started:
            # Inputs with bold labels
            st.markdown(bold_label('Full Name'), unsafe_allow_html=True)
            full_name = st.text_input(' ', key='full_name')  # Use a unique key to avoid conflicts
            st.markdown(bold_label('Current Position (Write in full including parenthetical, if any)'), unsafe_allow_html=True)
            current_position = st.text_input(' ', key='current_position')
            st.markdown(bold_label('Position Level'), unsafe_allow_html=True)
            position_level = st.selectbox(' ', ['1st Level', '2nd Level Non-Supervisory', 'Supervisory', 'Managerial'], key='position_level')
            st.markdown(bold_label('Device Used for e-Learning'), unsafe_allow_html=True)
            device = st.selectbox(' ', ['Computer/Laptop', 'Tablet', 'Smartphone'], key='device')
            st.markdown(bold_label('Preferred Learning Mode'), unsafe_allow_html=True)
            learning_mode = st.selectbox(' ', ['Synchronous Face-to-Face', 'Asynchronous', 'Blended'], key='learning_mode')
            st.markdown(bold_label('Select Competency'), unsafe_allow_html=True)
            select_competency = st.selectbox(' ', ['Select Competency'] + list(competency_descriptions.keys()), key='select_competency')
            
            st.markdown(bold_label('My Level for this Competency'), unsafe_allow_html=True)
            competency_level = st.selectbox(' ', ['Basic', 'Intermediate', 'Advanced', 'Superior', 'Not yet acquired'], key='competency_level')

            col1, col2 = st.columns([1, 1])

            with col1:
                if st.button('Save'):
                    save_data(full_name, current_position, position_level, device, learning_mode, select_competency, competency_level)
                    st.markdown(f"**Full Name:** {full_name}")
                    st.markdown(f"**Current Position:** {current_position}")
                    st.markdown(f"**Position Level:** {position_level}") 
                    st.markdown(f"**Device Used for e-Learning:** {device}")
                    st.markdown(f"**Preferred Learning Mode:** {learning_mode}")
                    st.markdown(f"**Competency:** {select_competency}")
                    st.markdown(f"**My Level for this Competency:** {competency_level}")
                    st.success('Information saved successfully!')

            with col2:
                if st.button('Reset'):
                    st.experimental_rerun()
        else:
            st.write("Survey has not been started or agreed upon yet.")
            # Optionally add a button to start the survey
            if st.button('Start Survey'):
                st.session_state.survey_started = True

else:
    st.warning('This site is currently under construction, please stand by.')

# Function to make labels bold
def bold_label(label):
    return f"<div style='font-weight: bold;'>{label}</div>"

# Function to save data to the database
def save_data(full_name, current_position, position_level, device, learning_mode, select_competency, competency_level):
    with conn:
        c.execute('''
        INSERT INTO elearning_preferences (
            full_name, current_position, position_level, device, learning_mode, select_competency, competency_level
        ) VALUES (?, ?, ?, ?, ?, ?, ?)''', 
        (full_name, current_position, position_level, device, learning_mode, select_competency, competency_level))
        conn.commit()

# Function to generate PDF report
def generate_pdf(data, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="e-Learning Preferences Report", ln=True, align='C')
    pdf.ln(10)

    for row in data:
        pdf.cell(200, 10, txt=f"Full Name: {row[1]}", ln=True)
        pdf.cell(200, 10, txt=f"Current Position: {row[2]}", ln=True)
        pdf.cell(200, 10, txt=f"Position Level: {row[3]}", ln=True)
        pdf.cell(200, 10, txt=f"Device: {row[4]}", ln=True)
        pdf.cell(200, 10, txt=f"Learning Mode: {row[5]}", ln=True)
        pdf.cell(200, 10, txt=f"Competency: {row[6]}", ln=True)
        pdf.cell(200, 10, txt=f"Competency Level: {row[7]}", ln=True)
        pdf.ln(10)

    pdf_output_path = os.path.join(os.getcwd(), filename)
    pdf.output(pdf_output_path)
    return pdf_output_path

# Function to generate a marksheet PDF for a specific user
def generate_marksheet(user_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Marksheet", ln=True, align='C')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt=f"Full Name: {user_data[1]}", ln=True)
    pdf.cell(200, 10, txt=f"Current Position: {user_data[2]}", ln=True)
    pdf.cell(200, 10, txt=f"Position Level: {user_data[3]}", ln=True)
    pdf.cell(200, 10, txt=f"Device: {user_data[4]}", ln=True)
    pdf.cell(200, 10, txt=f"Learning Mode: {user_data[5]}", ln=True)
    pdf.cell(200, 10, txt=f"Competency: {user_data[6]}", ln=True)
    pdf.cell(200, 10, txt=f"Competency Level: {user_data[7]}", ln=True)
    pdf.ln(10)

    pdf_output_path = os.path.join(os.getcwd(), f"{user_data[1]}_marksheet.pdf")
    pdf.output(pdf_output_path)
    return pdf_output_path

# Function to delete data from the database
def delete_data(full_name):
    with conn:
        c.execute('DELETE FROM elearning_preferences WHERE full_name = ?', (full_name,))
        conn.commit()

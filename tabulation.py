import os
import pandas as pd
import sqlite3
import streamlit as st
#from fpdf import FPDF
#import webbrowser
#from streamlit_modal import Modal

# Competency descriptions from the provided Excel file
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
    "Benefits, Compensation and Welfare Management": {
        "Description": """The ability to develop, implement, evaluate and enhance policies and programs on benefits, compensation, rewards, incentives, health and wellness to improve employee welfare.""",
        "Basic": """
            - Collates data/materials from the conduct and evaluation of organization-wide programs (i.e. health and wellness programs, information campaigns, sports activities, anniversary and Christmas programs, etc.).
            - Maintains and updates employee records (HRMIS, leave, absences and tardiness, medical, service records, etc.).
            - Prepares certifications such as but not limited to compensation, service records, leave balance, attendance and other employee welfare transactions of employees.
            - Writes simple pro-forma communications relative to benefits, compensation and welfare of employees.
            - Maintains and updates procurement records in database/filing system.
        """,
        "Intermediate": """
            - Computes leave, salaries, salary adjustments, loans, medical reimbursements/ entitlements of employees and prepares vouchers.
            - Monitors and reviews office reports to ensure compliance with existing policies, processes and systems of benefits, compensation, rewards & incentives, health and wellness mechanism of the organization.
            - Coordinates with central and regional office representatives in the implementation and evaluation of programs.
            - Prepares replies to queries on benefits, compensation and welfare management.
        """,
        "Advanced": """
            - Conducts information awareness on benefits, compensation, health and wellness programs to employees.
            - Conducts survey, FGD, research, policy studies, benchmarking studies on benefits, compensation and welfare of employees.
            - Prepares organization-wide reports on policy implementation and program administration.
            - Evaluates existing policies, processes and systems on benefits, compensation, wellness mechanisms and proposes enhancements.
        """,
        "Superior": """
            - Establishes and develops a comprehensive employee benefits, compensation and welfare programs for the CSC.
            - Reviews and recommends proposals for enhancements and changes of existing processes and systems of benefits, compensation, and welfare mechanism of the organization.
            - Formulates operational policies and guidelines on the benefits, compensation, and welfare of employees.
            - Develops communication and implementation plan on the benefits and compensation system, and employees welfare programs of the organization.
        """,
    },
    "Budget Management": {
        "Description": """Effective preparation of budget plans using the latest budgeting techniques, and preparation of budget submissions by agency based on policies.""",
        "Basic": """
            - Ability to implement and apply, with guidance or supervision, existing processes and policies for programs and activities.""",
        "Intermediate": """
            - Ability to ensure adherence to procedures, processes and policies in the performance of activities relative to budget management.
        """,
        "Advanced": """
            - Ability to monitor and review data and recommend enhancements and/or changes in procedures, processes and policies relative to budget management.
        """,
        "Superior": """
            - Ability to formulate advance policies and strategies on budget management.
        """,
    },
    # Add other competencies here...
}

# Initialize session state
if 'agreed' not in st.session_state:
    st.session_state.agreed = False

if 'survey_started' not in st.session_state:
    st.session_state.survey_started = False

# Function to display modal content
def show_modal():
    st.markdown(
        """
        <style>
        .modal-content {
            background-color: #fefefe;
            margin: auto;
            padding: 30px;
            border: 1px solid #888;
            width: 80%;
            height: 80vh;
            overflow-y: auto;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div class="modal-content">
            <h3 align="center"><b>Terms of Service and Privacy Policy</b></h3>
            <p>Dear <b>Respondent</b>:</p>
            <p>
                We are currently identifying the learning and development needs of employees in Region V.
                The result of this survey will be critical in identifying learning and development interventions
                that are responsive to your competency needs and the goals of your agency.
            </p>
            <p>
                Your responses are significant to the success of this endeavor and will be treated with utmost confidentiality
                and will be solely used for developmental purposes. Please answer the questions to the best of your knowledge
                and understanding.
            </p>
            <p>
                By choosing “I agree” below you agree to Civil Service Commission Region V’s Terms of Service.
            </p>
            <p>
                You also agree to our Privacy Policy, which describes how we process your information, on the following key points:
            </p>
            <ul>
                <li>When you accomplish and submit the Personal Information portion on LNA form, we store the information you give us.</li>
                <li>When you access the LNA webpage, we process information about that activity – including information like the device you used, IP addresses, cookie data, and location.</li>
                <li>When you accomplish and submit the Survey portion of the LNA form, we store information you give us for analysis.</li>
            </ul>
            <p><b>We process this data to:</b></p>
            <ul>
                <li>Help our services deliver more useful, customized training programs to address your needs;</li>
                <li>Improve the quality of our trainings and develop new ones; and</li>
                <li>Conduct analytics and measurements to address possible needs or concerns that may arise in the future.</li>
            </ul>
            <p>Lastly, you will be able to generate your Individual Development Plan which may be a basis of your agency's Learning and Development Plan for the succeeding year.</p>
            <a href="#"><button class="w3-btn w3-blue" id="agree-button">I Agree to the Terms of Service and Privacy Policy</button></a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Create a modal instance
#modal = Modal(title="Terms of Service and Privacy Policy", key="terms_modal")

# Create database connection
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

import streamlit as st
import pandas as pd
import sqlite3

# Sample users dictionary
user_passwords = {
    'admin': 'admin',
    'a.abad': 'empid1',
    'a.abellano': 'empid2',
    'a.abiera': 'empid3',
    'a.abrique': 'empid4',
    'f.aguilar': 'empid5',
    'z.alcazar': 'empid6',
    's.allorde': 'empid7',
    'mb.añasco': 'empid8',
    'r.ancermo': 'empid9',
    'r.aperin': 'empid10',
    'r.apuli': 'empid11',
    'mc.arenal': 'empid12',
    'r.arias': 'empid13',
    'j.armecin': 'empid14',
    'r.atento': 'empid15',
    'r.atun': 'empid16',
    'cl.ayala': 'empid17',
    'f.ayala': 'empid18',
    'mf.aydalla': 'empid19',
    'm.aydalla': 'empid20',
    'j.ayson': 'empid21',
    'a.azores': 'empid22',
    'r.azores': 'empid23',
    'a.azupardo': 'empid24',
    'k.azupardo': 'empid25',
    'kj.bagnes': 'empid26',
    'ma.balde': 'empid27',
    'rd.balde': 'empid28',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    'j.ayson': 'empid21',
    
    'user2': 'user2'
}

user_display_names = {
    'admin': 'Admin',
    'a.abad': 'Alessandro Abad',
    'm.abellano': 'Mark Abellano',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    'a.abad': 'Alessandro Abad',
    
    'user2': 'User Two'
}

# Database connection (assuming you have a SQLite database)
conn = sqlite3.connect('your_database.db')
c = conn.cursor()

# Function to generate PDF (assuming these functions are defined elsewhere)
def generate_pdf(data, filename):
    # Placeholder function
    pass

def generate_marksheet(data):
    # Placeholder function
    pass

def delete_data(user):
    c.execute('DELETE FROM elearning_preferences WHERE "Full Name" = ?', (user,))
    conn.commit()

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
else:
    st.warning('Please login to start survey')






# Function to create bold labels without extra space
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

    
    
    pdf.cell(200, 10, txt="", ln=True, align='C')
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


        # Add "Start LNA Survey" button to the sidebar for non-admin users
        if st.sidebar.button('Start LNA Survey') and not st.session_state.agreed:
            modal.open()
            st.session_state.survey_started = True

        # Display the modal if it is open
        
        
        
        #if modal.is_open() and not st.session_state.agreed:
            #with modal.container():
                #show_modal()

        
        
        # Handle the agreement
        if st.session_state.agreed:
            st.write("You have agreed to the Terms of Service and Privacy Policy. Proceed with the survey.")

        # JavaScript to trigger the agreement button click
        st.markdown(
            """
            <script>
            document.getElementById("agree-button").onclick = function() {
                fetch('/agree', {method: 'POST'});
            }
            </script>
            """,
            unsafe_allow_html=True,
        )

        # Handle the agreement on the backend
        if st.query_params.get("agree"):
            st.session_state.agreed = True

        # Display the survey form if the survey has been started and agreed
        if st.session_state.survey_started and st.session_state.agreed:
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

            # Display competency descriptions
            if select_competency in competency_descriptions:
                st.markdown(f"### {select_competency} Competency Descriptions")
                st.markdown(competency_descriptions[select_competency]["Description"])
                cols = st.columns(4)
                levels = ["Basic", "Intermediate", "Advanced", "Superior"]
                for i, level in enumerate(levels):
                    cols[i].markdown(f"**{level}**")
                    cols[i].markdown(competency_descriptions[select_competency][level])
            
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

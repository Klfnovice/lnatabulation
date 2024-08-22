import pandas as pd
import sqlite3
import streamlit as st
import matplotlib.pyplot as plt
import webbrowser
import os
from fpdf import FPDF
from datetime import datetime
from io import BytesIO
import requests
import openai
from streamlit_option_menu import option_menu

# Competency descriptions
competency_descriptions = {
    "Accounting": {"Description": "The ability to record, analyze, classify, summarize and interprets financial transactions to be able to prepare for a sound financial report and manage the accounts of the organization."},
    "Accounts Reconciliation": {"Description": "The ability to carry out timely and accurate reconciliation of accounting control statements, including bank reconciliations, control accounts, revenue reconciliations, advances, and deposits."},
    "Air-Conditioning Servicing": {"Description": "Explain basic principles of electrical and mechanical aspects of the Air-Conditioning Unit to safely install, commission, service and maintain air conditioning system."},
    "Applying Internal Control Functions": {"Description": "Has the ability to integrate effective design and develop financial management system that address issues related to financial management and operations to safeguard government assets, check the accuracy and reliability of accounting data, adhere to management policies, comply with laws and regulations and ensure efficient, ethical and economical operations."},
    "AutoCAD": {"Description": "The ability to operate software programs to create technical two-dimensional (2D) and three-dimensional (3D) designs."},
    "Automotive Servicing": {"Description": "Effectively achieve to inspect, clean and repair mechanical or electrical parts, components, assemblies and sub-assemblies of light and heavy-duty automotive vehicle with diesel or gas engine in accordance with manufacturer’s specification. It also covers servicing of engine mechanical components such as cooling and lubricating system and under chassis servicing and repair."},
    "Benefits, Compensation and Welfare Management": {"Description": "The ability to develop, implement, evaluate and enhance policies and programs on benefits, compensation, rewards, incentives, health and wellness to improve employee welfare."},
    "Budget Management": {"Description": "Effective preparation of budget plans using the latest budgeting techniques, and preparation of budget submissions by agency based on policies"},
    "Carpentry Skill": {"Description": "Has the ability to perform stake-out building lines, fabricate formworks, install/strip form works, install framing works, install architectural ceiling/wall sheets/panels and floor finishes and fabricate/install door/window jambs and panels."},
    "Cash Management": {"Description": "The ability to collect and manage assessment and usage of cash flow to ensure the financial stability and solvency of an organization."},
    "Chlorine Handling Skills": {"Description": "Has the fundamental knowledge to be able to safely use and handle chlorine and other chemical solutions in the District’s water treatment facilities."},
    "Computer Skills": {"Description": "The ability to operate standard personal computer and use available computer software, applications and technology."},
    "Conduct Audit Assignments": {"Description": "Using an audit methodology that is consistent with international standards on public sector audit for selecting a process for audit, planning an audit assignment, documenting a process, assessing risks and controls in a process, assessing the performance of processes, identifying control gaps, conducting audit tests, and accurately recording audit work."},
    "Customer Complaints Management": {"Description": "Has the ability to use proper channels to deal with customer complaints effectively to improve customer retention."},
    "Data Collection from Utility Meters": {"Description": "Demonstrate proficiency in using handheld devices and conduct accurate records of reading meters."},
    "Data Management": {"Description": "The ability to analyze statistics and other data by interpreting and evaluating the results to be able to formulate a report and/or presentation as reference for decision making."},
    "Delivering Service Excellence": {"Description": "The ability to provide proactive, responsive, accessible, courteous and effective public service to attain the highest level customer satisfaction."},
    "Digital Media and Visualization": {"Description": "The ability to convey ideas and information in forms such as audio, text, pictures, diagrams, video, photos, maps and 3D models."},
    "Drafting Construction Drawings": {"Description": "The ability to draft precise and detailed planning design for building and infrastructure project within the criteria set in conformance with the structural codes and standards."},
    "Drafting Electrical Layouts": {"Description": "The ability to draft precise and detailed electrical layout plan for the electrical wiring within the criteria set in conformance with the electrical codes and standards."},
    "Driving": {"Description": "Capable to operate motor vehicles classified under LTO Restriction with compliance to local traffic rules and regulations and perform minor vehicle repairs and other minor servicing."},
    "Electrical Installation": {"Description": "Has the capability to install and maintain electrical wiring, lighting and related equipment and systems where the voltage does not exceed the required voltage in building establishment."},
    "Electronics and Electrical Equipment Servicing": {"Description": "Has the ability to conduct maintenance and repair of electronic products and service appliances."},
    "Environmental Compliance": {"Description": "Has the ability to identify, define, develop, evaluate and improve systems, processes and procedures that ensures constant compliance of the project proponents, local government and its partner agencies/organizations in the implementation of projects, programs and activities related to and/or has adverse impact directly or indirectly to environment and natural resources."},
    "Facilities Management": {"Description": "Has the ability to maintain and improve office facilities or properties in order to ensure minimal disruption of business operations."},
    "Heavy Equipment Operation Skill": {"Description": "Demonstrate competency on operating heavy equipment according to procedures, specifications and manual of instruction."},
    "Housekeeping": {"Description": "Has the ability to maintain cleanliness of public areas, equipment and promote workplace hygiene procedures in providing housekeeping services."},
    "Information Technology Management": {"Description": "Demonstrate skills and working knowledge in Information Technology Management. Applies technical skills and demonstrates knowledge of emerging technology (e.g. IT processes, methodologies, etc.)."},
    "Inventory Management and Stock Control": {"Description": "Has the ability to record and manage inventory which typically covers the receipt and custody of items procured, ensuring just-in-time distribution when needed, safe maintenance of stocks, monitoring of re-order point and disposal of unnecessary stocks."},
    "Learning and Development Planning": {"Description": "The ability to translate training/learning needs results into interventions and prioritize them for implementation."},
    "Learning Measurement and Evaluation": {"Description": "The ability to determine training/learning needs and evaluate its effectiveness."},
    "Legal Management": {"Description": "The ability to provide legal assistance and oversee all legal matters within the organization."},
    "Liquidity, Debts and Investment Management": {"Description": "Has the ability to develop strategies in ensuring liquidity, debt and investment management to cover payments against all vouchers, and undertake investment programs in times of cash surplus."},
    "Management of Accounts Receivable": {"Description": "Ensuring the monitoring of timely payment of receivables and provide strategic initiatives for the improvement and more efficient accounts receivable management system."},
    "Market Analysis": {"Description": "Has the ability to gather and analyze data related to potential target consumers that will help generate revenues in the agency."},
    "Masonry": {"Description": "Has the ability to perform construction of brick and concrete block structure, installation of pre-cast baluster/handrail and plastering of concrete wall surface."},
    "Meter Maintenance / Calibration": {"Description": "Has the knowledge of calibration procedures and the ability to troubleshoot water meters within the prescribed standards."},
    "Metal Arc Welding": {"Description": "Has the ability to perform weld carbon steel plate and pipe components as specified by layout, blueprints, diagrams, work order, welding procedure or oral instructions using shielded metal arc welding equipment."},
    "Monitoring and Evaluating": {"Description": "Gathering and evaluating information to determine whether or not the on-going activities of a program are in line with intended direction or results."},
    "Negotiation Skills": {"Description": "Has the ability to adopt appropriate techniques for negotiating resistance and objections in order to negotiate to a desired outcome."},
    "Network, Telecommunication, Wireless and Mobility Knowledge": {"Description": "The ability to demonstrate expertise on processes, hardware, and software employed to facilitate communication between people computer systems and devices."},
    "Non-Revenue Water Management": {"Description": "Has the ability to identify leakages and provide strategic initiatives to address the reduction of non-revenue water."},
    "Occupational Safety and Health": {"Description": "Has the awareness to practice, evaluate, lead, establish and manage Occupational Safety and Health programs in the workplace."},
    "Oral Communication": {"Description": "Makes clear and convincing oral presentations to individual or groups; listens effectively and clarifies information as needed."},
    "Organizational and Procurement Planning": {"Description": "The ability to effectively undertake procurement planning, programming, project management, and requirement specifications to facilitate achievement of organizational or agency program of work, goals and targets within the specific acceptable timetable and budget."},
    "Pipe-Fitting": {"Description": "Has the ability to cut, bevel, and / or thread pipes, and install overhead and underground piping system."},
    "Planning and Delivering": {"Description": "The ability to prioritize and identify scope and allocate resources to meet individual, team, or organization targets and objectives."},
    "Plumbing-Service Connection": {"Description": "Has the capability of installing multiple units of plumbing system with multi-point hot-and-cold-water lines which also includes plumbing repair and maintenance works."},
    "Plumbing-Distribution System": {"Description": "Has the capability of installing and connecting network pipes in the water distribution system which also includes distribution and mainline repair."},
    "Policy Evaluation": {"Description": "The ability to measure and assess the appropriateness, effectiveness and efficiency of human resource policies, contributing to policy improvements and innovation."},
    "Preparation of Expenditure Program": {"Description": "The production of the monthly expenditure program (monthly flow), forecast by object allotment class (Personnel Services, MOOE and Capital Expenditure) using all relevant and available historical data to the highest degree of accuracy possible."},
    "Preparation of Revenue Program": {"Description": "Forecasting the monthly revenue program using all relevant and available historical data with the highest degree of accuracy possible."},
    "Preparing Feasibility Studies": {"Description": "The ability to systematically gather and analyze relevant information pertaining to some programs aimed at advancing and achievement the strategic agenda of the agency."},
    "Pressure Management": {"Description": "The ability to effectively regulate water pressure within water networks in ensuring the efficient and sustainable distribution of water supply."},
    "Procurement Management": {"Description": "The ability to plan and implement measures to acquire supplies and properties at the best possible cost; that meets the quality, quantity and timeliness requirement of the organization; and are compliant to procurement policies."},
    "Procurement Market Analysis": {"Description": "The ability to adopt strategies in identifying competition and market-segmentation prior to procurement in order to secure economic advantage."},
    "Procurement Planning": {"Description": "The ability to effectively undertake procurement planning according to the approved Annual Procurement Plan in order to facilitate the achievement of the agency’s program of work, goals and targets."},
    "Program / Course Delivery and Administration": {"Description": "The ability to plan, execute and report the implementation of training/learning interventions, courses and programs."},
    "Project / Program Management": {"Description": "The ability to monitor and coordinate the implementation of plans, policies, tasks and activities of programs and projects being undertaken by the stakeholder, and taking action to meet quality and performance goals."},
    "Public Relation Management": {"Description": "The ability to build, maintain and manage engagement and goodwill between the organization and the public through the installation of assistance and complaint mechanisms and the implementation of special programs."},
    "Pump Operation": {"Description": "The ability to monitor and maintain the pumping equipment and facilities in order to ensure maximum efficiency of its operations."},
    "Quality Management and Assurance": {"Description": "Performs tasks in ensuring that products or services consistently meet the prescribed government standards or within the prescribed contract agreement by other private institution."},
    "Records Management": {"Description": "The ability to apply and adapt records management standards related to the cycle of records in an agency/institution which are conducted to achieve adequate and proper documentation of government policies, transactions and effective management of the agency’s operations."},
    "Recruitment, Selection and Placement": {"Description": "The ability to search, attract, and assess job candidates and to guide the appointing authority in choosing the best fit for the job at the right time, in accordance with legal requirements in order to achieve organizational goals."},
    "Rewards and Recognition": {"Description": "The ability to identify, develop and implement programs for the organization/bureaucracy to reward and recognize outstanding performance and behavior."},
    "Supervisory Control and Data Acquisition (SCADA) Operation": {"Description": "The ability to develop a SCADA application and to use SCADA systems in the agency’s operation."},
    "Strategic Planning": {"Description": "The ability to influence, realign the organization's strategic goals and directions; monitor and review data from various aspects of strategic and corporate planning and recommend enhancements."},
    "Stress Management": {"Description": "The ability to apply techniques to cope with or lessen the physical and emotional effects of everyday life pressure in the workplace."},
    "Supplier Management and Contract Agreement": {"Description": "Has the ability to manage suppliers in order to ensure continuing provision of goods and services. Manage contract implementation and ensure fair, open and transparent dealings with existing and potential suppliers."},
    "Supplies and Property Management": {"Description": "The ability to plan and implement measures to efficiently allocate, utilize, maintain and dispose supplies and properties of the organization."},
    "Taxation": {"Description": "Has the ability to interpret, understand and manage various aspects of Philippine Tax laws."},
    "User and Customer Support": {"Description": "The ability to provide services, assistance, and technical support to help users implement and solve problems related to information technology."},
    "*Thinking Strategically and Creatively": {"Description": "The ability to “see the big picture”, think multi-dimensionally, craft innovative solutions, identify connections between situations or things that are not obviously related, and come up with new ideas and different ways to enhance organizational effectiveness and responsiveness."},
    "*Leading Change": {"Description": "The ability to generate genuine enthusiasm and momentum for organizational change. It involves engaging and enabling groups to understand, accept and commit to the change agenda. It also includes advancing and sustaining change."},
    "*Building Collaborative, Inclusive Working Relationship": {"Description": "The ability to build and maintain a network of reciprocal, high trust, synergistic working relationships within the organization and across government and relevant sectors. This involves the ability to successfully leverage and maximize opportunities for strategic influencing within the organization and with external stakeholders."},
    "*Managing Performance and Coaching for Results": {"Description": "The ability to create an enabling environment which will nurture and sustain a performance-based, coaching culture. Effectiveness in this competency area also includes a strong focus on developing people for current and future needs, managing talent, promoting the value of continuous learning and improvement."},
    "*Creating and Nurturing a High Performing Organization": {"Description": "The ability to create a high performing organizational culture that is purpose-driven, results-based, client-focused and team-oriented."},
    "*Performance Management": {"Description": "The ability to collect, analyze, review and report performance data and establish scientific basis for performance targets and measures."}
}


# Function to make labels bold
def bold_label(label):
    return f"<div style='font-weight: bold;'>{label}</div>"

# Initialize session state variables
def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'competencies' not in st.session_state:
        st.session_state.competencies = []
    if 'survey_started' not in st.session_state:
        st.session_state.survey_started = False
    if 'show_input_fields' not in st.session_state:
        st.session_state.show_input_fields = False
    if 'new_competencies' not in st.session_state:
        st.session_state.new_competencies = False
    if 'select_competency' not in st.session_state:
        st.session_state.select_competency = None
    if 'competency_level' not in st.session_state:
        st.session_state.competency_level = 'Basic'
    if 'upskilling_reskilling' not in st.session_state:
        st.session_state.upskilling_reskilling = ''
    if 'add_competency_clicked' not in st.session_state:
        st.session_state.add_competency_clicked = False
    if 'display_welcome_back' not in st.session_state:
        st.session_state.display_welcome_back = True
    if 'hide_saved_data' not in st.session_state:
        st.session_state.hide_saved_data = False
    if 'oic_dept_div' not in st.session_state:
        st.session_state.oic_dept_div = ''
    if 'intro_hidden' not in st.session_state:
        st.session_state.intro_hidden = False
    if 'supervisor_name' not in st.session_state:
        st.session_state.supervisor_name = ''  # Initialize supervisor_name

init_session_state()

# Define callback functions to reset the selections
def reset_selection():
    st.session_state['select_competency'] = None
    st.session_state['competency_level'] = 'Basic'
    st.session_state['upskilling_reskilling'] = ''
    st.session_state['hide_saved_data'] = False

# Function to hide the introduction
def hide_intro():
    st.session_state.intro_hidden = True

# Database connection
conn = sqlite3.connect('elearning_preferences.db')
c = conn.cursor()

# Check if the division column exists, and add it if it doesn't
try:
    c.execute("SELECT division FROM users LIMIT 1")
except sqlite3.OperationalError:
    c.execute('ALTER TABLE users ADD COLUMN division TEXT')
    conn.commit()

# Create table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS elearning_preferences (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    select_competency TEXT,
    competency_level TEXT,
    upskilling_reskilling TEXT,
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
    department TEXT,
    division TEXT,
    supervisors_name TEXT
)
''')
conn.commit()

# Create supervisors_details table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS supervisors_details (
    id INTEGER PRIMARY KEY,
    supervisor_name TEXT,
    designation TEXT,
    division TEXT,
    department TEXT
)
''')
conn.commit()


# Create competencies table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS competencies (
    id INTEGER PRIMARY KEY,
    competency TEXT,
    suggested_trainings TEXT,
    upskilling_reskilling TEXT
)
''')
conn.commit()


# Function to authenticate users
def authenticate_user(username, password):
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    return user

# Function to check if the user is an admin
def is_admin(user):
    admin_designations = ['Admin1', 'Admin2', 'Admin3']  # Add more designations as needed
    return user[4] in admin_designations

# Function to save data to the database
def save_data(user_id, competencies):
    c.execute('SELECT full_name FROM users WHERE id = ?', (user_id,))
    full_name = c.fetchone()[0]  # Assuming the user exists and has a full_name
    
    with conn:
        for competency in competencies:
            c.execute('''
            INSERT INTO elearning_preferences (
                user_id, full_name, select_competency, competency_level, upskilling_reskilling
            ) VALUES (?, ?, ?, ?, ?)''', 
            (user_id, full_name, competency['Competency'], competency['Competency Level'], competency['Upskilling/Reskilling']))
        conn.commit()

# Function to delete data from the database
def delete_data(user_id, competency_name):
    with conn:
        c.execute('DELETE FROM elearning_preferences WHERE user_id = ? AND select_competency = ?', (user_id, competency_name))
        conn.commit()



# Function to get supervisor details based on supervisor_name
def get_supervisor_details(supervisor_name):
    if supervisor_name:
        c.execute("SELECT supervisor_name, designation, division, department FROM supervisors_details WHERE supervisor_name = ?", (supervisor_name,))
        supervisor = c.fetchone()
        if supervisor:
            return {
                'name': supervisor[0],
                'designation': supervisor[1],
                'division': supervisor[2],
                'department': supervisor[3]
            }
    # Return N/A if no supervisor or no match found
    return {
        'name': 'N/A',
        'designation': 'N/A',
        'division': 'N/A',
        'department': 'N/A'
    }

# PDF generation class and functions
class PDF(FPDF):
    def __init__(self, orientation='P', unit='mm', format='Legal'):
        super().__init__(orientation, unit, format)
        self.header_printed = False

    def header(self):
        if not self.header_printed:
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'INDIVIDUAL DEVELOPMENT PLAN (LNA / IDP)', 0, 1, 'C')
            self.ln(5)
            self.header_printed = True

    def add_employee_details(self, employee_details):
        self.set_font('Arial', '', 12)
        self.cell(0, 8, f"Name of Employee: {employee_details['name']}", 0, 1)
        self.cell(0, 8, f"Position/Designation: {employee_details['position']}", 0, 1)
        self.cell(0, 8, f"Department: {employee_details['department']}", 0, 1)
        self.cell(0, 8, f"Division: {employee_details['division']}", 0, 1)
        self.cell(0, 8, f"Date & Time Generated: {employee_details['date']}", 0, 1)
        self.ln(5)

    def add_competencies(self, competencies):
        self.set_font('Arial', 'B', 10)
        self.cell(95, 8, 'Current competency', 1, 0, 'C')
        self.cell(95, 8, 'My current level', 1, 1, 'C')
        self.set_font('Arial', '', 10)
        for competency in competencies:
            self.cell(95, 8, str(competency['name']),'LR', 0,)
            self.cell(95, 8, str(competency['level']),'LR', 1, 'C')
        self.cell(190, 0, '', 'T', 1)
        self.cell(190, 10, '* Leadership Competencies', 0, 1, '')

    def add_learning_interventions(self, learning_interventions):
        self.set_font('Arial', 'B', 10)
        self.cell(190, 8, 'Suggested learning interventions to meet and address current competency gap', 1, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(95, 8, 'Training title', 1, 0, 'C')
        self.cell(95, 8, 'Competency to be addressed', 1, 1, 'C')

        for title, competency in learning_interventions:
            x = self.get_x()
            y = self.get_y()
            
            title_lines = self.get_string_width(title) // 95 + 1
            title_height = 3 * title_lines

            competency_lines = self.get_string_width(competency) // 95 + 1
            competency_height = 3 * competency_lines
            
            max_height = max(title_height, competency_height)
            
            self.multi_cell(95, 8, str(title), 'LTR', align='L')
            
            self.set_xy(x + 95, y)
            
            self.multi_cell(95, 8, str(competency), 'LTR', align='L')
            
            self.set_xy(x, y + max_height)
        
            self.cell(95, 8, '', 'LRB', 0)
            self.cell(95, 8, '', 'LRB', 1)
        self.ln(10)

    def add_training_preferences(self, upskilling_reskilling):
        self.set_font('Arial', 'B', 10)
        self.cell(190, 8, 'My preferred training for Upskilling/Reskilling that can help me improve my performance at work', 1, 1, 'C')
        self.set_font('Arial', '', 10)

        # Split the text into separate entries based on commas
        entries = upskilling_reskilling.split(', ')
    
        # Add each entry on a new line
        for entry in entries:
            self.multi_cell(190, 8, entry, 'LR', 1)
    
        self.cell(190, 0, '', 'T', 1)
        self.ln(10)

    def add_supervisor_remarks(self):
        self.set_font('Arial', 'B', 10)
        self.cell(190, 8, 'Supervisor remarks', 1, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(190, 24, '', 'LR', 1)
        self.cell(190, 0, '', 'T', 1)
        self.ln(10)

    def add_new_certification(self, supervisor_details, employee_name, employee_designation):
        self.set_font('Arial', '', 10)
        
        # Adding both certification statements side by side using multi_cell
        x = self.get_x()
        y = self.get_y()
        self.multi_cell(95, 6, "I certify that I was involved in the formulation of this development plan and agree with the identified activities that will be implemented in the next calendar year.", 0, 'C')
        self.set_xy(x + 95, y)
        self.multi_cell(95, 6, "I certify that this development plan has been formulated and discussed with the concerned employee.", 0, 'C')
        
        self.ln(10)
        # Adding employee and supervisor details
        self.set_font('Arial', 'B', 11)
        self.cell(95, 10, str(employee_name), 0, 0, 'C')
        self.cell(95, 5, str(supervisor_details['name']), 0, 1, 'C')
        # Removing the unnecessary newline
        self.set_font('Arial', '', 10)
        self.cell(95, 10, str(employee_designation), 0, 0, 'C')
        self.cell(95, 5, str(supervisor_details['designation']), 0, 1, 'C')
        # Combine division and department into one line without extra spaces
        self.cell(95, 5, '', 0, 0, 'C')  # Empty cell for alignment
        self.cell(95, 5, f"{supervisor_details['division']} {supervisor_details['department']}", 0, 1, 'C')

        self.ln(10)
        self.cell(190, 10, 'Approved by:', 0, 1, 'C')
        self.ln(5)
        self.ln(0)
        self.set_font('Arial', 'B', 11)
        self.cell(190, 10, 'JESUS ENRICO MOISES B. SALAZAR', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(190, 1, 'General Manager', 0, 1, 'C')

def create_marksheet_pdf(output_stream, employee_details, competencies, supervisor_details, upskilling_reskilling):
    pdf = PDF()
    pdf.add_page()
    pdf.add_employee_details(employee_details)
    pdf.add_competencies(competencies)
    
    c.execute('''
    SELECT suggested_trainings, competency FROM competencies WHERE competency IN ({})
    '''.format(','.join('?'*len(competencies))), [comp['name'] for comp in competencies])
    learning_interventions = [(row[0], row[1]) for row in c.fetchall() if row[0]]
    
    pdf.add_learning_interventions(learning_interventions)
    pdf.add_training_preferences(upskilling_reskilling)
    pdf.add_supervisor_remarks()
    pdf.add_new_certification(supervisor_details, employee_details['name'], employee_details['position'])

    # Output the PDF to the BytesIO stream
    pdf_data = pdf.output(dest='S').encode('latin1')
    output_stream.write(pdf_data)
    output_stream.seek(0)

def generate_marksheet(data, filename, employee_details, upskilling_reskilling):
    competencies = [{'name': row['Competency'], 'level': row['Competency Level']} for index, row in data.iterrows()]
    supervisor_details = get_supervisor_details(employee_details['supervisor_name'])
    output_path = os.path.join(os.getcwd(), filename)
    with open(output_path, 'wb') as f:
        create_marksheet_pdf(f, employee_details, competencies, supervisor_details, upskilling_reskilling)
    return output_path

# Function to generate PDF and return it as a BytesIO object
def generate_marksheet_pdf_bytes(user_data, employee_details, upskilling_reskilling):
    competencies = [{'name': row['Competency'], 'level': row['Competency Level']} for index, row in user_data.iterrows()]
    supervisor_details = get_supervisor_details(employee_details['supervisor_name'])
    
    pdf_output = BytesIO()
    create_marksheet_pdf(pdf_output, employee_details, competencies, supervisor_details, upskilling_reskilling)
    return pdf_output

# Apply custom CSS for background color and warning message
st.markdown("""
    <style>
    .stApp {
        background-color: ;
    }
    .warning {
        font-size: 20px;
        color: black;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit App Logic
if not st.session_state.logged_in:
    st.sidebar.title('Login')
    logo_path = r"D:\PY Projects\LNA\LCWD Logo.jpg"
    st.sidebar.image(logo_path, use_column_width=False)
    st.warning('Please Login to access the LNA survey')
    username = st.sidebar.text_input('Username', key='login_username')
    password = st.sidebar.text_input('Password', type='password', key='login_password')
    login_button = st.sidebar.button('Login', key='login_button')
    
    if login_button:
        user = authenticate_user(username, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.user_id = user[0]
            st.session_state.username = username
            st.session_state.full_name = user[2]
            st.session_state.designation = user[4]
            st.session_state.department = user[5]
            st.session_state.division = user[6]
            st.session_state.supervisor_name = user[7]  # Save supervisor name in session state
            if user[7]:  # If OIC_dept_div exists
                st.session_state.oic_dept_div = user[7]
            st.session_state.is_admin = is_admin(user)
            st.session_state.display_welcome_back = True
            st.rerun()
        else:
            st.sidebar.error('Invalid username or password')
else:
    if st.session_state.is_admin:
        st.sidebar.success(f'Logged in as ADMIN {st.session_state.full_name}')
    else:
        st.sidebar.success(f'Logged in as {st.session_state.full_name}')
        
    if st.sidebar.button('Logout'):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.session_state.survey_started = False
        st.session_state.competencies = []
        st.session_state.show_input_fields = False
        st.session_state.new_competencies = False
        st.session_state.add_competency_clicked = False
        st.session_state.display_welcome_back = True
        st.session_state.hide_saved_data = False
        st.session_state.intro_hidden = False
        st.rerun()

    # Unified PDF Generation
    def generate_employee_marksheet(df, full_name):
        selected_user_data = df[df['Full Name'] == full_name]
        now = datetime.now().strftime('%m/%d/%Y @ %I:%M:%S %p')
        employee_details = {
            'name': full_name,
            'position': selected_user_data['Designation'].iloc[0],
            'department': selected_user_data['Department'].iloc[0],
            'division': selected_user_data['Division'].iloc[0],
            'supervisor_name': selected_user_data['Supervisor Name'].iloc[0],
            'date': now,
        }
        pdf_bytes = generate_marksheet_pdf_bytes(selected_user_data, employee_details, ', '.join(selected_user_data['Upskilling/Reskilling'].dropna()))
        return pdf_bytes

    # Navigation bar for Admin users
    if st.session_state.is_admin:
        st.title('Admin Dashboard')
        selected_option = option_menu(
            menu_title=None,
            options=["Stored Data", "Data Visualization", "Data Analysis"],
            icons=["database", "bar-chart", "activity"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
        )

        
        if selected_option == "Stored Data":
            st.markdown("## Stored Data")
            
            
            @st.cache_data(ttl=600)    
            def get_user_data():
            # Define the current datetime
                now = datetime.now().strftime('%m/%d/%Y @ %I:%M:%S %p')
            
            query = '''
            SELECT u.id, u.full_name, u.department, u.division, u.designation, u.supervisors_name, e.select_competency, e.competency_level, e.upskilling_reskilling
            FROM users u
            JOIN elearning_preferences e ON u.id = e.user_id
            '''
            c.execute(query)
            rows = c.fetchall()
            df = pd.DataFrame(rows, columns=["User ID", "Full Name", "Department", "Division", "Designation", "Supervisor Name", "Competency", "Competency Level", "Upskilling/Reskilling"])

            user_count = df['Full Name'].nunique()  # Count unique full names
            department_count = df['Department'].nunique() - 1  # Count unique departments, excluding the column name
            division_count = df['Division'].nunique()  # Count unique divisions, excluding the column name


            # Display DataFrame of stored data
            if not df.empty:
                st.dataframe(df)
            else:
                st.write("No stored data available.")
            
            # Display selectbox with full names
            full_name = st.selectbox('Select a User to Generate Marksheet', df['Full Name'].unique())
            
            # Get the selected user's data after selecting a user
            selected_user_data = df[df['Full Name'] == full_name]

            # Correctly fetch supervisor details using the user's supervisor name
            supervisor_name = selected_user_data['Supervisor Name'].iloc[0]
            supervisor_details = get_supervisor_details(supervisor_name)

            # Prepare employee details
            employee_details = {
                'name': full_name,
                'position': selected_user_data['Designation'].iloc[0],
                'department': selected_user_data['Department'].iloc[0],
                'division': selected_user_data['Division'].iloc[0],
                'supervisor_name': supervisor_name,
                'date': now,
            }

            # Layout with two columns
            col1, col2 = st.columns([1, 1])
            
            with col1:
                # Display the Generate Marksheet PDF button
                if st.button('Generate Marksheet PDF'):
                    # Generating the PDF
                    pdf_bytes = generate_marksheet_pdf_bytes(selected_user_data, employee_details, ', '.join(selected_user_data['Upskilling/Reskilling'].dropna()))
                    st.warning('Marksheet PDF has been generated')
                    
                    # Provide download link
                    st.download_button(
                        label="Download Marksheet PDF",
                        data=pdf_bytes.getvalue(),
                        file_name=f"{full_name}_marksheet.pdf",
                        mime="application/pdf"
                    )
            
            with col2:
                st.markdown(f"""
                    <style>
                        .compact-row {{
                            line-height: 1.2;
                        }}
                        .bold-text {{
                            font-weight: bold;
                        }}
                    </style>
                    <div class="compact-row">Total number of employees: <span class="bold-text">{user_count}</span></div>
                    <div class="compact-row">Department: <span class="bold-text">{department_count}</span></div>
                    <div class="compact-row">Division: <span class="bold-text">{division_count}</span></div>
                """, unsafe_allow_html=True)

        elif selected_option == "Data Visualization":
            @st.cache_data(ttl=600)    
            def get_user_data():
                st.markdown("## Data Visualization")
                query = '''
                SELECT u.department, u.division, e.select_competency AS "Competency", e.competency_level AS "Competency Level"
                FROM users u
                JOIN elearning_preferences e ON u.id = e.user_id
                '''
                c.execute(query)
                rows = c.fetchall()
                df = pd.DataFrame(rows, columns=["Department", "Division", "Competency", "Competency Level"])

            if not df.empty:
                group_by_option = st.selectbox("Group data by:", ["Department", "Division"])
            
                if group_by_option == "Department":
                    grouped_df = df.groupby(["Department", "Competency"])["Competency Level"].count().reset_index()
                    grouped_df = grouped_df.pivot(index="Competency", columns="Department", values="Competency Level").fillna(0)
                else:
                    grouped_df = df.groupby(["Division", "Competency"])["Competency Level"].count().reset_index()
                    grouped_df = grouped_df.pivot(index="Competency", columns="Division", values="Competency Level").fillna(0)
                
                st.dataframe(grouped_df)

                fig, ax = plt.subplots(figsize=(10, 6))
                grouped_df.plot(kind='bar', stacked=True, ax=ax)
                plt.xticks(rotation=45, ha='right')
                plt.xlabel("Competency")
                plt.ylabel("Count")
                plt.title(f"Competencies by {group_by_option}")
                st.pyplot(fig)
            else:
                st.warning("No data available for visualization.")

        elif selected_option == "Data Analysis":
            @st.cache_data(ttl=600)    
            def get_user_data():
                st.markdown("## Data Frame for Analysis")
                
                query = '''
                SELECT u.id, u.full_name, u.department, u.division, u.designation, e.select_competency, e.competency_level
                FROM users u
                JOIN elearning_preferences e ON u.id = e.user_id
                '''
                c.execute(query)
                rows = c.fetchall()
                df = pd.DataFrame(rows, columns=["User ID", "Full Name", "Department", "Division", "Designation", "Competency", "Competency Level"])
                st.write(df)

    
            import sys
            # Ensure any previous instances of the openai module are removed
            if 'openai' in sys.modules:
                del sys.modules['openai']

            # Re-import the openai module
            import openai
            
            # OpenAI API key
            open.api_key = ""

            # Function to make API call
            def generate_analysis(dataframe):
                # Serialize the DataFrame to a string representation for the prompt
                df_str = dataframe.to_string(index=False)
                prompt = f"Based on the dataframe, generate a data analysis narrative:\n\n{df_str}"
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=150,
                    n=1,
                    stop=None,
                    temperature=0.7
                )
                return response.choices[0].text.strip()

            # Streamlit button and display logic
            if st.button("Generate Data Analysis"):
                analysis = generate_analysis(df)
                st.write("### Data Analysis Narrative")
                st.write(analysis)    


    if st.session_state.logged_in:
    # @st.cache_data(ttl=600)    
    # def get_user_data():
        if not st.session_state.is_admin:
            # Adding a line border instead of a heading
            st.sidebar.markdown("<hr style='border: 1px solid #d3d3d3;'>", unsafe_allow_html=True)
            
            user_data = pd.read_sql_query(f'''
            SELECT e.select_competency AS "Competency", e.competency_level AS "Competency Level", e.upskilling_reskilling AS "Upskilling/Reskilling"
            FROM elearning_preferences e
            WHERE e.user_id = {st.session_state.user_id}
            ''', conn)
            
            if not user_data.empty:
                now = datetime.now().strftime('%m/%d/%Y @ %I:%M:%S %p')
                employee_details = {
                    'name': st.session_state.full_name,
                    'position': st.session_state.designation,
                    'department': st.session_state.department,
                    'division': st.session_state.division,
                    'supervisor_name': st.session_state.supervisor_name,
                    'date': now,
                    'OIC_dept_div': st.session_state.oic_dept_div if 'oic_dept_div' in st.session_state else None
                }
                
                pdf_bytes = generate_marksheet_pdf_bytes(user_data, employee_details, ', '.join(user_data['Upskilling/Reskilling'].dropna()))
                st.sidebar.download_button(
                    label="Download my generated LNA",
                    data=pdf_bytes.getvalue(),
                    file_name=f"{st.session_state.full_name}_marksheet.pdf",
                    mime="application/pdf"
                )

    query = '''
    SELECT select_competency FROM elearning_preferences WHERE user_id = ?
    '''
    c.execute(query, (st.session_state.user_id,))
    user_competencies = c.fetchall()
    user_competencies = [item[0] for item in user_competencies]

    if st.session_state.logged_in:
        if not st.session_state.is_admin:
            query = '''
            SELECT e.select_competency AS "Competency", e.competency_level AS "Competency Level", e.upskilling_reskilling AS "Upskilling/Reskilling"
            FROM elearning_preferences e
            WHERE e.user_id = ?
            '''
            c.execute(query, (st.session_state.user_id,))
            user_rows = c.fetchall()
            user_df = pd.DataFrame(user_rows, columns=["Competency", "Competency Level", "Upskilling/Reskilling"])

            st.title('LCWD Individual Training Development Needs Survey')

            if not st.session_state.add_competency_clicked:
                if not user_df.empty and not st.session_state.hide_saved_data:
                    if st.session_state.display_welcome_back:
                        st.write(f"Welcome back, {st.session_state.full_name}!")
                        st.session_state.display_welcome_back = False
                    st.markdown("## Your Saved Data")
                    if st.button('Generate my LNA/IDP'):
                        now = datetime.now().strftime('%m/%d/%Y @ %I:%M:%S %p')
                        employee_details = {
                            'name': st.session_state.full_name,
                            'position': st.session_state.designation,
                            'department': st.session_state.department,
                            'division': st.session_state.division,
                            'supervisor_name': st.session_state.supervisor_name,
                            'date': now,
                            'OIC_dept_div': st.session_state.oic_dept_div if 'oic_dept_div' in st.session_state else None
                        }
                        pdf_path = generate_marksheet(user_df, f"{st.session_state.full_name}_marksheet.pdf", employee_details, ', '.join(user_df['Upskilling/Reskilling'].dropna()))
                        webbrowser.open(f"file://{pdf_path}")
                        st.success(f"Marksheet PDF generated: {pdf_path}")

                    st.dataframe(user_df)

                    selected_competency = st.selectbox('Remove Your Save Data', user_competencies, key='delete_competency')
                    if st.button('Delete'):
                        delete_data(st.session_state.user_id, selected_competency)
                        st.success(f'Competency "{selected_competency}" deleted successfully.')
                        st.rerun()

                        query = '''
                        SELECT COUNT(*) FROM elearning_preferences WHERE user_id = ?
                        '''
                        c.execute(query, (st.session_state.user_id,))
                        remaining_data = c.fetchone()[0] > 0
                        if not remaining_data:
                            st.session_state.add_competency_clicked = False
                            st.session_state.hide_saved_data = False
                            st.warning('Please logout to access again the LNA Survey')
                            st.rerun()

                if not st.session_state.show_input_fields:
                    if user_df.empty:
                        if not st.session_state.intro_hidden:
                            st.write(f"Welcome, {st.session_state.full_name}")
                            st.write('<div style="text-align: justify">We are currently identifying the learning and development needs of LCWDs employees, the result of this survey will be critical in identifying learning and development interventions that are responsive to your competency needs and the goals of our agency.</div>', unsafe_allow_html=True)
                            st.text("")
                            st.write('<div style="text-align: justify">Kindly provide time to accomplish and complete this Learning Needs Analysis (LNA) survey as accurately and honestly as possible. It is important in creating our learning and development plan and assists you to achieve success in your current job role. The information that will be gathered will also help the Human Resource (HR) Section in identifying training priorities in providing the best training that specifically meets your specific needs and develop targeted competencies to support organizational goals. It is recommended that supervisors and staff members only choose a maximum of ten job-related competencies that are vital in achieving your current duties to set limits in the budget appropriation for the training expense. The results of this entire survey are confidential and will only be shared with HR personnel that will be solely used for developmental purposes.<div>', unsafe_allow_html=True)
                            st.text("")            
                            st.write('<div style="text-align: justify">If you are ready to take the survey kindly click the Start LNA Survey below. Thank you.</div>', unsafe_allow_html=True)
                            st.text("")
                            st.text("")
                            if st.button('Start LNA Survey'):
                                st.session_state.survey_started = True
                                st.session_state.show_input_fields = True
                                hide_intro()  # Hide the introduction after starting the survey
                                st.rerun()
                    
                    else:
                        st.write("Would you like to add additional competency to your stored data?")
                        if st.button('Add More Competency'):
                            st.session_state.show_input_fields = True
                            st.session_state.add_competency_clicked = True
                            st.session_state.hide_saved_data = True
                            hide_intro()  # Hide the introduction after clicking Add More Competency
                            st.rerun()

            if st.session_state.show_input_fields or st.session_state.add_competency_clicked:
                st.write('<div style="text-align: justify">All identified current competencies for LCWDs employees including leadership competencies* are provided with their respective definition.</div>', unsafe_allow_html=True)
                st.text("")
                with st.expander("View LCWD's identified competencies"):
                    st.markdown("""**Accounting**: The ability to record, analyze, classify, summarize and interprets financial transactions to be able to prepare for a sound financial report and manage the accounts of the organization.""")
                    st.markdown("""**Accounts Reconciliation**: The ability to carry out timely and accurate reconciliation of accounting control statements, including bank reconciliations, control accounts, revenue reconciliations, advances, and deposits.""")
                    st.markdown("""**Air-Conditioning Servicing**: Explain basic principles of electrical and mechanical aspects of the Air-Conditioning Unit to safely install, commission, service and maintain air conditioning system.""")
                    st.markdown("""**Applying Internal Control Functions**: Has the ability to integrate effective design and develop financial management system that address issues related to financial management and operations to safeguard government assets, check the accuracy and reliability of accounting data, adhere to management policies, comply with laws and regulations and ensure efficient, ethical and economical operations.""")
                    st.markdown("""**AutoCAD**: The ability to operate software programs to create technical two-dimensional (2D) and three-dimensional (3D) designs.""")
                    st.markdown("""**Automotive Servicing**: Effectively achieve to inspect, clean and repair mechanical or electrical parts, components, assemblies and sub-assemblies of light and heavy-duty automotive vehicle with diesel or gas engine in accordance with manufacturer’s specification. It also covers servicing of engine mechanical components such as cooling and lubricating system and underchassis servicing and repair.""")
                    st.markdown("""**Benefits, Compensation and Welfare Management**: The ability to develop, implement, evaluate and enhance policies and programs on benefits, compensation, rewards, incentives, health and wellness to improve employee welfare.""")
                    st.markdown("""**Budget Management**: Effective preparation of budget plans using the latest budgeting techniques, and preparation of budget submissions by agency based on policies.""")
                    st.markdown("""**Carpentry Skill**: Has the ability to perform stake-out building lines, fabricate formworks, install/strip form works, install framing works, install architectural ceiling/wall sheats/panels and floor finishes and fabricate/install door/window jambs and panels.""")
                    st.markdown("""**Cash Management**: The ability to collect and manage assessment and usage of cash flow to ensure the financial stability and solvency of an organization.""")
                    st.markdown("""**Chlorine Handling Skills**: Has the fundamental knowledge to be able to safely use and handle chlorine and other chemical solutions in the District’s water treatment facilities.""")
                    st.markdown("""**Computer Skills**: The ability to operate standard personal computer and use available computer software, applications and technology.""")
                    st.markdown("""**Conduct Audit Assignments**: Using an audit methodology that is consistent with international standards on public sector audit for selecting a process for audit, planning an audit assignment, documenting a process, assessing risks and controls in a process, assessing the performance of processes, identifying control gaps, conducting audit tests, and accurately recording audit work.""")
                    st.markdown("""**Customer Complaints Management**: Has the ability to use proper channels to deal with customer complaints effectively to improve customer retention.""")
                    st.markdown("""**Data Collection from Utility Meters**: Demonstrate proficiency in using handheld devices and conduct accurate records of reading meters.""")
                    st.markdown("""**Data Management**: The ability to analyze statistics and other data by interpreting and evaluating the results to be able to formulate a report and/or presentation as reference for decision making.""")
                    st.markdown("""**Delivering Service Excellence**: The ability to provide proactive, responsive, accessible, courteous and effective public service to attain the highest level customer satisfaction.""")
                    st.markdown("""**Digital Media and Visualisation**: The ability to convey ideas and information in forms such as audio, text, pictures, diagrams, video, photos, maps and 3D models.""")
                    st.markdown("""**Drafting Construction Drawings**: The ability to draft precise and detailed planning design for building and infrastructure project within the criteria set in conformance with the structural codes and standards.""")
                    st.markdown("""**Drafting Electrical Layouts**: The ability to draft precise and detailed electrical layout plan for the electrical wiring within the criteria set in conformance with the electrical codes and standards.""")
                    st.markdown("""**Driving**: Capable to operate motor vehicles classified under LTO Restriction with compliance to local traffic rules and regulations and perform minor vehicle repairs and other minor servicing.""")
                    st.markdown("""**Electrical Installation**: Has the capability to install and maintain electrical wiring, lighting and related equipment and systems where the voltage does not exceed the required voltage in building establishment.""")
                    st.markdown("""**Electronics and Electrical Equipment Servicing**: Has the ability to conduct maintenance and repair of electronic products and service appliances.""")
                    st.markdown("""**Environmental Compliance**: Has the ability to identify, define, develop, evaluate and improve systems, processes and procedures that ensures constant compliance of the project proponents, local government and its partner agencies/organizations in the implementation of projects, programs and activities related to and/or has adverse impact directly or indirectly to environment and natural resources.""")
                    st.markdown("""**Facilities Management**: Has the ability to maintain and improve office facilities or properties in order to ensure minimal disruption of business operations.""")
                    st.markdown("""**Heavy Equipment Operation Skill**: Demonstrate competency on operating heavy equipment according to procedures, specifications and manual of instruction.""")
                    st.markdown("""**Housekeeping**: Has the ability to maintain cleanliness of public areas, equipment and promote workplace hygiene procedures in providing housekeeping services.""")
                    st.markdown("""**Information Technology Management**: Demonstrate skills and working knowledge in Information Technology Management. Applies technical skills and demonstrates knowledge of emerging technology (e.g. IT processes, methodologies, etc.).""")
                    st.markdown("""**Inventory Management and Stock Control**: Has the ability to record and manage inventory which typically covers the receipt and custody of items procured, ensuring just-in-time distribution when needed, safe maintenance of stocks, monitoring of re-order point and disposal of unnecessary stocks.""")
                    st.markdown("""**Learning and Development Planning**: The ability to translate training/learning needs results into interventions and prioritize them for implementation.""")
                    st.markdown("""**Learning Measurement and Evaluation**: The ability to determine training/learning needs and evaluate its effectiveness.""")
                    st.markdown("""**Legal Management**: The ability to provide legal assistance and oversee all legal matters within the organization.""")
                    st.markdown("""**Liquidity, Debts and Investment Management**: Has the ability to develop strategies in ensuring liquidity, debt and investment management to cover payments against all vouchers, and undertake investment programs in times of cash surplus.""")
                    st.markdown("""**Management of Accounts Receivable**: Ensuring the monitoring of timely payment of receivables and provide strategic initiatives for the improvement and more efficient accounts receivable management system.""")
                    st.markdown("""**Market Analysis**: Has the ability to gather and analyze data related to potential target consumers that will help generate revenues in the agency.""")
                    st.markdown("""**Masonry**: Has the ability to perform construction of brick and concrete block structure, installation of pre-cast balluster/handrail and plastering of concrete wall surface.""")
                    st.markdown("""**Meter Maintenance / Calibration**: Has the knowledge of calibration procedures and the ability to troubleshoot water meters within the prescribed standards.""")
                    st.markdown("""**Metal Arc Welding**: Has the ability to perform weld carbon steel plate and pipe components as specified by layout, blueprints, diagrams, work order, welding procedure or oral instructions using shielded metal arc welding equipment.""")
                    st.markdown("""**Monitoring and Evaluating**: Gathering and evaluating information to determine whether or not the on-going activities of a program are in line with intended direction or results.""")
                    st.markdown("""**Negotiation Skills**: Has the ability to adopt appropriate techniques for negotiating resistance and objections in order to negotiate to a desired outcome.""")
                    st.markdown("""**Network, Telecommunication, Wireless and Mobility Knowledge**: The ability to demonstrate expertise on processes, hardware, and software employed to facilitate communication between people computer systems and devices.""")
                    st.markdown("""**Non-Revenue Water Management**: Has the ability to identify leakages and provide strategic initiatives to address the reduction of non-revenue water.""")
                    st.markdown("""**Occupational Safety and Health**: Has the awareness to practice, evaluate, lead, establish and manage Occupational Safety and Health programs in the workplace.""")
                    st.markdown("""**Oral Communication**: Makes clear and convincing oral presentations to individual or groups; listens effectively and clarifies information as needed.""")
                    st.markdown("""**Organizational and Procurement Planning**: The ability to effectively undertake procurement planning, programming, project management, and requirement specifications to facilitate achievement of organisational or agency program of work, goals and targets within the specific acceptable timetable and budget.""")
                    st.markdown("""**Pipe-Fitting**: Has the ability to cut, bevel, and / or thread pipes, and install overhead and underground piping system.""")
                    st.markdown("""**Planning and Delivering**: The ability to prioritize and identify scope and allocate resources to meet individual, team, or organization targets and objectives.""")
                    st.markdown("""**Plumbing-Service Connection**: Has the capability of installing multiple units of plumbing system with multi-point hot-and-cold-water lines which also includes plumbing repair and maintenance works.""")
                    st.markdown("""**Plumbing-Distribution System**: Has the capability of installing and connecting network pipes in the water distribution system which also includes distribution and mainline repair.""")
                    st.markdown("""**Policy Evaluation**: The ability to measure and assess the appropriateness, effectiveness and efficiency of human resource policies, contributing to policy improvements and innovation.""")
                    st.markdown("""**Preparation of Expenditure Program**: The production of the monthly expenditure program (monthly flow), forecast by object allotment class (Personnel Services, MOOE and Capital Expenditure) using all relevant and available historical data to the highest degree of accuracy possible.""")
                    st.markdown("""**Preparation of Revenue Program**: Forecasting the monthly revenue program using all relevant and available historical data with the highest degree of accuracy possible.""")
                    st.markdown("""**Preparing Feasibility Studies**: The ability to systematically gather and analyse relevant information pertaining to some programs aimed at advancing and achievement the strategic agenda of the agency.""")
                    st.markdown("""**Pressure Management**: The ability to effectively regulate water pressure within water networks in ensuring the efficient and sustainable distribution of water supply.""")
                    st.markdown("""**Procurement Management**: The ability to plan and implement measures to acquire supplies and properties at the best possible cost; that meets the quality, quantity and timeliness requirement of the organization; and are compliant to procurement policies.""")
                    st.markdown("""**Procurement Market Analysis**: The ability to adopt strategies in identifying competition and market-segmentation prior to procurement in order to secure economic advantage.""")
                    st.markdown("""**Procurement Planning**: The ability to effectively undertake procurement planning according to the approved Annual Procurement Plan in order to facilitate the achievement of the agency’s program of work, goals and targets.""")
                    st.markdown("""**Program / Course Delivery and Administration**: The ability to plan, execute and report the implementation of training/learning interventions, courses and programs.""")
                    st.markdown("""**Project / Program Management**: The ability to monitor and coordinate the implementation of plans, policies, tasks and activities of programs and projects being undertaken by the stakeholder, and taking action to meet quality and performance goals.""")
                    st.markdown("""**Public Relation Management**: The ability to build, maintain and manage engagement and goodwill between the organization and the public through the installation of assistance and complaint mechanisms and the implementation of special programs.""")
                    st.markdown("""**Pump Operation**: The ability to monitor and maintain the pumping equipment and facilities in order to ensure maximum efficiency of its operations.""")
                    st.markdown("""**Quality Management and Assurance**: Performs tasks in ensuring that products or services consistently meet the prescribed government standards or within the prescribed contract agreement by other private institution.""")
                    st.markdown("""**Records Management**: The ability to apply and adapt records management standards related to the cycle of records in an agency/institution which are conducted to achieve adequate and proper documentation of government policies, transactions and effective management of the agency’s operations.""")
                    st.markdown("""**Recruitment, Selection and Placement**: The ability to search, attract, and assess job candidates and to guide the appointing authority in choosing the best fit for the job at the right time, in accordance with legal requirements in order to achieve organizational goals.""")
                    st.markdown("""**Rewards and Recognition**: The ability to identify, develop and implement programs for the organization/bureaucracy to reward and recognize outstanding performance and behavior.""")
                    st.markdown("""**Supervisory Control and Data Acquisition (SCADA) Operation**: The ability to develop a SCADA application and to use SCADA systems in the agency’s operation.""")
                    st.markdown("""**Strategic Planning**: The ability to influence, realign the organization's strategic goals and directions; monitor and review data from various aspects of strategic and corporate planning and recommend enhancements.""")
                    st.markdown("""**Stress Management**: The ability to apply techniques to cope with or lessen the physical and emotional effects of everyday life pressure in the workplace.""")
                    st.markdown("""**Supplier Management and Contract Agreement**: Has the ability to manage suppliers in order to ensure continuing provision of goods and services. Manage contract implementation and ensure fair, open and transparent dealings with existing and potential suppliers.""")
                    st.markdown("""**Supplies and Property Management**: The ability to plan and implement measures to efficiently allocate, utilize, maintain and dispose supplies and properties of the organization.""")
                    st.markdown("""**Taxation**: Has the ability to interpret, understand and manage various aspects of Philippine Tax laws.""")
                    st.markdown("""**User and Customer Support**: The ability to provide services, assistance, and technical support to help users implement and solve problems related to information technology.""")
                    st.markdown("""**Writing Effectively**: The ability to write in clear, concise and coherent manner using different tools to convey information or express ideas effectively.""")
                    
                    #Leadership Competencies
                    st.markdown(bold_label('<div style="text-align: Center">Leadership Competencies*</div>'), unsafe_allow_html=True)
                    st.markdown("""**Thinking Strategically and Creatively**: The ability to “see the big picture”, think multi-dimensionally, craft innovative solutions, identify connections between situations or things that are not obviously related, and come up with new ideas and different ways to enhance organizational effectiveness and responsiveness.""")
                    st.markdown("""**Leading Change**: The ability to generate genuine enthusiasm and momentum for organizational change. It involves engaging and enabling groups to understand, accept and commit to the change agenda. It also includes advancing and sustaining change.""")
                    st.markdown("""**Building Collaborative, Inclusive Working Relationship**: The ability to build and maintain a network of reciprocal, high trust, synergistic working relationships within the organization and across government and relevant sectors. This involves the ability to successfully leverage and maximize opportunities for strategic influencing within the organization and with external stakeholders.""")
                    st.markdown("""**Managing Performance and Coaching Results**: The ability to create an enabling environment which will nurture and sustain a performance-based, coaching culture. Effectiveness in this competency area also includes a strong focus on developing people for current and future needs, managing talent, promoting the value of continuous learning and improvement.""")
                    st.markdown("""**Creating and Nurturing a High Performance Organisation**: The ability to create a high performing organizational culture that is purpose-driven, results-based, client-focused and team-oriented.""")
                    st.markdown("""**Performance Management**: The ability to collect, analyze, review and report performance data and establish scientific basis for performance targets and measures.""")

                if st.session_state.show_input_fields or st.session_state.add_competency_clicked:
                    st.write('<div style="text-align: justify">For the LCWD, we have selected a four-level scale of proficiency level for each competency where it is generally described in terms of behavioral indicators (e.g. Scope/Context, Complexity and Autonomy/Responsibility).</div>', unsafe_allow_html=True)
                    st.text("")
                with st.expander("View Proficiency Level Table"):
                    st.write("""
                    | Progression Criteria  | Level 1 Basic                                   | Level 2 Intermediate                      | Level 3 Advanced                                             | Level 4 Superior                                             |
                    |-----------------------|-----------------------------------------------|-------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------|
                    | Core Description      | Requires guidance or assistance of peer or supervisor to apply the competency. | Applies the competency with minimal supervision. | Develops new or enhances existing processes, procedures, and policies. | Integrates efforts of one or more practitioners and recommends improvements on policies, programs, and regulations. |
                    | SCOPE / CONTEXT       | Limited to own tasks and requires full supervision to perform duties and responsibilities. Competency is at a level where specific procedures are observed. | Limited to own tasks and requires some supervision and further training. Competency is at a level where specific procedures are observed. | Generally confined in own set of tasks, but has tasks that require working with others, with some activities not necessarily covered by procedures. | Covers/integrates work of different individuals/work groups, multiple tasks, diverse work units, varied situations. |
                    | COMPLEXITY (Task - Based to Strategic) | Demonstrates an understanding of only the most basic concepts contained | Demonstrates an understanding of the fundamental concepts involved | Demonstrates a solid understanding of core concepts within this competency. Appears | Demonstrates a clear understanding of many advanced concepts within this |
                    | Autonomy and Responsibility | No decision making authority and must be completely supervised in all tasks | No decision making authority, moderately supervised and can follow basic standards and procedures of work. | Most tasks /activities can be done independently given clear directions, standards and procedures of work, requires consultation for non-familiar, non-routine tasks/situations. | Independent work covering responsibility for others' work.
                    """)

                st.markdown("""<style>.stSelectbox {margin-top: -20px;}.stSelectbox > div > div {padding-top: 0rem;}.stSelectbox label {margin-bottom: 0rem;}</style>""", unsafe_allow_html=True)
                st.markdown(bold_label('Select Competency'), unsafe_allow_html=True)
                select_competency = st.selectbox('-', list(competency_descriptions.keys()), key='select_competency')
                if select_competency:
                    competency_info = competency_descriptions[select_competency]
                    st.markdown(f"**Description**: {competency_info['Description']}")

                st.markdown("""<style>.stSelectbox {margin-top: -20px;}.stSelectbox > div > div {padding-top: 0rem;}.stSelectbox label {margin-bottom: 0rem;}</style>""", unsafe_allow_html=True)
                st.markdown(bold_label('My Level for this Competency'), unsafe_allow_html=True)
                competency_level = st.selectbox(' ', ['Basic', 'Intermediate', 'Advanced', 'Superior', 'Not yet acquired'], key='competency_level')

                st.markdown("""<style>.stTextArea {margin-top: -20px;padding-top: 0rem;margin-bottom: 0rem;}.stTextArea > div > div {padding-top: 0rem;}</style>""", unsafe_allow_html=True)
                st.markdown(bold_label('My Preferred Training for Upskilling/Reskilling'), unsafe_allow_html=True)
                upskilling_reskilling = st.text_area('-', key='upskilling_reskilling')

                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button('Add this competency'):
                        if not st.session_state.select_competency:
                            st.warning("You have not selected a competency. Please select one from the dropdown.")
                        else:
                            st.session_state.competencies.append({
                                'Competency': st.session_state.select_competency, 
                                'Competency Level': st.session_state.competency_level,
                                'Upskilling/Reskilling': st.session_state.upskilling_reskilling
                            })
                            st.session_state.new_competencies = True
                            st.session_state.add_competency_clicked = False
                            st.session_state.show_input_fields = False  # Hide input fields after adding competency
                            hide_intro()  # Hide the introduction after adding competency
                            st.rerun()

                with col2:
                    if st.button('Reset Selection', on_click=reset_selection):
                        st.rerun()

            if st.session_state.new_competencies:                
                st.write("Do you want to include this in the list of your Learning Needs?")
                competencies_df = pd.DataFrame(st.session_state.competencies, columns=["Competency", "Competency Level", "Upskilling/Reskilling"])
                st.dataframe(competencies_df)

                col1, col2 = st.columns([1, 1])
                
                with col1:
                    if st.button('Save'):
                        save_data(st.session_state.user_id, st.session_state.competencies)
                        st.success('Information saved successfully!')
                        st.session_state.competencies = []  # Clear the competencies list after saving
                        st.session_state.new_competencies = False
                        st.session_state.show_input_fields = False
                        st.session_state.hide_saved_data = False
                        st.rerun()

                with col2:
                    if st.button('Return to LNA Survey'):
                        st.session_state.competencies = []  # Clear the competencies list
                        st.session_state.new_competencies = False  # Hide the dataframe and buttons
                        st.session_state.show_input_fields = True
                        st.session_state.hide_saved_data = True
                        st.rerun()

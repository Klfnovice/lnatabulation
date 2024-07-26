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
        "Description": "The ability to record, analyze, classify, summarize and interprets financial transactions to be able to prepare for a sound financial report and manage the accounts of the organization.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
    
    "Accounting Reconciliation": 
        {
        "Description": "The ability to carry out timely and accurate reconciliation of accounting control statements, including bank reconciliations, control accounts, revenue reconciliations, advances, and deposits.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
    
    "Air-Conditioning Servicing":
        {
        "Description": "Explain basic principles of electrical and mechanical aspects of the Air-Conditioning Unit to safely install, commission, service and maintain air conditioning system.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Applying Internal Control Functions":
        {
        "Description": "Has the ability to integrate effective design and develop financial management system that address issues related to financial management and operations to safeguard government assets, check the accuracy and reliability of accounting data, adhere to management policies, comply with laws and regulations and ensure efficient, ethical and economical operations.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
    
    "AutoCAD":
        {
        "Description": "The ability to operate software programs to create technical two-dimensional (2D) and three-dimensional (3D) designs.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
    
    "Automotive Servicing":
        {
        "Description": "Effectively achieve to inspect, clean and repair mechanical or electrical parts, components, assemblies and sub-assemblies of light and heavy-duty automotive vehicle with diesel or gas engine in accordance with manufacturer’s specification. It also covers servicing of engine mechanical components such as cooling and lubricating system and underchassis servicing and repair.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Benifits, Compensation and Welfare Management":
        {
        "Description": "The ability to develop, implement, evaluate and enhance policies and programs on benefits, compensation, rewards, incentives, health and wellness to improve employee welfare.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },    

    "Budget Management":
        {
        "Description": "Effective preparation of budget plans using the latest budgeting techniques, and preparation of budget submissions by agency based on policies.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Carpentry Skill":
        {
        "Description": "Has the ability to perform stake-out building lines, fabricate formworks, install/strip form works, install framing works, install architectural ceiling/wall sheats/panels and floor finishes and fabricate/install door/window jambs and panels.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Cash Management":
        {
        "Description": "The ability to collect and manage assessment and usage of cash flow to ensure the financial stability and solvency of an organization.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Chlorine Handling Skills":
        {
        "Description": "Has the fundamental knowledge to be able to safely use and handle chlorine and other chemical solutions in the District’s water treatment facilities.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Computer Skills":
        {
        "Description": "Able to adopt audit methodology that is consistent with international standards on public sector audit for selecting a process for audit, planning an audit assignment, documenting a process, assessing risks and controls in a process, assessing the performance of processes, identifying control gaps, conducting audit tests, and accurately recording audit work.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Conduct Audit Assignments":
        {
        "Description": "Using an audit methodology that is consistent with international standards on public sector audit for selecting a process for audit, planning an audit assignment, documenting a process, assessing risks and controls in a process, assessing the performance of processes, identifying control gaps, conducting audit tests, and accurately recording audit work.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Customer Complaints Management":
        {
        "Desription": "Has the ability to use proper channels to deal with customer complaints effectively to improve customer retention.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Data Collection from Utility Meters":
        {
        "Description": "Demonstrate proficiency in using handheld devices and conduct accurate records of reading meters.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Data Management":
        {
        "Description": "The ability to analyze statistics and other data by interpreting and evaluating the results to be able to formulate a report and/or presentation as reference for decision making.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Delivering Service Excellence":
        {
        "Description": "The ability to provide proactive, responsive, accessible, courteous and effective public service to attain the highest level customer satisfaction.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Digital Media and Visualisation":
        {
        "Description": "The ability to convey ideas and information in forms such audio, text, pictures, diagrams, video, photos, maps and 3D models.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
        
    "Drafting Construction Drawings":
        {
        "Description": "The ability to draft precise and detailed planning design for building and infrastructure project within the criteria set in conformance with the structural codes and standards.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Drafting Electrical Layouts":
        {
        "Description": "The ability to draft precise and detailed electrical layout plan for the electrical wiring within the criteria set in conformance with the electrical codes and standards.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },      

    "Driving":
        {
        "Description": "Capable to operate motor vehicles classified under LTO Restriction with compliance to local traffic rules and regulations and perform minor vehicle repairs and other minor servicing.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
        
    "Electrical Installation":
        {
        "Description": "Has the capability to install and maintain electrical wiring, lighting and related equipment and systems where the voltage does not exceed the required voltage in building establishment.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Electronics and Electrical Equipment Servicing":
        {
        "Description": "Has the ability to conduct maintenance and repair of electronic products and service appliances.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Environmental Compliance":
        {
        "Description": "Has the ability to identify, define, develop, evaluate and improve systems, processes and procedures that ensures constant compliance of the project proponents, local government and its partner agencies/organizations in the implementation of projects, programs and activities related to and/or has adverse impact directly or indirectly to environment and natural resources.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Facilities Management":
        {
        "Description": "Has the ability to maintain and improve office facilities or properties in order to ensure minimal disruption of business operations.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Heavy Equipment Operational Skill": 
        {
        "Description": "Demonstrate competency on operating heavy equipment according to procedures, specifications and manual of instruction.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Housekeeping":
        {
        "Description": "Has the ability to maintain cleanliness of public areas, equipment and promote workplace hygiene procedures in providing housekeeping services.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },    
    
    "Information Technology Management":
        {
        "Description": "Demonstrate skills and working knowledge in Information Technology Management. Applies technical skills and demonstrates knowledge of emerging technology (e.g. IT processes, methodologies, etc.).",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Inventory Management and Stock Control":
        {
        "Description": "Has the ability to record and manage inventory which typically covers the receipt and custody of items procured, ensuring just-in-time distribution when needed, safe maintenance of stocks, monitoring of re-order point and disposal of unnecessary stocks.",
        "Description": "Demonstrate skills and working knowledge in Information Technology Management. Applies technical skills and demonstrates knowledge of emerging technology (e.g. IT processes, methodologies, etc.).",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Learning and Development Planning":
        {
        "Description": "The ability to translate training/learning needs results into interventions and prioritize them for implementation.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Learning Measurement and Evaluation":
        {
        "Description": "The ability to determine training/learning needs and evaluate its effectiveness.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Legal Management":
        {
        "Description": "The ability to provide legal assistance and oversee all legal matters within the organization.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Liquidity, Debts and Investment Managment":
        {
        "Description": "Has the ability to develop strategies in ensuring liquidity, debt and investment management to cover payments against all vouchers, and undertake investment programs in times of cash surplus.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Management of Accounts Receivable":
        {
        "Description": "Ensuring the monitoring of timely payment of receivables and provide strategic initiatives for the improvement and more efficient accounts receivable management system.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Market Analysis":
        {
        "Description": "Has the ability to gather and analyze data related to potential target consumers that will help generate revenues in the agency.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Masonry":
        {
        "Description": "Has the ability to perform construction of brick and concrete block structure, installation of pre-cast balluster/handrail and plastering of concrete wall surface.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
            
    "Meter Maintenance / Calibration":
        {
        "Description": "Has the knowledge of calibration procedures and the ability to troubleshoot water meters within the prescribed standards.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Metal Arc Welding":
        {
        "Description": "Has the ability to perform weld carbon steel plate and pipe components as specified by layout, blueprints, diagrams, work order, welding procedure or oral instructions using shielded metal arc welding equipment.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
            
    "Negotiation Skills":
        {
        "Description": "Has the ability to adopt appropriate techniques for negotiating resistance and objections in order to negotiate to a desired outcome.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },        
            
    "Non-Revenue Water Management":
        {
        "Description": "Has the ability to identify leakages and provide strategic initiatives to address the reduction of non-revenue water.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Occupational Safety and Health":
        {
        "Description": "Has the awareness to practice, evaluate, lead, establish and manage Occupational Safety and Health programs in the workplace.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
        
    "Oral Communication":
        {
        "Description": "Makes clear and convincing oral presentations to individual or groups; listens effectively and clarifies information as needed.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },    

    "Pipe-Fitting":
        {
        "Description": "Has the ability to cut, bevel, and / or thread pipes, and install overhead and underground piping system.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Planning and Delivering":
        {
        "Description": "The ability to prioritize and identify scope and allocate resources to meet individual, team, or organization targets and objectives.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Plumbing - Service Connection":
        {
        "Description": "Has the capability of installing multiple units of plumbing system with multi-point hot-and-cold-water lines which also includes plumbing repair and maintenance works.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Plumbing - Distribution System":
        {
        "Description": "Has the capability of installing and connecting network pipes in the water distribution system which also includes distribution and mainline repair.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
        
    "Policy Evaluation":    
        {
        "Description": "The ability to measure and assess the appropriateness, effectiveness and efficiency of human resource policies, contributing to policy improvements and innovation.",        
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Preparation of Expenditure Program":
        {
        "Description": "The production of the monthly expenditure program (monthly flow), forecast by object allotment class (Personnel Services, MOOE and Capital Expenditure) using all relevant and available historical data to the highest degree of accuracy possible.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
        
    "Preparation of Revenue Program":
        {
        "Description": "Forecasting the monthly revenue program using all relevant and available historical data with the highest degree of accuracy possible.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },   

    "Pressure Management":
        {
        "Description": "The ability to effectively regulate water pressure within water networks in ensuring the efficient and sustainable distribution of water supply.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Procurement Management":
        {
        "Description": "The ability to plan and implement measures to acquire supplies and properties at the best possible cost; that meets the quality, quantity and timeliness requirement of the organization; and are compliant to procurement policies.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Procurement Planning":
        {
        "Description": "The ability to effectively undertake procurement planning according to the approved Annual Procurement Plan in order to facilitate the achievement of the agency’s program of work, goals and targets.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Program / Course Delivery and Administration":
        {
        "Description": "The ability to plan, execute and report the implementation of training/learning interventions, courses and programs.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Project / Program Management":
        {
        "Description": "The ability to monitor and coordinate the implementation of plans, policies, tasks and activities of programs and projects being undertaken by the stakeholder, and taking action to meet quality and performance goals.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Public Relation Management":
        {
        "Description": "The ability to build, maintain and manage engagement and goodwill between the organization and the public through the installation of assistance and complaint mechanisms and the implementation of special programs.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Pump Operation":
        {
        "Description": "The ability to monitor and maintain the pumping equipment and facilities in order to ensure maximum efficiency of its operations.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },
        
    "Quality Management and Assurance":
        {
        "Description": "Performs tasks in ensuring that products or services consistently meet the prescribed government standards or within the prescribed contract agreement by other private institution.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Records Management":
        {
        "Description": "The ability to apply and adapt records management standards related to the cycle of records in an agency/institution which are conducted to achieve adequate and proper documentation of government policies, transactions and effective management of the agency’s operations.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Recruitment, Selection and Placement":
        {
        "Description": "The ability to search, attract, and assess job candidates and to guide the appointing authority in choosing the best fit for the job at the right time, in accordance with legal requirements in order to achieve organizational goals.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Rewards and Recognition":
        {
        "Description": "The ability to identify, develop and implement programs for the organization/bureaucracy to reward and recognize outstanding performance and behavior.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Supervisory Control and Data Qcquisition (SCADA) Operation":
        {
        "Description": "The ability to develop a SCADA application and to use SCADA systems in the agency’s operation.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Strategic Planning":
        {
        "Description": "The ability to influence, realign the organization's strategic goals and directions; monitor and review data from various aspects of strategic and corporate planning and recommend enhancements.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Stress Management":
        {
        "Description": "The ability to apply techniques to cope with or lessen the physical and emotional effects of everyday life pressure in the workplace.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Supplier Management and Contract Agreement":
        {
        "Description": "Has the ability to manage suppliers in order to ensure continuing provision of goods and services. Manage contract implementation and ensure fair, open and transparent dealings with existing and potential suppliers.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Supplies and Property Management":
        {
        "Description": "The ability to plan and implement measures to efficiently allocate, utilize, maintain and dispose supplies and properties of the organization.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Taxation":
        {
        "Description": "Has the ability to interpret, understand and manage various aspects of Philippine Tax laws.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
        },

    "Writing Effectively":
        {
        "Description": "The ability to write in clear, concise and coherent manner using different tools to convey information or express ideas effectively.",
        "Basic": {},
        "Intermediate": {},
        "Advanced": {},
        "Superior": {}
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
    department TEXT
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

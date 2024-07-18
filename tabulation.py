import streamlit as st

# Competency descriptions from the provided Excel file
competency_descriptions = {
    "Accounting": {
        "Description": """
            The ability to record, analyze, classify, summarize and interprets financial transactions to be able to prepare for a sound financial report and manage the accounts of the organization.
        """,
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
        """
    },
    "Procurement Management": {
        "Description": """
            The ability to plan and implement measures to acquire supplies and properties at the best possible cost; that meets the quality, quantity and timeliness requirement of the organization; and are compliant to procurement policies.
        """,
        "Basic": """
            - Coordinates schedules and attendance of committee members to Bids and Awards Committee (BAC) meetings.
            - Takes charge of logistic concerns such as but not limited to materials, equipment and meals.
            - Files document for procurement such as but not limited to the following:
                - Annual Procurement Plan (APP)
                - Agency Procurement Compliance and Performance Rating (APCPI)
                - Procurement Monitoring Report (PMR)
            - Receives procurement requests and checks completeness of requirements.
            - Maintains and updates procurement records in database/filing system.
            - Writes simple pro-forma communications such as but not limited to acknowledgment and transmittal letters relative to procurement.
        """,
        "Intermediate": """
            - Prepares agenda folder/ documents/materials and takes minutes of BAC meetings.
            - Prepares the following reports:
                - APP
                - APCPI
                - PMR
            - Posts specifications of requests in the Philippine Government Electronic Procurement System (PhilGEPS) and conducts pre-bid and clarification for bid.
            - Procures goods as scheduled and in compliance with the existing laws and regulations (RA9184, COA, DBM).
            - Prepares replies to queries on procurement of supplies and properties.
        """,
        "Advanced": """
            - Reviews and validates various reports:
                - APP
                - APCPI
                - PMR
            - Develops and enhances internal policies and procedures on procurement such as but not limited to cost-cutting and internal control measures.
            - Consolidates the Project Procurement Management Plans (PMP) of offices/units into APP.
            - Reviews requests and recommends approval for the procurement of supplies and equipment.
        """,
        "Superior": """
            - Convenes the BAC meetings as the Chair of the BAC Secretariat.
            - Endorses APCPI & PMR for approval by the management and submission to the Government Procurement Policy Board - Technical Support Office (GPPB TSO).
            - Develops communication plan and procurement plan in accordance with the approved office budget.
            - Monitors the implementation of policies, programs and activities on procurement.
        """
    },
    "Benefits, Compensation and Welfare Management": {
        "Description": """
            The ability to develop, implement, evaluate and enhance policies and programs on benefits, compensation, rewards, incentives, health and wellness to improve employee welfare.""",
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
        """
    },
    "Budget Management": {
        "Description": """
            Effective preparation of budget plans using the latest budgeting techniques, and preparation of budget submissions by agency based on policies.""",
        "Basic": """
            - Ability to implement and apply, with guidance or supervision, existing processes and policies for programs nd activities.
        """,
        "Intermediate": """
            - Ability to ensure adherence to procedures, processes and policies in the performance of activities relative to budget management.
        """,
        "Advance": """
            - Ability to monitor and review data and recommend enhancements and/or changes in procedures, processes and policies relative to budget management.
        """,
        "Superior": """
            - Ability to formulate advance policies and strategies on budget management.
    }                                                                                                           
}

# Page Title
st.title('Learning Needs Analysis - eLearning Preferences')

# Input fields
full_name = st.text_input('Full Name')
current_position = st.text_input('Current Position (Write in full including parenthetical, if any)')
office_agency = st.text_input('Office/Agency (Write in full, including Region and Field, if any)')
position_level = st.selectbox('Position Level', ['1st Level', '2nd Level Non-Supervisory', 'Supervisory', 'Managerial'])
province = st.selectbox('Province', ['Albay', 'Camarines Sur', 'Sorsogon'])
device = st.selectbox('Device Used for e-Learning', ['Computer/Laptop', 'Tablet', 'Smartphone'])
learning_mode = st.selectbox('Preferred Learning Mode', ['Synchronous Face-to-Face', 'Asynchronous', 'Blended'])
select_competency = st.selectbox('Select Competency', list(competency_descriptions.keys()), key='select_competency')

# Display competency descriptions
if select_competency in competency_descriptions:
    st.markdown(f"### {select_competency} Competency Descriptions")
    st.markdown(competency_descriptions[select_competency]["Description"])
    cols = st.columns(4)
    levels = ["Basic", "Intermediate", "Advanced", "Superior"]
    for i, level in enumerate(levels):
        cols[i].markdown(f"**{level}**")
        cols[i].markdown(competency_descriptions[select_competency][level])

competency_level = st.selectbox('Competency Level', ['Basic', 'Intermediate', 'Advanced', 'Superior', 'Not yet acquired'], key='competency_level')

# Submit button
if st.button('Save'):
    st.markdown(f"**Full Name:** {full_name}")
    st.markdown(f"**Current Position:** {current_position}")
    st.markdown(f"**Office/Agency:** {office_agency}")
    st.markdown(f"**Position Level:** {position_level}")
    st.markdown(f"**Province:** {province}")
    st.markdown(f"**Device Used for e-Learning:** {device}")
    st.markdown(f"**Preferred Learning Mode:** {learning_mode}")
    st.markdown(f"**Competency:** {select_competency}")
    st.markdown(f"**My Level for this Competency:** {competency_level}")
    st.success('Information saved successfully!')

if st.button('Reset'):
    st.caching.clear_cache()
    st.experimental_rerun()

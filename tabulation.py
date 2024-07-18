import streamlit as st

# Competency descriptions from the provided Excel file
competency_descriptions = {
    "Accounting": {
        "Basic": """
            - Receives and records all claims for processing.
            - Checks completeness of documents/attachments necessary for claims processing.
            - Prepares certification or statement of employee compensation benefits.
            - Maintains index of records of compensation, benefits, and deductions.
        """,
        "Intermediate": """
            - Validates and records journal entries of financial transactions.
            - Records financial transactions in the book of accounts.
            - Prepares certificate of remittances, schedule of accounts payable, and trial balance.
            - Updates records of receipts and expenditures for monthly reconciliation.
        """,
        "Advanced": """
            - Reviews monthly deductions and remittances to various agencies.
            - Reviews ledger, general ledger accounts, and schedules of accounts.
            - Validates and reconciles reciprocal accounts for accuracy.
            - Prepares financial reports, schedules, and all other accounting-related reports.
        """,
        "Superior": """
            - Certifies funds availability of disbursements.
            - Identifies trends and developments in accounting and finance.
            - Develops communication plan and policies, guidelines for financial transactions.
            - Reviews and recommends policies, guidelines, and standards on accounting and financial management.
        """
    },
    "Procurement Management": {
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
            - Prepares agenda folder/documents/materials and takes minutes of BAC meetings.
            - Prepares the following reports:
                - APP
                - APCPI
                - PMR
            - Posts specifications of requests in the Philippine Government Electronic Procurement System (PhilGEPS) and conducts pre-bid and clarification for bid.
            - Procures goods as scheduled and in compliance with the existing laws and regulations (RA9184, COA, DBM).
            - Prepares replies to queries on procurement of supplies and equipment.
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
    }
    # Add other competencies as needed
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

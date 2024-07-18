import streamlit as st

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
select_competency = st.selectbox('Select Competency', ['Procurement Management', 'Another Competency'], key='select_competency')

# Competency descriptions
competency_descriptions = {
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
    },
    "Another Competency": {
        "Basic": "Description for Basic level of Another Competency",
        "Intermediate": "Description for Intermediate level of Another Competency",
        "Advanced": "Description for Advanced level of Another Competency",
        "Superior": "Description for Superior level of Another Competency"
    }
}

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

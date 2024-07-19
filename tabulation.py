import streamlit as st

# Competency descriptions from the provided Excel file
competency_descriptions = {
    "Accounting": {
        "Description": 
        """The ability to record, analyze, classify, summarize and interprets financial transactions to be able to prepare for a sound financial report and manage the accounts of the organization.""",
        "Basic": 
        """
            - Receives and records all claims for processing, evaluation and certification of the unit.
            - Checks completeness of documents/attachments needed for the transaction and validates accuracy of computation.
            - Prepares certification or statement of employees' contributions and remittances.
            - Maintains index of records of compensation, benefits, allowances, mandatory deductions and remittances.
            - Prepares journal entries and certificates of taxes withheld.
            - Writes simple pro-forma communications on accounting transactions.
        """,
        "Intermediate": 
        """
            - Validates and records journal entries of financial transactions.
            - Records financial transactions in the book of accounts and maintains files of financial reports/documents.
            - Prepares certificate of remittances, schedule of remittances and all other requirements for remittances.
            - Updates records of receipts and expenditures funds to monitor balance of funds and verifies records of funds availability.
            - Reconciles general and subsidiary ledgers of accounts.
            - Prepares replies to queries on accounting transactions.
        """,
        "Advanced": 
        """
            - Reviews monthly deductions and remittances to national government agencies.
            - Reviews ledger, general ledger accounts and schedules of the financial reports.
            - Validates and reconciles reciprocal accounts for the central/regional offices.
            - Prepares financial reports, schedules and all other reports of all funds as required by the regulatory agencies and the Commission.
            - Approves journal entries.
            - Develops or enhances existing policies, guidelines and processes on accounting and auditing procedures.
        """,
        "Superior": 
        """
            - Certifies funds availability of disbursements, supporting documents are complete and proper and the necessary deductions are effected and monitors timely remittance of all deductions and payments made.
            - Identifies trends and developments in accounting and auditing and recommends enhancement of policies, procedures, systems and processes.
            - Develops communication plan and policies, guidelines and issuances on accounting rules and regulations.
            - Reviews and recommends policies, guidelines and processes on accounting and auditing procedures.
            - Prepares financial report for management and recommends appropriate financial internal control measures for the allocation and sourcing of funds.
        """,
        },
    
    "Benefits, Compensation and Welfare Management": {
        "Description": 
        """The ability to develop, implement, evaluate and enhance policies and programs on benefits, compensation, rewards, incentives, health and wellness to improve employee welfare.""",
        "Basic": """
            - Collates data/materials from the conduct and evaluation of organization-wide programs (i.e. health and wellness programs, information campaigns, sports activities, anniversary and Christmas programs, etc.).
            - Maintains and updates employee records (HRMIS, leave, absences and tardiness, medical, service records, etc.).
            - Prepares certifications such as but not limited to compensation, service records, leave balance, attendance and other employee welfare transactions of employees.
            - Writes simple pro-forma communications relative to benefits, compensation and welfare of employees.
            - Maintains and updates procurement records in database/filing system.
        """,
        "Intermediate": 
        """
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
        "Superior": 
        """
            - Establishes and develops a comprehensive employee benefits, compensation and welfare programs for the CSC.
            - Reviews and recommends proposals for enhancements and changes of existing processes and systems of benefits, compensation, and welfare mechanism of the organization.
            - Formulates operational policies and guidelines on the benefits, compensation, and welfare of employees.
            - Develops communication and implementation plan on the benefits and compensation system, and employees welfare programs of the organization.
        """,
    },
    
    "Budget Management": {
        "Description": 
        """Effective preparation of budget plans using the latest budgeting techniques, and preparation of budget submissions by agency based on policies.""",
        "Basic": 
        """
            - Ability to implement and apply, with guidance or supervision, existing processes and policies for programs nd activities.""",
        "Intermediate": """
            - Ability to ensure adherence to procedures, processes and policies in the performance of activities relative to budget management.
        """,
        "Advanced": 
        """
            - Ability to monitor and review data and recommend enhancements and/or changes in procedures, processes and policies relative to budget management.
        """,
        "Superior": 
        """
            - Ability to formulate advance policies and strategies on budget management.
        """,
    },
    
    "Building Collaborative, Inclusive Working Relationships": {
        "Description": 
        """The ability to build and maintain a network of reciprocal, high trust, synergistic working relationships within the organization nd across government and relevant sectors. This involves the ability to successfully leverage and maximize opportunities for strategic influencing within the organization and with external stakeholders.""",
        "Basic": 
        """
            - Maximizes existing partnerships and networks and capitalizes son these to deliver or enhance work outcomes.
        """,
        "Intermediate": 
        """
            - Builds partnerships and networks to deliver or enhance work outcomes.
        """,
        "Advanced": 
        """
            - Strengthens and deepens partnerships and networks to deliver or enhance work outcomes.
        """,
        "Superior": 
        """
            - Builds and then leverages on collaborative partnerships and networks to deliver or enhance work outcomes.
        """,
    },
    
    "Cash Management": {
        "Description": 
        """The ability to collect and manage assessment and usage of cash flow to ensure the financial stability and solvency of an organization.""",
        "Basic": 
        """
            - Prepares the following financial documents:
                - deposit slips
                - summary of collections
                - checks for payment
                - automatic debit advice
                - list of checks issued
                - documents on availability of funds;
            - Liaises with the bank and other financial institutions with regards to payments of remittances and other transactions.
        """,
        "Intermediate": 
        """
            - Issues receipts for various transactions.
            - Maintains/updates official check register/official cash book.
            - Prepares the following financial documents:                     
                - Statement of Daily Cash Position
                - Statement of cash accountability
            - Reviews the following reports: 
                - Checks Issued
                - Collection and deposit.
                - Generates and evaluates data on various aspects of tasks and activities.
            - Recommends enhancements on the processes within the Division Level.
        """,
        "Advanced": 
        """
            - Prepares and consolidates Monthly Cash Position Reports of all Funds.
            - Monitors the transfer of funds to CSC Regional Offices.
            - Verifies and signs checks up to the extent of accountability as authorized by the Commission.
            - Identifies trends and developments in cash management and recommend enhancements of current procedures, processes and policies.
        """,
        "Superior": 
        """
            - Monitors compliance with generally accepted accounting and auditing principles rules and regulations pertaining to: 
                - collections, deposits release of payments
                - preparation and submission of cash position report to the management
                - handling of cash, official receipts, checkbooks, warrants and other negotiable instruments;
            - Reviews, verifies and signs checks up to the extent of accountability as authorized by the Commission.
            - Recommends for the establishment of a comprehensive cash management system for the Organization.
        """,
    },
    
    "Championing and Applying Innovation": {
        "Description": 
        """The ability to increase productivity and efficiency at work by applying new ideas and creative solutions to existing processes, methods and services. """,
        "Basic": 
        """
            - Demonstrates an awareness of basic principles of innovation            
        """,
        "Intermediate": 
        """
            - Contributes new ideas, approaches and solutions
        """,
        "Advanced": 
        """
            - Produces novel, out-of-the-box ideas to improve or replace existing practices and procedures
        """,
        "Superior": 
        """
            - Promotes a culture and discipline of challenging the status quo and seeking for and applying improvements.
        """,
    },
    
    "Procurement Management": {
        "Description": 
        """The ability to plan and implement measures to acquire supplies and properties at the best possible cost; that meets the quality, quantity and timeliness requirement of the organization; and are compliant to procurement policies.""",
        "Basic": 
        """
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
        "Intermediate": 
        """
            - Prepares agenda folder/ documents/materials and takes minutes of BAC meetings.
            - Prepares the following reports:
                - APP
                - APCPI
                - PMR
            - Posts specifications of requests in the Philippine Government Electronic Procurement System (PhilGEPS) and conducts pre-bid and clarification for bid.
            - Procures goods as scheduled and in compliance with the existing laws and regulations (RA9184, COA, DBM).
            - Prepares replies to queries on procurement of supplies and properties.
        """,
        "Advanced": 
        """
                - Reviews and validates various reports:
                - APP
                - APCPI
                - PMR
            - Develops and enhances internal policies and procedures on procurement such as but not limited to cost-cutting and internal control measures.
            - Consolidates the Project Procurement Management Plans (PMP) of offices/units into APP.
            - Reviews requests and recommends approval for the procurement of supplies and equipment.
        """,
        "Superior": 
        """ 
            - Convenes the BAC meetings as the Chair of the BAC Secretariat.
            - Endorses APCPI & PMR for approval by the management and submission to the Government Procurement Policy Board - Technical Support Office (GPPB TSO).
            - Develops communication plan and procurement plan in accordance with the approved office budget.
            - Monitors the implementation of policies, programs and activities on procurement.
        """,
    }, 
    
    "Program/Course Delivery and Administration": {
        "Description": 
        """The ability to plan, execute and report the implementation of training/learning interventions, courses and programs.""",
        "Basic": 
        """
            - Checks and confirms registration of participants, accepts payments and/or facilitates issuance of OR/AR.
            - Issues complete training kit (IDs, notebooks, hand-outs, etc.) to registered participants.
            - Prepares and issues training paraphernalia (such as: Attendance Sheet, Participants Directory, Certificates of Completion and Appearance, etc.) and other training and office materials and supplies.
            - Reproduces and packages training/learning materials as specified in the Training Activity Plan/ Training Design Matrix.
            - Gathers and preserves workshop outputs as required by the training administrator.
            - Prepares status of payments of participants. 
        """,
        "Intermediate":
        """
            - Prepares and executes Learning and Development/ Program/Course Implementation Checklists using pre-designed template.
            - Procures miscellaneous materials and processes petty cash vouchers.
            - Selects, recommends and coordinates with subject matter experts (SMEs).
            - Processes standard Service Level Agreements (SLAs)/Memorandum of Agreement (MOAs).
            - Checks if venue arrangement is in accordance with the specifications provided for in the Training Activity Plan/Training Design Matrix (TDM) or as requested by the Facilitator or SME.
            - Administers Level 1 and 2 Evaluation Instruments as specified in the Evaluation Plan.
            - Prepares Training Report in accordance with the ISO 9001 template/Competency-Based Learning and Development Management System (CBLDMS).
            - Ensures the completeness of the Implementation Folder as required in the ISO 9001 Program/Course Implementation Process/CBLDMS.
        """,
        "Advanced":
        """
            - Sources and recommends new SMEs.
            - Formulates non-standard Service Level Agreements (SLAs)/Memorandum of Agreement (MOAs) subject to the review of the Office of Legal Affairs (OLA)/Legal Service Division (LSD).
            - Determines special learning and non-learning needs of stakeholders such as agencies/other CSC units.
            - Prepares comprehensive Training/Learning and Development Report for In-House Programs or customized training/L&D programs.
        """,
        "Superior":
        """
            - Reviews, approves and monitors L&D/Program/Course Implementation Checklists.
            - Identifies and allocates resource requirements to ensure proper delivery and administration of training/learning interventions.
            - Approves SMEs as recommended by the Training Administrator.
            - Addresses exceptional participant/training concerns and issues.
            - Approves Training Reports and ensures that all recommendations are properly implemented.
        """,
    },
    
    "Program/Course Design and Development": {
        "Description":
        """The ability to apply research skills towards identifying and developing learning objectives, sourcing, selecting and sequencing content, designing training/learning methodologies and activities and developing training/learning materials.""",
        "Basic":
        """
            - Prepares and selects energizers and ice breakers.
        """,
        "Intermediate":
        """
            - Reviews and determines appropriateness of Course Briefs and Training Activity Plans/Training Design Matrix submitted by external Learning Service Providers.
            - Reviews and determines appropriateness of Course Briefs and Training Activity Plans/Training Design Matrix submitted by external Learning Service Providers.
            - Sources, selects and sequences content in accordance with the specified learning objectives.
            - Develops PowerPoint slides and other learning materials given the content and other specifications.
            - Documents and prepares own Course Briefs, Training Activity Plan/Training Design Matrix.
        """,
        "Advanced":
        """
            - Develops learning objectives (with performance, conditions and criteria) using the SMART format and Bloom's taxonomy.
            - Designs training/learning methodologies and activities.
            - Develops Participant's Manuals, Facilitator's Guide and Evaluation Plan and other training/learning materials.
        """,
        "Superior":
        """
            - Reviews and approves Course Brief, Training Activity Plan/ Training Design Matrix, Participant's Manual, Facilitator's Guide and Evaluation Plan, in accordance with the identified needs as specified in Training/Learning Needs/Competency Assessment Reports and Annual Training/Learning and Development Plan.
            - Identifies and allocates resource requirements to ensure proper design and development of learning interventions.
        """,
    },
    
    "Public Relations Management": {
        "Description":
        """The ability to build, maintain and manage engagement and goodwill between the organization and the public through the installation of assistance and complaint mechanisms and the implementation of special programs.""",
        "Basic":
        """
            - Responds to simple inquiries and requests.
            - Refers simple requests/complaints from agencies or clients to concerned offices/units/agencies.
            - Maintains and updates databases of reports received, queries, complaints, commendation and suggestions.
            - Writes simple pro-forma communications such as but not limited to acknowledgment and transmittal letters relative to public relations.
        """,
        "Intermediate":
        """
            - Coordinates with concerned offices/units/agencies on reports received for action.
            - Prepares periodic statistical reports on complaints, requests and queries received from clients.
            - Coordinates with concerned offices/units/agencies for the conduct of validation for the recipients of special programs (e.g. Pamanang Lingkod Bayan).
            - Conducts validation for the recipients of special programs (e.g. Pamanang Lingkod Bayan).
            - Prepares replies to queries on the implementation of special programs and public assistance and complaint center.
        """,
        "Advanced":
        """
            - Collaborates with regulatory agencies and or media relative to complaints and commendations about public officials and employees.
            - Prepares periodic reports and recommendations to management on the operation and services of the public assistance and complaint center.
            - Develops feedback mechanism to assess the services of the public assistance and complaint center.
            - Develops or enhances strategies on how to sustain or improve existing programs.
            - Conducts studies/analysis on the complaints, requests and queries of clients and agencies.
            - Develops or enhances policies and procedures on the implementation of special programs.
        """,
        "Superior":
        """
            - Reviews and recommends enhancements to existing policies, guidelines and procedures relative to public relations.
            - Reviews existing assistance and complaint mechanisms and special programs and recommends enhancements.
            - Monitors and evaluates the implementation of the special programs and the public assistance and complaint center.
        """,    
    },
    
    "Records Management": {
    "Description":
    """The ability to apply and adapt records management standards related to the cycle of records in an agency/institution which are conducted to achieve adequate and proper documentation of government policies, transactions and effective management of at he agency/institution operations.""",
    "Basic":
    """
        - Develops communication plan on policies, guidelines and issuances on the administration of examination.
        - Conducts training for examination representatives/test administrators/examiners and supervisors.
        - Reviews and recommends manual on test administration.
        - Maintains personal records in a methodical and organized manner using own initiative to facilitate easy retrieval.
        - Quickly retrieves employees' records upon request and willingly and immediately respond to clients.
        - Applies knowledge of records management software applications and their use.
        - Checks accuracy of the details of all transactions and record keeping.
    """,
    "Intermediate":
    """
        - Keeps updated with current records management technology and practices to continuously improve existing systems and practices for efficiency and effectiveness in records management functions.
        - Applies and adapt record management standards and best practices effectively.
        - Support others in the development and introduction of new record keeping practices and procedures.
        - Displays proactive approach to improving record keeping practices.
    """,
    "Advanced":
    """
        - Develops procedures for quick classification, better storage, protection and disposition of records to provide integrity, reliability, efficiency and effectiveness in records management functions and to respond to internal and external clients' needs and expectations.
        - Interprets best practice standards.
        - Applies locally and provide accurate and effective advice and guidance to colleagues.
        - Assesses current record keeping systems and provides feedback on their strengths and areas for improvement.
        - Recognizes potential issues in relation to records management and communicates these to the relevant staff.
    """,
    "Superior":
    """
        - Shares expertise, lessons learned and ideas with others for improvement of the records management system for the organization's productivity, efficiency and effectiveness.
        - Develops and implements record management policies, procedure and guidance, and provides advice on record keeping issues.
        - Critically assesses current procedures and provides workable solutions for continuous improvement.
    """,
    },
    
    "Recruitment, Selection and Placement": {
    "Description":
    """The ability to search, attract, and assess job candidates and to guide the appointing authority in choosing the best fit for the job at the right time, in accordance with legal requirements in order to achieve organizational goals.""",
    "Basic":
    """
        - Prepares annual list of projected turnover due to retirement for recruitment planning.
        - Maintains and updates database of vacancies, applicants, and personnel actions.
        - Facilitates publication and posting of vacancies.
        - Coordinates with personnel selection boards (PSBs) and heads of offices/divisions on their availability for meetings and interviews.
        - Checks the veracity and authenticity of the CSC eligibility of the candidates by verifying with the IRMO/EAD.
        - Provides new appointees with the list of pre-employment requirements and endorses them to the heads of offices/divisions.
        - Writes simple pro-forma communications relative to recruitment, selection and placement.
    """,
    "Intermediate":
    """
        - Sources internal and external talents through the use of various recruitment strategies.
        - Checks the completeness of application documents and reviews paper qualifications of applicants vis-a-vis the qualification standards.
        - Communicates/informs applicants of the results of the screening and assessment schedules.
        - Administers assessment instruments and prepares assessment results.
        - Facilitates the interview and prepares reports.
        - Prepares reports based on background investigation results.
        - Takes minutes of meetings during PSB meetings/ deliberations.
        - Prepares assessment folders and a draft recommendation memo for review and approval by the PSB.
        - Prepares resolutions and appointments for signature by the Commission/Regional Director.
        - Conducts mini orientation to new appointees about CSC, basic policies on work hours, benefits, etc.
        - Completes the new hires' employment related paperwork.
        - Prepares replies to queries on recruitment, selection and placement.
    """,
    "Advanced":
    """
        - Conducts assessment center for Division Chief to Director positions and prepares corresponding assessment reports.
        - Reviews/evaluates all appointments issued by CSCROs.
        - Develops and enhances assessment tools/forms.
        - Interviews applicants/candidates to vacant positions.
        - Conducts exit interviews to identify HR strengths and areas for improvement and prepares report.
    """,
    "Superior":
    """
        - Evaluate accuracy of assessment results.
        - Recommends talent pool requirements of the Commission by reviewing strategic objectives and scorecards of the organization.
        - Reviews and recommends improvements in recruitment and selection policies and processes.
        - Develops communication and implementation plan on the recruitment, selection, and placement policies of the Commission.
    """,
    },
    
    "Research and Development Planning": {
    "Description":
    """Systematically gathering and analyzing information useful in identifying, implementing and evaluating development programs supportive of the development thrusts and priorities.""",
    "Basic":
    """
        - Observes guidelines and checks for completeness of required information when determining the scope and limitation of research work
        - Applies appropriate data gathering tools and recognizes and accesses correct information sources
    """,
    "Intermediate":
    """
        - Recognizes and adopts the appropriate research methodologies and resources needed based on the identified needs and issues that must be addressed by the research
        - Identifies primary and alternate sources of data, applies data reconstruction techniques and data gathering methodologies to complete required data
    """,
    "Advanced":
    """
        - Performs necessary quantitative and/or qualitative data analysis to generate the information needed, and organizes the same for presentation purposes.
    """,
    "Superior":
    """
        - Reviews research results and organizes such into useful information (socio-economic, information, demographic, program/project feasibility, situationer, impact analysis, etc.) in provincial development planning
    """,
    },
    
    "Rewards and Recognition": {
    "Description":
    """The ability to identify, develop and implement programs for the organization/bureaucracy to reward and recognize outstanding performance and behavior.""",
    "Basic":
    """
        - Coordinates schedule of meetings and availability of committee members.
        - Takes charge of logistic concerns such as but not limited to the venue, emails and equipment for use during meetings.
        - Receives nomination folders and checks competencies of requirements.
        - Prepares profile of nominees for presentation to the committee.
        - Maintains and updates database of the type of awards, nominees and awardees.
        - Writes simple pro-forma communication such as but not limited to acknowledgement and transmittal letters relative to rewards and recognition.
    """,
    "Intermediate":
    """
        - Conducts information campaign activities relative to the rewards and recognition programs.
        - Evaluates documentary requirements of nominees and the appropriate category of awards that may be considered.
        - Prepares agenda folder and takes minutes of committee meetings.
        - Coordinates with validators for the conduct of background investigation and submission of reports.
        - Verifies and consolidates feedback on the candidates received from clients and stakeholders.
        - Coordinates the productions/reproduction of awards paraphernalia.
        - Replies to queries on rewards and recognition.
    """,
    "Advanced":
    """
        - Identifies and recommends awards committee composition.
        - Collaborates with the search committee/performance management team in proactively identifying possible nominees.
        - Prepares the assessment reports and recommendation of the committee to the approving body.
        - Conceptualized program collaterals in collaborating with graphic designers or suppliers.
        - Facilitates conduct of the awards rites and prepares post activity report.
        - Conducts comparative studies on the organization's rewards and recognition program vis-à-vis the best practices of organizations from the private and public sector, both local and international.
        - Develops policies or enhances procedures on rewards and recognition.
        - Determines and recommends kind of monetary and non-monetary rewards based on existing policies.
    """,
    "Superior":
    """
        - Reviews and recommends enhancements to existing policies, guidelines, procedure relative to the reward and recognition programs.
        - Develops communication and implementation plan on the policies, guidelines and issuances on rewards and recognition program.
        - Monitors and evaluates the conduct of the awarding rites.
        - Monitors and evaluates the implementation of the rewards and recognition program.
        - Conducts studies on the impact of the program to the performance of the organization/unit.
    """,
    },
    
    "Solving Problems and Making Decisions": {
    "Description":
    """The ability to resolve deviations and exercise good judgement by using fact-based analysis and generating and selecting appropriate courses of action to produce positive results.""",
    "Basic":
    """
        - Provides timely solutions to problems and decision dilemmas that have clear-cut options and/or choices and whose solutions are available and can be accessed from a database or gleaned from an existing policy or process.
    """,
    "Intermediate":
    """
        - Provides timely solutions to problems and decision dilemmas that do not have clear-cut options and resolutions may require some analysis or creativity.
    """,
    "Advanced":
    """
        - Provides timely solutions to problems and decision dilemmas that do not have clear-cut options and assumptions are partial or minimal and need to be identified.
    """,
    "Superior":
    """
        - Provides timely solutions to problems even without available data and comes up with appropriate and sound alternatives to resolve a decision dilemma.
    """,
    },
    
    "Speaking Effectively": {
    "Description":
    """The ability to actively listen, understand and respond appropriately when interacting with individuals and groups.""",
    "Basic":
    """
        - Effectively delivers messages that simply focus on data, facts or information and requires minimal preparation or can be supported by available communication materials.
    """,
    "Intermediate":
    """
        - Effectively delivers messages that require some planning for the method used and the possible reception to the message; audience may be a controlled group (teams, or divisions).
    """,
    "Advanced":
    """
        - Effectively delivers messages that require careful planning for the method used and the possible impact of the message; audience may be a large group (office, organization).
    """,
    "Superior":
    """
        - Facilitate and influences target audience such as the heads of agency and external partner/clients.
    """,
    },
    
    "Strategic Planning": {
    "Description":
    """The ability to influence, realign the organization's strategic goals and directions; monitor and review data from various aspects of strategic and corporate planning and recommend enhancements.""",
    "Basic":
    """
        - Conducts research and gathers data and information to support corporate planning agenda
        - Consolidates issues and concerns of different offices/units with regard to their targets and accomplishments
        - Provides administrative support to the Performance Management Team in its review and evaluation of performance targets
    """,
    "Intermediate":
    """
        - Assesses the level of performance of the different offices based on their targets and accomplishments
        - Evaluates, analyzes and interprets the consolidated issues and concerns of the different offices based on targets and accomplishments
        - Organizes the logistical support for the Performance Management Team
    """,
    "Advanced":
    """
        - Develops linkages within the organization and with other government units and organizations to operate within the program's environment and achieve organization's goals
        - Recommends areas of focus and enhancements in the work plans/programs
        - Crafts short-term plans relative to work in the office or division
    """,
    "Superior":
    """
        - Translates the vision, mission and values of heads into effective strategies
        - Inspires and influences others to assume ownership pf organization's goals
        - Displays thinking and planning to ensure the organization moves towards its vision
        - Initiates, develops, coordinates and evaluates change management strategies to successfully bring about change in the organization
        - Acts decisively in a complex environment of ambiguity and multiple stakeholders
    """,
    },
    
    "Supplies and Property Management": {
    "Description":
    """The ability to plan and implement measures to efficiently allocate, utilize, maintain and dispose supplies and properties of the organization.""",
    "Basic":
    """
        - Coordinates schedules, attendance and logistics and assist in the facilitation of the Disposal Committee (Discom), BAC for Discom (BAC for D) meetings.
        - Facilitates the distribution of supplies and property to various offices / custodians.
        - Files documents for property and supplies such as but not limited to the following:
            -ARE
            -IRP
            -IIRUP
            -RSMI
            -WMR
            -RPCPPE
        - Takes charge of logistics for meetings such as but not limited to materials, venue and meals.
        - Receives and records the list of unserviceable Plant, Properties and Equipment (PPE) and other materials for disposal.
        - Maintains and updates property, supplies and equipment records in database/filing system.
    """,
    "Intermediate":
    """
        - Reviews completeness of documents/materials for DisCom meetings.
        - Prepares minutes of Discom and BAC for DisCom meetings.
        - Prepares the following Supplies and Property documents:
            -ARE
            -IRP
            -IIRUP
            -RSMI
            -WMR
            -RPCPPE
        - Monitors and prepares the Insurance of serviceable PPE.
        - Receives and inspects procured goods and services in accordance with the approved specifications.
        - Assists property custodians for the repair of properties / equipment.
        - Conducts regular inventory of PPE for all offices and updates employees' records (ARE, MR).
        - Conducts disposal through sale of waste/junk materials as the need arises.
    """,
    "Advanced":
    """
        - Reviews and validates various Supplies and Property reports:
            -ARE
            -IRP
            -IIRUP
            -RSMI
            -WMR
            -RPCPPE
        - Reviews existing policies on Property Management and recommends enhancements/ changes if necessary.
        - Develops and enhances supply distribution and inventory management systems.
        - Develops schedule of maintenance, repair and disposal of properties and equipment.
        - Reviews records of unserviceable Plant, Properties and Equipment (PPE) and other materials and recommends disposal.
    """,
    "Superior":
    """
        - Convenes the DisCom as the need arises.
        - Monitors the implementation of programs and activities on supply and property management.
        - Recommends enhancements/ changes to Supplies and Property Management policies based on reviews and evaluation conducted.
        - Recommends implementation of cost-cutting and internal control measures relative to the utilization of supplies and properties.
    """,
    },
    
    "Test Administration": {
    "Description":
    """The ability to plan, execute, monitor and report the implementation of examination related programs and activities.""",
    "Basic":
    """
        - Communicates examination venue and delivery of materials to concerned parties.
        - Reproduces and packages, examination forms/kits.
        - Distributes and retrieves examination materials.
        - Receives and records clean- matched file.
        - Files examination related issuances.
        - Writes simple pro-forma communications such as but not limited to acknowledgment and transmittal letters relative to test administration.
        - Prepares requirements on the liquidation/reimbursement of examination related expenses (such as but not limited to Office Order, Itinerary of travel, vouchers, PR/RIS, liquidation/ reimbursement report, etc.).
    """,
    "Intermediate":
    """
        - Prepares examination announcements/advisory.
        - Coordinates with partner agencies on examination related activities.
        - Evaluates examination applicant's personal information and verifies identity during personal appearances.
        - Prepares and prints application forms, examination attendance sheet, picture seat plan, certificate of eligibility, and other examination related forms.
        - Administers tests conducted at the Central Office.
        - Processes examination results.
        - Maintains and updates database of examination results.
        - Prepares report on the conduct of the pre-examination activities.
        - Consolidates examination reports/data submitted by Regional Offices.
        - Prepares replies to policy related queries on test administration.
    """,
    "Advanced":
    """
        - Creates, edits and deletes administration accounts for the CSC Central and Regional Offices.
        - Conducts briefing/orientation to examination representatives and delivery teams.
        - Consolidates and evaluates examination related statistical reports.
        - Develops examination calendar and timetable of activities.
        - Prepares narrative report (e.g Collection, Expenses and Net Income)
        - Develops and enhances policies relative to the administration of examinations.
        - Develops manual on test administration.
    """,
    "Superior":
    """
        - Develops communication plan on policies, guidelines and issuances on the administration of examination.
        - Conducts training for examination representatives/test administrators/examiners and supervisors.
        - Reviews and recommends manual on test administration.
        - Identifies trends and developments in the administration of examination and recommends enhancements to current procedures, processes and policies.
    """,
    },

    "Thinking Strategically and Creatively": {
    "Description":
    """The ability to "see the big picture", think multi-dimensionally, craft innovative solutions, identify connections between situations or things that are not obviously related, and come up with new ideas and different ways to enhance organizational effectiveness and responsiveness.""",
    "Basic":
    """
        - Displays awareness and supports the vision, mission, values, objectives and purposes of the agency or organization.
    """,
    "Intermedite":
    """
        - Creates or defines goals and initiatives based on how one can support, extend or align to the goals of one's department or functional area.
    """,
    "Advanced":
    """
        - Plans, crafts and adapts strategies for achieving the vision, mission and objectives of the agency or organization and secures the proper implementation of these strategies.
    """,
    "Superior":
    """
        - Interprets the complex and volatile nature of the environment to the agency or organization and adaptively moves it into a more strategic position where it can better address the challenges it faces both now and into the future.
    """,
    },

    "Writing Effectively": {
    "Description":
    """The ability to write in clear, concise and coherent manner using different tools to convey information or express ideas effectively.""",
    "Basic":
    """
        - Refers to and/or uses existing communication materials or templates t produce own written work.
    """,
    "Intermediate":
    """
        - Edits existing or customizes available communication materials to produce an appropriate written work.
    """,
    "Advanced":
    """
        - Produces written work from scratch with some guidelines while complying to agreed or prescribed standards of communicating within the bureaucracy.
    """,
    "Superior":
    """
        - Designs and/or sets standards for a written material used within the bureaucracy while demonstrating independence producing written work.
    """,
    },

    "Written Communication": {
    "Description":
    """The ability to express fats and ideas in writing in a clear, convincing and organized manner.""",
    "Basic":
    """
        - Practices and uses the different written business communication formats used in the office.
        - Writes routine correspondence/communications based on readily available information, data, with minimal information, spelling and grammatical ergots.
        - Secures information from required references for specific purposes.
        - Prepares the content of a written work for a given topic.
    """,
    "Intermediate":
    """
        - Writes narrative/descriptive reports and related writing assignments based on readily available information.
        - Self-edits words, numbers, letters, sentences, including capitalization, lower case, punctuation and phonic notation.
        - Demonstrates clarity, fluency, impact, conciseness in his/her written communications.
        - Prepares technical reports and related documents involving the analysis of various interrelated data or activities/projects/current issues.
        - Creates grammatically and structurally proper and articulate written composition, including formal letters and technical reports of considerable difficulty.
    """,
    "Advanced":
    """
        - Edits and corrects various correspondences/documentation of staff.
        - Guides and coaches others on the output of their work t ensure quality.
        - Writes complex technical reports using clear terminology and concise format for use by high-level decision-makers.
        - Reviews technical reports, edits materials, and provides suggestions to improve clarity while ensuring documents are targeted to the intended audience.
        - Creates convincing, complex, and articulate written documents.
    """,
    "Superior":
    """
        - Develops written communication strategies which meet information requirements and the end-user or beneficiaries of its programs and services.
        - Writes, reviews, and publishes advanced research findings and guidelines to be made available to other group and agencies.
        - Writes white papers on key agency objectives for use by high-level officials.
        - Reviews and critiques the writing of others in a constructive and substantive manner.
    """,
    
        
        
    
    
    
        
    
    









    
    }                                                                                                           
}

# Page Title
st.title('Learning Needs Analysis - eLearning Preferences')

# Function to create bold labels
def bold_label(label):
    return f"**{label}**"

# Input fields
st.markdown(bold_label('Full Name'))
full_name = st.text_input('')
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

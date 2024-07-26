import os
import pandas as pd
import sqlite3
import streamlit as st
#from fpdf import FPDF
#import webbrowser
#from streamlit_modal import Modal

# Competency descriptions from dropdown list
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

# users dictionary
user_passwords = {
    'admin': 'admin',
    'a.abad': 'empid1',
    'm.abellano': 'empid2',
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
    'b.baldos': 'empid29',
    'l.balete': 'empid30',
    'j.ballon': 'empid31',
    'd.barja': 'empid32',
    'am.barnuevo': 'empid33',
    'w.barola': 'empid34',
    'j.beato': 'empid35',
    'a.belardo': 'empid36',
    'v.beler': 'empid37',
    'j.benasa': 'empid38',
    'i.benitez': 'empid39',
    's.benito': 'empid40',
    'j.bercilla': 'empid41',
    'r.bilaran': 'empid42',
    'e.billudo': 'empid43',
    'yig.bon': 'empid44',
    'je.boñon': 'empid45',
    'bv.borromeo': 'empid46',
    'e.buag': 'empid47',
    'j.buendia': 'empid48',
    'nme.bulawan': 'empid49',
    'f.cajerel': 'empid50',
    'j.calixtro': 'empid51',
    'a.caña': 'empid52',
    'ni.caparas': 'empid53',
    'g.cardel': 'empid54',
    'm.casulla': 'empid55',
    'r.casulla': 'empid56',
    'j.cerdena': 'empid57',
    'r.cerdeña': 'empid58',
    'ka.codorniz': 'empid59',
    'h.dagsil': 'empid60',
    'r.dalma': 'empid61',
    'k.dantes': 'empid62',
    'j.delayre': 'empid63',
    'j.domens': 'empid64',
    's.ebio': 'empid65',
    'mj.espartinez': 'empid66',
    'e.espejo': 'empid67',
    'n.espinosa': 'empid68',
    'r.esquilador': 'empid69',
    's.fermanes': 'empid70',
    'kl.francia': 'empid71',
    'v.fruelda': 'empid72',
    'v.goyena': 'empid73',
    'j.grebialde': 'empid74',
    'o.grebialde': 'empid75',
    'c.hernandez': 'empid76',
    'jm.hollon': 'empid77',
    'r.huab': 'empid78',
    'j.jadie': 'empid79',
    'n.jadie': 'empid80',
    'j.jovero': 'empid81',
    'b.jovero': 'empid82',
    'w.lee': 'empid82',
    'jv.lim': 'empid83',
    'e.lisay': 'empid84',
    'j.llandelar': 'empid85',
    'l.lorena': 'empid86',
    'j.loreno': 'empid87',
    'l.lorin': 'empid88',
    'r.lubiano': 'empid87',
    'c.lunar': 'empid88',
    'i.macabihag': 'empid89',
    'o.macasinag': 'empid90',
    'r.madrinian': 'empid91',
    'c.maravilla': 'empid92',
    'd.mendenilla': 'empid93',
    'jk.mendez': 'empid94',
    'rjr.mira': 'empid95',
    'r.mira': 'empid96',
    'a.miras': 'empid97',
    'j.misolania': 'empid98',
    'h.morada': 'empid99',
    'sg.morante': 'empid100',
    'c.morco': 'empid101',
    'r.napili': 'empid102',
    'e.navarro': 'empid103',
    'aj.nieto': 'empid104',
    'n.nodado': 'empid105',
    'm.nolledo': 'empid106',
    'a.noguchi': 'empid107',
    'j.nova': 'empid108',
    'alvin.nuñez': 'empid109',
    'andrew.nuñez': 'empid110',
    'e.nuñez': 'empid111',
    'j.nuñez': 'empid112',
    'l.nuñez': 'empid113',
    'ml.nuñez': 'empid114',
    'j.olavario': 'empid115',
    'd.olimpo': 'empid116',
    'g.orejo': 'empid117',
    'rv.padre': 'empid118',
    'ms.palattao': 'empid119',
    'c.panagan': 'empid120',
    'kd.pasano': 'empid121',
    'r.pasibe': 'empid122',
    'v.paular': 'empid123',
    'j.perez': 'empid124',
    'f.pornelosa': 'empid125',
    'rs.prieto': 'empid126',
    'e.pura': 'empid127',
    'il.de leoz': 'empid128',
    'e.reales': 'empid129',
    'a.red': 'empid130',
    'r.red': 'empid131',
    'sj.rodis': 'empid132',
    'da.rosal': 'empid133',
    'j.sagales': 'empid134',
    'aa.samaniego': 'empid135',
    'd.santidad': 'empid136',
    'e.sapanta': 'empid137',
    'jv.solteo': 'empid138',
    'ms.valencia': 'empid139',
    'v.villar': 'empid140',
    'r.villareal': 'empid141',
}

user_display_names = {
    'admin': 'Admin',
    'a.abad': 'Alessandro Abad',
    'm.abellano': 'Mark Abellano',
    'a.abiera': 'Arthur Abiera',
    'a.abrique': 'Anthony Abrique',
    'z.alcazar': 'Zharra Alcazar',
    's.allorde': 'Shiela Allorde',
    'mb.añasco': 'Mark Bryan Añasco',
    'r.ancermo': 'Romel Ancermo',
    'a.abiera': 'Arthur Abiera',
    'r.aperin': 'Reymon Aperin',
    'r.apuli': 'Rodel Apuli',
    'mc.conception': 'Ma. Conception Arenal',
    'r.arias': 'Randy Arias',
    'j.armecin': 'Jhomel Armecin',
    'r.atento': 'Roslyn Atento',
    'r.atun': 'Richard Atun',
    'cl.ayala': 'Christian Louie Ayala',
    'f.ayala': 'Franklin Ayala',
    'mf.aydalla': 'Ma. Francia Aydalla',
    'j.ayson': 'Joseph Ayson',
    'a.azores': 'Antonio Azores Jr.',
    'r.azores': 'Ramil Azores',
    'a.azupardo': 'Arnel Azupardo',
    'j.azupardo': 'Jesue Azupardo',
    'k.azupardo': 'Kevin Azupardo',
    'kj.bagnes': 'Kristian Jude Bagnes',
    'ma.balde': 'Miguel Aldrin Balde',
    'rd.balde': 'Ram Derick Balde',
    'b.baldos': 'Berly Baldos',
    'r.baldos': 'Rey Baldos',
    'l.balete': 'Lito Balete',
    'j.ballon': 'Jonathan Ballon',
    'g.bansale': 'Gerald Bansale',
    'd.barja': 'Dante Barja',
    'am.barnuevo': 'Ann Margaret Barnuevo',
    'j.beato': 'Joel Beato',
    'a.belardo': 'Ariel Belardo',
    'v.beler': 'Vener Beler',
    'jr.benasa': 'Jhone Rino Benasa',
    'i.benitez': 'Ismael Benitez',
    's.benito': 'Sally Benito',
    'kc.bequio': 'Kim KC Bequio',
    'j.bercilla': 'Jose Bercilla Jr.',
    'v.bermoy': 'Victor Bermoy',
    'r.bermudes': 'Raymund Bermudes',
    'r.bilaran': 'Rolando Bilaran',
    'e.billudo': 'Emil Billudo',
    'ad.bodota': 'Alwin Domingo Bodota',
    'yig.bon': 'Yrick Ian Garel Bon',
    'je.boñon': 'Jessa Erika Boñon',
    'bv.borromeo': 'Barbie Vonetta Borromeo',
    's.brillo': 'Serdan Brillo',
    'e.buag': 'Ernani Buag',
    'nme.bulawan': 'Nezzie Marie Eloiza Bulawan',
    'f.cajerel': 'Floro Cajerel',
    'j.calixtro': 'John Calixtro',
    'a.caña': 'Archie Caña',
    'ni.caparas': 'Neil Ian Caparas',
    'g.cardel': 'Gutchil Cardel',
    'm.casulla': 'Marlon Casulla',
    'r.casulla': 'Rex Casulla',
    'j.cerdeña': 'Joven Cerdeña',
    'r.cerdeña': 'Rodolfo Cerdeña Jr.',
    'ka.codorniz': 'Karla Ann Codorniz',
    'h.dagsil': 'Hilde Dagsil',
    'r.dalma': 'Ricky Dalma',
    'k.dantes': 'Karen Dantes',
    'j.del ayre': 'Joseph Del Ayre',
    'ad.delovino': 'Anna Dominique Delovino',
    'd.delovino': 'Dominguito Delovino Jr.',
    'j.domens': 'Jhonie Domens',
    's.ebio': 'Santiago Ebio',
    'mj.espartinez': 'Mark John Espartinez',
    'e.espejo': 'Elvie Espejo',
    'n.espinosa': 'Noel Espinosa',
    'r.esquilador': 'Raymond Esquilador',
    'e.esquivel': 'Edsel Esquivel',
    's.fermanes': 'Segundino Fermanes Jr.',
    'kl.francia': 'Karl Lester Francia',
    'v.fruelda': 'Vicente, Fruelda',
    'v.goyena': 'John Calixtro',
    'j.grebialde': 'Jonathan Grebialde',
    'o.grebialde': 'Oliver Grebialde',
    'c.hernandez': 'Carolyn Hernandez',
    'jm.hollon': 'James Morris Hollon',
    'r.huab': 'Rolando Huab',
    'j.Jadie': 'Jadie Jovencio IV',
    'n.jadie': 'Nerio Jadie',
    'j.jovero': 'Jonathan Jovero',
    'b.jovero': 'Bernadette Jovero',
    'w.lee': 'Warren Lee',
    'jv.lim': 'John Vincent Lim',
    'e.lisay': 'Emmanuel Lisay',
    'j.llandelar': 'Jayrand Llandelar',
    'l.lorena': 'Lourdes Lorena',
    'j.loreno': 'Jay Loreno',
    'r.lubiano': 'Rafael Lubiano',
    'c.lunar': 'Cherry Lunar',
    'i.macabihag': 'Israel Macabihag',
    'o.macasinag': 'Onofre Macasinag Jr.',
    'k.manda': 'Karl Manda',
    'c.maravilla': 'Clevin Maravilla',
    'd.mendenilla': 'Danilo Mendenilla',
    'jk.mendez': 'John Kenneth Mendez',
    'a.miras': 'Alan Miras',
    'j.misolania': 'Joonee Misolania',
    'h.morada': 'Hannah Morada',
    'sg.morante': 'San Gray Morante',
    'c.morco': 'Christopher Morco',
    'e.navarro': 'Edwin Navarro',
    'aj.nieto': 'Anthony John Nieto',
    'n.nodado': 'Nolita Nodado',
    'm.nolledo': 'Melanie Nolledo',
    'a.noguchi': 'Akemi Noguchi',
    'j.nova': 'Jonard Nova',
    'alvin.nuñez': 'Alvin Nuñez',
    'andrew.nuñez': 'Andrew Nuñez',
    'e.nuñez': 'Eric Nuñez',
    'j.nuñez': 'Joffrey Nuñez',
    'l.nuñez': 'Lilane Nuñez',
    'ml.nuñez': 'Ma. Librada Nuñez',
    'j.olavario': 'Joed Olavario',
    'd.olimpo': 'Darwin Olimpo',
    'g.orejo': 'Ginena Orejo',
    'rv.padre': 'Ramon Victor Padre',
    'ms.palattao': 'Ma. Suzette Palattao',
    'c.panagan': 'Cesar Panagan',
    'kd.pasano': 'Kate Darla Pasano',
    'r.pasibe': 'Rochelle Pasibe',
    'v.paular': 'Vhenjie Paular',
    'j.perez': 'Jay Perez',
    'f.pornelosa': 'Francisco Pornelosa',
    'rs.prieto': 'Ralph Sheirwin Prieto',
    'e.pura': 'Emy pura',
    'il.de leoz': 'Ivy-Lynn Raguindin-De Leoz',
    'e.reales': 'Enah Reales',
    'a.red': 'Aguinaldo Red',
    'r.red': 'Rosell Red',
    'sj.rodis': 'Shere Jane Rodis',
    'sa.roldan': 'Shaira Antonieta Roldan',
    'da.rosal': 'Darryl Andrie Rosal',
    'j.sagales': 'Justino Sagales',
    'aa.samaniego': 'Arman Ador Samaniego',
    'd.santidad': 'Diane Santidad',
    'e.sapanta': 'Elaine Sapanta',
    'ms.valencia': 'Ma. Shanice Valencia',
    'v.villar': 'Veronica Villar',
    'r.villareal': 'Raul Villareal',
}

# Database connection to SQLite database
conn = sqlite3.connect('your_database.db')
c = conn.cursor()

# Function to generate PDF
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
#st.sidebar.image("https://raw.githubusercontent.com/Klfnovice/lnatabulation/main/LCWD%20Logo%20-%20Copy.png", use_column_width=True)
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
    st.warning('this site is currently under construction, \"please stand by\"')






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

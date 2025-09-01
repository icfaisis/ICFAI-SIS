import streamlit as st
import pandas as pd
from PIL import Image

# --- Dummy Data (as before) ---
student_data = {
    "username": "23STUCHH011068",
    "password": "2006KM",
    "name": "KRISHNA MISHRA",
    "enrollment": "23STUCHH011068",
    "email": "krishnamishra23@ifheindia.org",
    "profile_pic": "krishna_mishra.jpg"
}

semester_data = {
    "Semester 1": {
        "subjects": ["Applied Physics", "Applied Chemistry", "Mathematics-I", "Basic Electrical and Electronics Engineering", "Introduction to Computer Science", "Engineering Graphics and Design"],
        "attendance": [90, 85, 92, 88, 95, 87],
        "cgpa": 5.46
    },
    "Semester 2": {
        "subjects": ["Mathematics-II", "Data Structures", "Object-Oriented Programming using C++", "Digital Logic and Computer Architecture", "Communication Skills", "Environmental Science"],
        "attendance": [88, 91, 93, 89, 85, 90],
        "cgpa": 5.73
    },
    "Semester 3": {
        "subjects": ["Discrete Mathematics", "Operating Systems", "Database Management Systems", "Design and Analysis of Algorithms", "Software Engineering", "Computer Networks"],
        "attendance": [91, 87, 90, 94, 86, 92],
        "cgpa": 6.10
    },
    "Semester 4": {
        "subjects": ["Theory of Computation", "Machine Learning", "Artificial Intelligence", "Web Technology", "Microprocessor and Interfacing", "Cyber Security"],
        "attendance": [90, 88, 92, 85, 91, 89],
        "cgpa": 6.94
    },
    "Semester 5": {
        "subjects": ["Compiler Design", "Cloud Computing", "Data Science", "Natural Language Processing", "Distributed Systems", "Mobile Application Development"],
        "attendance": [89, 93, 87, 90, 85, 91],
        "cgpa": 7.50
    }
}

# --- Custom CSS for Improved UI/UX ---
def apply_custom_css():
    st.markdown("""
        <style>
        .main-header {
            font-size: 2.5em;
            font-weight: bold;
            color: #004d40;
            text-align: center;
            margin-bottom: 20px;
            padding: 10px;
            border-bottom: 2px solid #004d40;
        }
        .subheader {
            font-size: 1.5em;
            color: #333333;
            margin-top: 20px;
        }
        .sidebar-header {
            font-size: 1.8em;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            padding: 15px;
            background-color: #004d40;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .dashboard-card {
            background-color: #e0f2f1;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .profile-pic {
            border-radius: 50%;
            border: 4px solid #004d40;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }
        .data-label {
            font-weight: bold;
            color: #004d40;
        }
        .stButton>button {
            width: 100%;
            border-radius: 50px;
            background-color: #00695c;
            color: white;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #004d40;
            color: white;
        }
        .st-emotion-cache-1wv0k83.ef3psqc11 {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
        }
        .st-emotion-cache-1wv0k83.ef3psqc11 .st-emotion-cache-1wv0k83.ef3psqc11 {
            background-color: #e0f2f1;
        }
        </style>
    """, unsafe_allow_html=True)

# --- Pages Functions (with UI/UX improvements) ---
def login_page():
    st.markdown('<h1 class="main-header">ICFAI UNIVERSITY</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="subheader" style="text-align: center;">Student Portal Login</h2>', unsafe_allow_html=True)

    with st.container():
        st.write("---")
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        if st.button("Login"):
            if username == student_data["username"] and password == student_data["password"]:
                st.session_state["logged_in"] = True
                st.rerun()
            else:
                st.error("Invalid username or password. Please try again.")
        st.write("---")

def dashboard_page():
    st.markdown(f'<h1 class="main-header">Welcome, {student_data["name"]}!</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        try:
            image = Image.open(student_data["profile_pic"])
            st.image(image, width=180, use_column_width=False, output_format='PNG', clamp=True)
        except FileNotFoundError:
            st.warning("Profile picture not found.")
            
    with col2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown(f'**<span class="data-label">Enrollment No:</span>** {student_data["enrollment"]}', unsafe_allow_html=True)
        st.markdown(f'**<span class="data-label">Email:</span>** {student_data["email"]}', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("Your Academic Snapshot")
    st.info("Here you can find a quick overview of your academic progress. Use the sidebar to navigate to detailed reports.")

def attendance_page():
    st.markdown('<h1 class="main-header">Attendance Report</h1>', unsafe_allow_html=True)
    
    selected_semester = st.selectbox("Select Semester", list(semester_data.keys()), key="attendance_sem")
    
    st.markdown("---")
    st.subheader(f"Semester {selected_semester.split(' ')[1]} Attendance")
    
    subjects = semester_data[selected_semester]["subjects"]
    attendance = semester_data[selected_semester]["attendance"]
    
    df_attendance = pd.DataFrame({
        "Subject": subjects,
        "Attendance (%)": attendance
    })

    st.dataframe(df_attendance.style.highlight_max(axis=0, subset=['Attendance (%)'], color='lightgreen').highlight_min(axis=0, subset=['Attendance (%)'], color='salmon'), use_container_width=True)

def gradelist_page():
    st.markdown('<h1 class="main-header">Grade Report</h1>', unsafe_allow_html=True)

    grades = []
    for sem, data in semester_data.items():
        grades.append({"Semester": sem, "CGPA": data["cgpa"]})

    df_grades = pd.DataFrame(grades)
    
    st.subheader("Semester-wise CGPA")
    st.dataframe(df_grades, use_container_width=True)

def resources_page():
    st.markdown('<h1 class="main-header">Resources</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">A place for all your study materials.</p>', unsafe_allow_html=True)
    
    st.subheader("General Resources")
    st.success("This section will be populated with lecture notes, sample papers, and other academic resources.")
    
    st.subheader("Quick Links")
    st.markdown("- [University Library Portal](https://www.google.com)")
    st.markdown("- [Academic Calendar](https://www.google.com)")

def internship_page():
    st.markdown('<h1 class="main-header">Internship Details</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;">Showcasing your professional experience.</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("IP - 1")
    st.markdown("- **Company:** VISAM AI")
    st.markdown("- **Grade:** A")
    st.markdown("- **CGPA:** 9.0")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Main App Logic ---
apply_custom_css()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login_page()
else:
    with st.sidebar:
        st.markdown('<div class="sidebar-header">Student Portal</div>', unsafe_allow_html=True)
        page = st.radio("Go to", ["Dashboard", "Attendance", "Grade List", "Resources", "Internship"], help="Select a page to navigate")
        st.markdown("---")
        if st.button("Logout", help="Click to log out of your account"):
            st.session_state["logged_in"] = False
            st.rerun()

    if page == "Dashboard":
        dashboard_page()
    elif page == "Attendance":
        attendance_page()
    elif page == "Grade List":
        gradelist_page()
    elif page == "Resources":
        resources_page()
    elif page == "Internship":
        internship_page()

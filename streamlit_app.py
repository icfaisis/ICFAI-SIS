import streamlit as st
import pandas as pd
from PIL import Image

# Dummy data for demonstration purposes
# Please update this with your actual data
student_data = {
    "username": "23STUCHH011068",
    "password": "2006KM",
    "name": "KRISHNA MISHRA",
    "enrollment": "23STUCHH011068",
    "email": "krishnamishra23@ifheindia.org",
    "profile_pic": "krishna_mishra.jpg"
}

# Semester subjects and attendance data (dummy data)
# NOTE: This is based on a sample B.Tech CSE curriculum.
# Please replace this with the official ICFAI University curriculum.
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
    
}

# --- Login Page ---
def login_page():
    st.title("ICFAI UNIVERSTIY")
    st.subheader("Login to Student Portal")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == student_data["username"] and password == student_data["password"]:
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid username or password")

# --- Dashboard Page ---
def dashboard_page():
    st.title("Student Dashboard")
    st.header(student_data["name"])

    try:
        image = Image.open(student_data["profile_pic"])
        st.image(image, width=150)
    except FileNotFoundError:
        st.warning("Profile picture not found. Please place 'krishna_mishra.jpg' in the same directory.")

    st.write(f"**Enrollment No:** {student_data['enrollment']}")
    st.write(f"**Email:** {student_data['email']}")

# --- Attendance Page ---
def attendance_page():
    st.title("Attendance Report")
    selected_semester = st.selectbox("Select Semester", list(semester_data.keys()))

    if selected_semester:
        subjects = semester_data[selected_semester]["subjects"]
        attendance = semester_data[selected_semester]["attendance"]

        df_attendance = pd.DataFrame({
            "Subject": subjects,
            "Attendance (%)": attendance
        })

        st.dataframe(df_attendance, use_container_width=True)

# --- Grade List Page ---
def gradelist_page():
    st.title("Grade Report")

    grades = []
    for sem, data in semester_data.items():
        grades.append({"Semester": sem, "CGPA": data["cgpa"]})

    df_grades = pd.DataFrame(grades)
    st.dataframe(df_grades, use_container_width=True)

# --- Resources Page ---
def resources_page():
    st.title("Resources")
    st.info("This section is for displaying academic resources like e-books, lecture notes, etc.")
    # You can add more content here, e.g.,
    # st.subheader("Subject-wise Notes")
    # st.markdown("- [Data Structures Notes](link_to_pdf)")

# --- Internship Page ---
def internship_page():
    st.title("Internship Details")
    st.markdown("**Internship Program 1**")
    st.markdown("- **Company:** VISAM AI")
    st.markdown("- **Grade:** A")
    st.markdown("- **CGPA:** 9.0")

# --- Main App Logic ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login_page()
else:
    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to", ["Dashboard", "Attendance", "Grade List", "Resources", "Internship"])
        if st.button("Logout"):
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

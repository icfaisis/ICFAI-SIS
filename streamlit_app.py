import streamlit as st
import pandas as pd

# User data for login
USER_DATA = {
    "23STUCHH011068": {
        "name": "KRISHNA MISHRA",
        "enrollment_no": "23STUCHH011068",
        "phone_no": "9391615864",
        "email": "krishamishra23@ifheindia.org",
        "picture": "profile_pic.jpg",  # Provide your profile pic file here
        "password": "2006KM"
    }
}

############ Attendance Data from screenshots ############
def get_attendance_data():
    return {
        1: [
            {"Course Code": "CS101", "Subject Name": "DISCRETE ORGANISATION AND ARCHITECTURE", "Total Sessions": 45, "Sessions Attended": 44},
            {"Course Code": "CS102", "Subject Name": "DATA STRUCTURES", "Total Sessions": 41, "Sessions Attended": 38},
            {"Course Code": "CS103", "Subject Name": "NUMERICAL ANALYSIS", "Total Sessions": 36, "Sessions Attended": 33},
            {"Course Code": "CS104", "Subject Name": "LANGUAGE AND COMMUNICATION", "Total Sessions": 27, "Sessions Attended": 26},
            {"Course Code": "CS105", "Subject Name": "PRINCIPLES OF PROGRAMMING", "Total Sessions": 35, "Sessions Attended": 32},
            {"Course Code": "CS106", "Subject Name": "MANAGEMENT PRINCIPLES", "Total Sessions": 36, "Sessions Attended": 32},
            {"Course Code": "CS107", "Subject Name": "PROBABILITY AND STATISTICS", "Total Sessions": 29, "Sessions Attended": 26},
        ],
        2: [
            {"Course Code": "CS201", "Subject Name": "DESIGN AND ANALYSIS OF ALGORITHMS", "Total Sessions": 41, "Sessions Attended": 35},
            {"Course Code": "CS202", "Subject Name": "OPERATING SYSTEMS", "Total Sessions": 41, "Sessions Attended": 37},
            {"Course Code": "CS203", "Subject Name": "ARTIFICIAL INTELLIGENCE AND MANAGEMENT", "Total Sessions": 37, "Sessions Attended": 31},
            {"Course Code": "CS204", "Subject Name": "DATABASE MANAGEMENT SYSTEM", "Total Sessions": 35, "Sessions Attended": 31},
            {"Course Code": "CS205", "Subject Name": "OBJECT ORIENTED PROGRAMMING", "Total Sessions": 37, "Sessions Attended": 30},
            {"Course Code": "CS206", "Subject Name": "LANGUAGE AND COMMUNICATION SKILLS", "Total Sessions": 27, "Sessions Attended": 26},
            {"Course Code": "CS207", "Subject Name": "THEORY OF COMPUTATION", "Total Sessions": 27, "Sessions Attended": 21},
        ],
        3: [
            {"Course Code": "CS301", "Subject Name": "Data Structure", "Total Sessions": 46, "Sessions Attended": 36},
            {"Course Code": "CS302", "Subject Name": "Engineering Mathematics", "Total Sessions": 43, "Sessions Attended": 34},
            {"Course Code": "CS303", "Subject Name": "High Performance Computing", "Total Sessions": 39, "Sessions Attended": 32},
            {"Course Code": "CS304", "Subject Name": "Programming for Artificial Intelligence", "Total Sessions": 35, "Sessions Attended": 26},
            {"Course Code": "CS305", "Subject Name": "Psychology and its Aspects", "Total Sessions": 30, "Sessions Attended": 27},
            {"Course Code": "CS306", "Subject Name": "Professional Communication", "Total Sessions": 16, "Sessions Attended": 13},
        ],
        4: [
            {"Course Code": "CS401", "Subject Name": "Basic Electronics", "Total Sessions": 46, "Sessions Attended": 30},
            {"Course Code": "CS402", "Subject Name": "Computer Programming", "Total Sessions": 43, "Sessions Attended": 32},
            {"Course Code": "CS403", "Subject Name": "Digital Electronics", "Total Sessions": 41, "Sessions Attended": 22},
            {"Course Code": "CS404", "Subject Name": "Language and Communication", "Total Sessions": 35, "Sessions Attended": 18},
            {"Course Code": "CS405", "Subject Name": "Logic Design and Theory of Computation", "Total Sessions": 27, "Sessions Attended": 15},
            {"Course Code": "CS406", "Subject Name": "Logic Analysis and Ordinary Differential Equations", "Total Sessions": 18, "Sessions Attended": 9},
        ]
    }

############ Grade Data and Grade Points ############
def get_grade_data():
    return [
        # Semester 1
        {"Semester": 1, "Course Code": "CS101", "Course Name": "DISCRETE ORGANISATION AND ARCHITECTURE", "Credits": 3, "Grade": "A"},
        {"Semester": 1, "Course Code": "CS102", "Course Name": "DATA STRUCTURES", "Credits": 4, "Grade": "A"},
        {"Semester": 1, "Course Code": "CS103", "Course Name": "NUMERICAL ANALYSIS", "Credits": 3, "Grade": "A"},
        {"Semester": 1, "Course Code": "CS104", "Course Name": "LANGUAGE AND COMMUNICATION", "Credits": 2, "Grade": "B+"},
        {"Semester": 1, "Course Code": "CS105", "Course Name": "PRINCIPLES OF PROGRAMMING", "Credits": 3, "Grade": "A"},
        {"Semester": 1, "Course Code": "CS106", "Course Name": "MANAGEMENT PRINCIPLES", "Credits": 3, "Grade": "A"},
        {"Semester": 1, "Course Code": "CS107", "Course Name": "PROBABILITY AND STATISTICS", "Credits": 2, "Grade": "A"},
        # Semester 2
        {"Semester": 2, "Course Code": "CS201", "Course Name": "DESIGN AND ANALYSIS OF ALGORITHMS", "Credits": 4, "Grade": "B"},
        {"Semester": 2, "Course Code": "CS202", "Course Name": "OPERATING SYSTEMS", "Credits": 4, "Grade": "B+"},
        {"Semester": 2, "Course Code": "CS203", "Course Name": "ARTIFICIAL INTELLIGENCE AND MANAGEMENT", "Credits": 3, "Grade": "B+"},
        {"Semester": 2, "Course Code": "CS204", "Course Name": "DATABASE MANAGEMENT SYSTEM", "Credits": 3, "Grade": "A"},
        {"Semester": 2, "Course Code": "CS205", "Course Name": "OBJECT ORIENTED PROGRAMMING", "Credits": 4, "Grade": "B+"},
        {"Semester": 2, "Course Code": "CS206", "Course Name": "LANGUAGE AND COMMUNICATION SKILLS", "Credits": 2, "Grade": "A"},
        {"Semester": 2, "Course Code": "CS207", "Course Name": "THEORY OF COMPUTATION", "Credits": 2, "Grade": "A"},
        # Semester 3
        {"Semester": 3, "Course Code": "CS301", "Course Name": "Data Structure", "Credits": 4, "Grade": "A"},
        {"Semester": 3, "Course Code": "CS302", "Course Name": "Engineering Mathematics", "Credits": 4, "Grade": "B+"},
        {"Semester": 3, "Course Code": "CS303", "Course Name": "High Performance Computing", "Credits": 3, "Grade": "A"},
        {"Semester": 3, "Course Code": "CS304", "Course Name": "Programming for Artificial Intelligence", "Credits": 3, "Grade": "A"},
        {"Semester": 3, "Course Code": "CS305", "Course Name": "Psychology and its Aspects", "Credits": 2, "Grade": "A"},
        {"Semester": 3, "Course Code": "CS306", "Course Name": "Professional Communication", "Credits": 2, "Grade": "B+"},
        # Semester 4
        {"Semester": 4, "Course Code": "CS401", "Course Name": "Basic Electronics", "Credits": 3, "Grade": "A"},
        {"Semester": 4, "Course Code": "CS402", "Course Name": "Computer Programming", "Credits": 3, "Grade": "A"},
        {"Semester": 4, "Course Code": "CS403", "Course Name": "Digital Electronics", "Credits": 3, "Grade": "A"},
        {"Semester": 4, "Course Code": "CS404", "Course Name": "Language and Communication", "Credits": 2, "Grade": "A"},
        {"Semester": 4, "Course Code": "CS405", "Course Name": "Logic Design and Theory of Computation", "Credits": 3, "Grade": "A"},
        {"Semester": 4, "Course Code": "CS406", "Course Name": "Logic Analysis and Ordinary Differential Equations", "Credits": 2, "Grade": "A"},
    ]

# Map grades to points (approximate to match CGPA near 6.98)
GRADE_POINTS = {
    "A": 6.5,
    "A+": 6.8,
    "A++": 7.0,
    "B+": 5.5,
    "B": 5.0,
    "C": 4.0,
    "D": 3.0,
    "F": 0.0
}

# Streamlit Session State Init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None

# Login page with centered UI and college name header
def login():
    st.markdown(
        """
        <style>
        .main {background-color: #ffffff;}
        .stTextInput > div > div > input {
            background-color: #f0f0f0;
            color: #000000;
            font-size: 18px;
        }
        .stApp {background-color: #ffffff;}
        .login-container {
            display: flex; flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 70vh;
        }
        .college-header {
            text-align: center;
            font-size: 36px;
            font-family: 'Georgia', serif;
            margin-bottom: 24px;
            color: #000000;
            font-weight: bold;
            letter-spacing: 1px;
        }
        body {
            color: #000000;
        }
        </style>
        <div class="college-header">ICFAI UNIVERSITY</div>
        """, unsafe_allow_html=True
    )
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.title("College Login")
        enrollment_no = st.text_input("Enrollment No")
        password = st.text_input("Password", type="password")
        login_btn = st.button("Login")
        st.markdown('</div>', unsafe_allow_html=True)
        if login_btn:
            user = USER_DATA.get(enrollment_no)
            if user and user["password"] == password:
                st.session_state.logged_in = True
                st.session_state.user = user
                st.experimental_rerun()
            else:
                st.error("Invalid enrollment no or password")

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.experimental_rerun()

# Header: college logo, title and logout button
def header():
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        st.image("college_logo.png", width=50)
    with col2:
        st.header("College Portal")
    with col3:
        if st.button("Logout"):
            logout()

# Attendance Page
def attendance_page():
    header()
    st.subheader("Attendance")
    semester = st.selectbox("Select Semester", [1, 2, 3, 4])
    attendance_data = get_attendance_data()
    selected_data = attendance_data.get(semester, [])
    if selected_data:
        st.table(selected_data)
    else:
        st.info("Attendance data not available for this semester.")

# Grade List Page
def grade_list_page():
    header()
    st.subheader("Grade List")
    data = get_grade_data()
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    # Calculate CGPA approximate
    total_credits = df['Credits'].sum()
    weighted_points = (df['Credits'] * df['Grade'].map(GRADE_POINTS)).sum()
    total_grade = weighted_points / total_credits
    st.markdown(f"### Total Grade (Approximate CGPA): {total_grade:.2f}")

# Dashboard after login with sidebar navigation
def dashboard():
    header()
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Dashboard", "Attendance", "Grade List", "Faculty", "Timetable", "Resources"])

    user = st.session_state.user

    if selection == "Dashboard":
        st.subheader("Student Details")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(f"**Name:** {user['name']}")
            st.write(f"**Enrollment No:** {user['enrollment_no']}")
            st.write(f"**Phone No:** {user['phone_no']}")
            st.write(f"**College Email:** {user['email']}")
        with col2:
            st.image(user["picture"], width=120)
    elif selection == "Attendance":
        attendance_page()
    elif selection == "Grade List":
        grade_list_page()
    elif selection == "Faculty":
        st.subheader("Faculty Page Coming Soon!")
    elif selection == "Timetable":
        st.subheader("Timetable Page Coming Soon!")
    elif selection == "Resources":
        st.subheader("Resources Page Coming Soon!")

# Main function
def main():
    st.set_page_config(page_title="College Portal", layout="wide")
    if not st.session_state.logged_in:
        login()
    else:
        dashboard()

if __name__ == "__main__":
    main()

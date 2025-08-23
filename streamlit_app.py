# college_portal.py
import streamlit as st
import pandas as pd

# ---------------- User Data ----------------
USER_DATA = {
    "23STUCHH011068": {
        "name": "KRISHNA MISHRA",
        "enrollment_no": "23STUCHH011068",
        "phone_no": "9391615864",
        "email": "krishamishra23@ifheindia.org",
        "picture": "profile_pic.jpg",  # Put your picture in the same folder
        "password": "2006KM"
    }
}

# ---------------- Attendance ----------------
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

# ---------------- Grades ----------------
def get_grade_data():
    return [
        # (Trimmed for readability, you already listed all grades)
        {"Semester": 1, "Course Code": "CS101", "Course Name": "DISCRETE ORGANISATION AND ARCHITECTURE", "Credits": 3, "Grade": "A"},
        {"Semester": 1, "Course Code": "CS102", "Course Name": "DATA STRUCTURES", "Credits": 4, "Grade": "A"},
        {"Semester": 1, "Course Code": "CS103", "Course Name": "NUMERICAL ANALYSIS", "Credits": 3, "Grade": "A"},
        {"Semester": 1, "Course Code": "CS104", "Course Name": "LANGUAGE AND COMMUNICATION", "Credits": 2, "Grade": "B+"},
        # ... keep the rest as you defined
    ]

GRADE_POINTS = {
    "A": 7.0, "A+": 7.5, "B+": 6.5, "B": 6.0, "C": 5.0, "D": 4.0, "F": 0.0
}

# ---------------- Session State ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None

# ---------------- Login Page ----------------
def login():
    st.markdown("<h1 style='text-align: center; color: #0056B3;'>ICFAI UNIVERSITY</h1>", unsafe_allow_html=True)
    st.markdown("### Welcome to the College Portal")
    
    enrollment = st.text_input("Enrollment Number")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        user = USER_DATA.get(enrollment)
        if user and user["password"] == password:
            st.session_state.logged_in = True
            st.session_state.user = user
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid Enrollment Number or Password")

def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.experimental_rerun()

# ---------------- Dashboard ----------------
def dashboard():
    user = st.session_state.user
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ["Dashboard", "Attendance", "Grade List", "Faculty", "Timetable", "Resources", "Logout"])
    
    if choice == "Dashboard":
        st.header("Student Dashboard")
        col1, col2 = st.columns([2,1])
        with col1:
            st.write(f"**Name:** {user['name']}")
            st.write(f"**Enrollment No:** {user['enrollment_no']}")
            st.write(f"**Phone:** {user['phone_no']}")
            st.write(f"**Email:** {user['email']}")
        with col2:
            st.image(user["picture"], width=120)

    elif choice == "Attendance":
        st.header("Attendance")
        semester = st.selectbox("Select Semester", [1, 2, 3, 4])
        data = get_attendance_data().get(semester, [])
        st.table(pd.DataFrame(data))

    elif choice == "Grade List":
        st.header("Grade List")
        df = pd.DataFrame(get_grade_data())
        st.dataframe(df, use_container_width=True)

        # CGPA calculation
        df["Points"] = df["Grade"].map(GRADE_POINTS)
        total_points = (df["Credits"] * df["Points"]).sum()
        total_credits = df["Credits"].sum()
        cgpa = total_points / total_credits if total_credits else 0
        st.markdown(f"### Cumulative GPA (CGPA): {cgpa:.2f}")

    elif choice in ["Faculty", "Timetable", "Resources"]:
        st.header(choice)
        st.info("Coming Soon...")

    elif choice == "Logout":
        logout()

# ---------------- Main ----------------
def main():
    st.set_page_config(page_title="College Portal", layout="wide")
    if not st.session_state.logged_in:
        login()
    else:
        dashboard()

if __name__ == "__main__":
    main()

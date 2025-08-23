import streamlit as st

# -------------------------------
# Fake student database
# -------------------------------
students = {
    "23STUCHH011068": {
        "name": "Krishna Mishra",
        "enrollment": "23STUCHH011068",
        "password": "1234",  # demo password
        "course": "B.Tech CSE",
        "semester": 3,
        "subjects": ["DBMS", "Operating Systems", "Sociology", "Signal Processing"],
        "grades": {"DBMS": "A", "Operating Systems": "B+", "Sociology": "A-", "Signal Processing": "B"}
    },
    "23STUCHH011045": {
        "name": "Rahul Verma",
        "enrollment": "23STUCHH011045",
        "password": "5678",
        "course": "B.Tech AI",
        "semester": 5,
        "subjects": ["ML", "AI Ethics", "Deep Learning", "Cloud Computing"],
        "grades": {"ML": "A+", "AI Ethics": "A", "Deep Learning": "A-", "Cloud Computing": "B+"}
    }
}

# -------------------------------
# Session Initialization
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# -------------------------------
# Login Page
# -------------------------------
def login():
    st.title("ICFAI Student Information System")
    st.subheader("Login to Student Portal")

    enrollment = st.text_input("Enrollment Number")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if enrollment in students and students[enrollment]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.user = students[enrollment]
            st.success("Login successful! Redirecting...")
            st.rerun()  # 🔥 new method (replaces st.experimental_rerun)
        else:
            st.error("Invalid Enrollment Number or Password")

# -------------------------------
# Dashboard Page
# -------------------------------
def dashboard():
    user = st.session_state.user
    st.title(f"Welcome, {user['name']} 👋")
    st.write(f"**Enrollment Number:** {user['enrollment']}")
    st.write(f"**Course:** {user['course']}")
    st.write(f"**Semester:** {user['semester']}")

    st.subheader("📘 Subjects & Grades")
    for subject in user["subjects"]:
        grade = user["grades"].get(subject, "N/A")
        st.write(f"- **{subject}**: {grade}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.success("Logged out successfully!")
        st.rerun()

# -------------------------------
# Main
# -------------------------------
def main():
    if not st.session_state.logged_in:
        login()
    else:
        dashboard()

if __name__ == "__main__":
    main()

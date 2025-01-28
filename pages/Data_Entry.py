import streamlit as st
from sqlalchemy import text, create_engine
import urllib.parse

# Database connection setup
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "student_database"
DB_USER = "root"
DB_PASSWORD = urllib.parse.quote("Sabira@123")

db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# Function to insert data
def insert_data(firstname, lastname, title, age, nationality, registration_status, num_courses, num_semesters):
    query = text("""
        INSERT INTO Student_Data (firstname, lastname, title, age, nationality, registration_status, num_courses, num_semesters)
        VALUES (:firstname, :lastname, :title, :age, :nationality, :registration_status, :num_courses, :num_semesters)
    """)
    with engine.connect() as conn:
        conn.execute(query, {
            "firstname": firstname,
            "lastname": lastname,
            "title": title,
            "age": age,
            "nationality": nationality,
            "registration_status": registration_status,
            "num_courses": num_courses,
            "num_semesters": num_semesters
        })
        conn.commit()

# Streamlit UI
st.title("Data Entry Form")
with st.form("data_entry_form"):
    firstname = st.text_input("First Name")
    lastname = st.text_input("Last Name")
    title = st.selectbox("Title", ["", "Mr.", "Ms.", "Dr."])
    age = st.number_input("Age", min_value=18, max_value=110, step=1)
    nationality = st.selectbox("Nationality", ["", "Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
    registration_status = st.radio("Registration Status", ["Registered", "Not Registered"], index=1)
    num_courses = st.number_input("# Completed Courses", min_value=0, step=1)
    num_semesters = st.number_input("# Semesters", min_value=0, step=1)
    accepted = st.checkbox("I accept the terms and conditions.")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if accepted:
            if firstname.strip() and lastname.strip():
                try:
                    insert_data(firstname, lastname, title, age, nationality, registration_status, num_courses, num_semesters)
                    st.success("Data successfully submitted!")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("First name and last name are required.")
        else:
            st.warning("You must accept the terms and conditions.")

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

# Function to update data
def update_data(student_id, field, new_value):
    query = text(f"UPDATE Student_Data SET {field} = :new_value WHERE id = :student_id")
    with engine.connect() as conn:
        conn.execute(query, {"new_value": new_value, "student_id": student_id})
        conn.commit()

# Streamlit UI
st.title("Update Student Data")
student_id = st.number_input("Enter Student ID to Update", min_value=1, step=1)
field = st.selectbox("Field to Update", ["firstname", "lastname", "title", "age", "nationality", "registration_status", "num_courses", "num_semesters"])
new_value = st.text_input("New Value")
if st.button("Update"):
    try:
        update_data(student_id, field, new_value)
        st.success("Data successfully updated!")
    except Exception as e:
        st.error(f"Error updating data: {e}")

import streamlit as st
from sqlalchemy import create_engine, text
import urllib.parse

# Database connection setup
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "student_database"
DB_USER = "root"
DB_PASSWORD = urllib.parse.quote("Sabira@123")
db_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

# Function to fetch data
def fetch_data():
    query = text("SELECT * FROM Student_Data")  # Use text() for raw SQL queries
    try:
        with engine.connect() as conn:
            result = conn.execute(query)  # Execute the query
            columns = result.keys()  # Get column names
            data = [dict(zip(columns, row)) for row in result]  # Convert rows into a dictionary using column names
        return data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []  # Return an empty list on error

# Streamlit UI
st.title("View Student Data")

data = fetch_data()  # Fetch data

# Display the data
if data:
    st.table(data)  # Display the data as a table
else:
    st.info("No data found in the database.")

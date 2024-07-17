import streamlit as st
import mysql.connector
from datetime import datetime


def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Kavi@245',
        database='zoho'
    )
    
# User Registration

def register_user(username,password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    conn.close()
    
# Check if user exists and password is correct
def login_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s and password=%s", (username, password))
    conn.commit()
    conn.close()
    
    
# get User details

def get_user_details(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT age, dob, contact FROM users WHERE username=%s", (username))
    conn.commit()
    conn.close()
    
# update user details

def update_user_details(username, age, dob, contact):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET age=%s, dob=%s, contact=%s WHERE username=%s", (age, dob, contact, username))
    conn.commit()
    conn.close()
    
# streamlit app

st.title("User Authentication System")

# Navigation

page = st.sidebar.selectbox("Select Page",["Register","Login","Profile"])

if page == "Register":
    st.header("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if username and password:
            register_user(username, password)   
            st.success("User Registered Successfully")
    else:
        st.error("Please provide both username and password")
        
        
elif page == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.session_state["logged_in"] = True 
        st.session_state["username"] = username
        st.success("User Logged in Successfully")
    else:
        st.error("Invalid username and password")
        
    
elif page == "Profile":
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        st.subheader("Profile")
        username = st.session_state["username"]  
        user_details = get_user_details["username"]
        age = st.number_input("Age", value=user_details[0] if user_details else 0)
        dob = st.date_input("Date of Birth", value=datetime.strptime(user_details[1], "%Y-%m-%d") if user_details else datetime.today)
        contact = st.text_input("Contact", value=user_details[2] if user_details else "")
        if st.button("Update"):
            update_user_details(username, age, dob, contact)
            st.success("Profile Updated Successfully")
        else:
            st.error("Please log in to view your profile")
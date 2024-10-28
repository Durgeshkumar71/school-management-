import streamlit as st
import pandas as pd

# Initialize data storage
if "students" not in st.session_state:
    st.session_state["students"] = []
if "teachers" not in st.session_state:
    st.session_state["teachers"] = []
if "subjects" not in st.session_state:
    st.session_state["subjects"] = []

# Sidebar for navigation
st.sidebar.title("School Management System")
menu = st.sidebar.selectbox("Select Option", ["Add Student", "Add Teacher", "Add Subject", "View Students", "View Teachers", "View Subjects"])

# Add Student
if menu == "Add Student":
    st.title("Add New Student")
    student_name = st.text_input("Student Name")
    student_age = st.number_input("Age", min_value=3, max_value=18, step=1)
    student_class = st.selectbox("Class", ["1st Grade", "2nd Grade", "3rd Grade", "4th Grade", "5th Grade", "6th Grade"])
    
    if st.button("Add Student"):
        st.session_state["students"].append({
            "Name": student_name,
            "Age": student_age,
            "Class": student_class
        })
        st.success(f"Student {student_name} added successfully!")

# Add Teacher
elif menu == "Add Teacher":
    st.title("Add New Teacher")
    teacher_name = st.text_input("Teacher Name")
    teacher_subject = st.text_input("Subject Specialty")
    
    if st.button("Add Teacher"):
        st.session_state["teachers"].append({
            "Name": teacher_name,
            "Subject Specialty": teacher_subject
        })
        st.success(f"Teacher {teacher_name} added successfully!")

# Add Subject
elif menu == "Add Subject":
    st.title("Add New Subject")
    subject_name = st.text_input("Subject Name")
    subject_teacher = st.selectbox("Assign Teacher", [teacher["Name"] for teacher in st.session_state["teachers"]])
    
    if st.button("Add Subject"):
        st.session_state["subjects"].append({
            "Subject": subject_name,
            "Assigned Teacher": subject_teacher
        })
        st.success(f"Subject {subject_name} assigned to {subject_teacher}")

# View Students
elif menu == "View Students":
    st.title("Student List")
    if len(st.session_state["students"]) == 0:
        st.write("No students have been added.")
    else:
        st.table(pd.DataFrame(st.session_state["students"]))

# View Teachers
elif menu == "View Teachers":
    st.title("Teacher List")
    if len(st.session_state["teachers"]) == 0:
        st.write("No teachers have been added.")
    else:
        st.table(pd.DataFrame(st.session_state["teachers"]))

# View Subjects
elif menu == "View Subjects":
    st.title("Subject List")
    if len(st.session_state["subjects"]) == 0:
        st.write("No subjects have been added.")
    else:
        st.table(pd.DataFrame(st.session_state["subjects"]))

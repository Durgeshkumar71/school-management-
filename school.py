import streamlit as st
import pandas as pd
import os

# Set up directory to store uploaded data if it doesn't exist
if not os.path.exists("school_data"):
    os.makedirs("school_data")

# Title of the app
st.title("School Management System")

# Options for managing the school system
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose an action", ["Upload Class Data", "View Class Data", "Delete Class Data"])

# Function to save uploaded file to a class-specific directory
def save_file(uploaded_file, class_name):
    class_folder = os.path.join("school_data", class_name)
    if not os.path.exists(class_folder):
        os.makedirs(class_folder)
    file_path = os.path.join(class_folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' saved for {class_name}.")

# Upload Class Data
if option == "Upload Class Data":
    st.subheader("Upload Class Data")
    class_name = st.text_input("Enter Class Name (e.g., Grade 1, Grade 2):")
    uploaded_file = st.file_uploader("Upload a CSV file with class data", type=["csv"])
    
    if uploaded_file and class_name:
        save_file(uploaded_file, class_name)

# View Class Data
elif option == "View Class Data":
    st.subheader("View Class Data")
    classes = [folder for folder in os.listdir("school_data") if os.path.isdir(os.path.join("school_data", folder))]
    
    if classes:
        selected_class = st.selectbox("Select a Class", classes)
        class_folder = os.path.join("school_data", selected_class)
        class_files = [f for f in os.listdir(class_folder) if os.path.isfile(os.path.join(class_folder, f))]
        
        if class_files:
            selected_file = st.selectbox("Select a File", class_files)
            file_path = os.path.join(class_folder, selected_file)
            data = pd.read_csv(file_path)
            st.write(f"Displaying data for {selected_class} - {selected_file}")
            st.dataframe(data)
        else:
            st.write("No files found for this class.")
    else:
        st.write("No classes found. Please upload class data first.")

# Delete Class Data
elif option == "Delete Class Data":
    st.subheader("Delete Class Data")
    classes = [folder for folder in os.listdir("school_data") if os.path.isdir(os.path.join("school_data", folder))]
    
    if classes:
        selected_class = st.selectbox("Select a Class to Delete Data", classes)
        class_folder = os.path.join("school_data", selected_class)
        
        if st.button("Delete Class Data"):
            for file in os.listdir(class_folder):
                file_path = os.path.join(class_folder, file)
                os.remove(file_path)
            os.rmdir(class_folder)
            st.success(f"Data for {selected_class} has been deleted.")
    else:
        st.write("No classes found.")
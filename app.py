# =============================================
# 🎓 Streamlit App: GPA & CGPA Calculator (4 Semesters)
# =============================================

import streamlit as st
import pandas as pd

# -----------------------------
# App Configuration
# -----------------------------
st.set_page_config(page_title="GPA & CGPA Calculator", layout="wide")

# -----------------------------
# Header
# -----------------------------
st.title("🎓 GPA & CGPA Calculator (First 4 Semesters)")
st.write("Input your marks and get your GPA per semester and overall CGPA.")

# -----------------------------
# Function to calculate GPA
# -----------------------------
def calculate_gpa(marks):
    """Assuming GPA scale out of 4"""
    gpa_list = []
    for mark in marks:
        if mark >= 85:
            gpa_list.append(4.0)
        elif mark >= 80:
            gpa_list.append(3.7)
        elif mark >= 75:
            gpa_list.append(3.3)
        elif mark >= 70:
            gpa_list.append(3.0)
        elif mark >= 65:
            gpa_list.append(2.7)
        elif mark >= 60:
            gpa_list.append(2.3)
        elif mark >= 55:
            gpa_list.append(2.0)
        elif mark >= 50:
            gpa_list.append(1.7)
        elif mark >= 45:
            gpa_list.append(1.0)
        else:
            gpa_list.append(0.0)
    return round(sum(gpa_list)/len(gpa_list), 2)

# -----------------------------
# Tabs for Semesters
# -----------------------------
tabs = st.tabs(["Semester 1", "Semester 2", "Semester 3", "Semester 4"])

semester_gpas = []

for i, tab in enumerate(tabs):
    with tab:
        st.subheader(f"Semester {i+1}")
        num_courses = st.number_input(f"Enter number of courses in Semester {i+1}", min_value=1, step=1, key=f"num_{i}")
        marks = []
        for j in range(int(num_courses)):
            mark = st.number_input(f"Enter marks for course {j+1} (0-100)", min_value=0, max_value=100, key=f"{i}_{j}")
            marks.append(mark)
        
        if st.button(f"Calculate GPA for Semester {i+1}", key=f"btn_{i}"):
            gpa = calculate_gpa(marks)
            semester_gpas.append(gpa)
            st.success(f"✅ GPA for Semester {i+1}: {gpa}")

# -----------------------------
# CGPA Calculation
# -----------------------------
if len(semester_gpas) == 4:
    cgpa = round(sum(semester_gpas)/4, 2)
    st.balloons()
    st.header(f"🎉 Your CGPA till 4th Semester: {cgpa}")

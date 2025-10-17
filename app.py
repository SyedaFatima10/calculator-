# =============================================
# 🎓 Streamlit App: GPA & CGPA Calculator (4 Semesters)
# =============================================

import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="GPA & CGPA Calculator", layout="wide")

# -----------------------------
# App Header
# -----------------------------
st.title("🎓 GPA & CGPA Calculator (First 4 Semesters)")

# -----------------------------
# Function to calculate GPA
# -----------------------------
def calculate_gpa(marks):
    # Assuming GPA scale: 90-100:4, 80-89:3.5, 70-79:3, 60-69:2.5, 50-59:2, <50:0
    gpa_points = []
    for mark in marks:
        if mark >= 90:
            gpa_points.append(4.0)
        elif mark >= 80:
            gpa_points.append(3.5)
        elif mark >= 70:
            gpa_points.append(3.0)
        elif mark >= 60:
            gpa_points.append(2.5)
        elif mark >= 50:
            gpa_points.append(2.0)
        else:
            gpa_points.append(0)
    return round(sum(gpa_points)/len(gpa_points), 2)

# -----------------------------
# Sidebar for number of courses
# -----------------------------
st.sidebar.header("📚 Number of Courses per Semester")
num_courses = {}
for sem in range(1, 5):
    num_courses[sem] = st.sidebar.number_input(f"Semester {sem}", min_value=1, max_value=10, value=5, step=1)

# -----------------------------
# Tabs for each semester
# -----------------------------
tabs = st.tabs([f"Semester {i}" for i in range(1, 5)])
semester_marks = {}

for i, tab in enumerate(tabs):
    sem = i + 1
    with tab:
        st.subheader(f"Enter marks for Semester {sem}")
        marks = []
        for j in range(1, num_courses[sem]+1):
            mark = st.number_input(f"Subject {j}", min_value=0, max_value=100, value=0)
            marks.append(mark)
        semester_marks[sem] = marks

# -----------------------------
# Calculate GPA and CGPA
# -----------------------------
if st.button("Calculate GPA & CGPA"):
    gpa_list = []
    st.subheader("📊 GPA for Each Semester")
    for sem in range(1, 5):
        gpa = calculate_gpa(semester_marks[sem])
        gpa_list.append(gpa)
        st.write(f"Semester {sem} GPA: {gpa}")

    cgpa = round(sum(gpa_list)/len(gpa_list), 2)
    st.subheader(f"🎯 Overall CGPA: {cgpa}")

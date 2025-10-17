# =============================================
# 🎓 Streamlit App: GPA & CGPA Calculator
# =============================================

import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="GPA & CGPA Calculator", layout="wide")

# -----------------------------
# Tabs: Courses & Marks
# -----------------------------
tab1, tab2 = st.tabs(["📚 Number of Courses", "📝 Enter Marks"])

# Dictionary to store number of courses per semester
num_courses = {}

# -----------------------------
# Tab 1: Input Number of Courses
# -----------------------------
with tab1:
    st.header("Enter the number of courses for each semester")
    for sem in range(1, 5):
        num_courses[f"Semester {sem}"] = st.number_input(
            f"Number of courses in Semester {sem}", min_value=1, step=1, value=1
        )

# Dictionary to store marks
marks = {}

# -----------------------------
# Tab 2: Input Marks and Calculate GPA
# -----------------------------
with tab2:
    st.header("Enter marks for each course")

    if not num_courses:
        st.warning("Please enter the number of courses in Tab 1 first!")
    else:
        for sem in range(1, 5):
            st.subheader(f"Semester {sem}")
            marks[f"Semester {sem}"] = []
            for course in range(1, num_courses[f"Semester {sem}"] + 1):
                mark = st.number_input(
                    f"Semester {sem} - Course {course} Marks",
                    min_value=0,
                    max_value=100,
                    step=1,
                    key=f"sem{sem}_course{course}"
                )
                marks[f"Semester {sem}"].append(mark)

        # -----------------------------
        # GPA Calculation Function
        # -----------------------------
        def calculate_gpa(marks_list):
            # Simple GPA scale:
            # 90-100 -> 4.0, 80-89 -> 3.5, 70-79 -> 3.0, 60-69 -> 2.5, 50-59 -> 2.0, <50 -> 0
            gpa_points = []
            for mark in marks_list:
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
            return sum(gpa_points) / len(gpa_points)

        # -----------------------------
        # Calculate Semester GPAs
        # -----------------------------
        semester_gpas = {}
        for sem in range(1, 5):
            semester_gpas[f"Semester {sem}"] = calculate_gpa(marks[f"Semester {sem}"])

        # -----------------------------
        # Calculate CGPA
        # -----------------------------
        cgpa = sum(semester_gpas.values()) / 4

        # -----------------------------
        # Display Results
        # -----------------------------
        st.header("📊 GPA & CGPA Results")
        for sem in range(1, 5):
            st.write(f"**Semester {sem} GPA:** {semester_gpas[f'Semester {sem}']:.2f}")
        st.write(f"**CGPA (First 4 Semesters):** {cgpa:.2f}")

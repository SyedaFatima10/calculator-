import streamlit as st
import pandas as pd

# ------------------------- #
# Streamlit Page Settings
# ------------------------- #
st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

st.title("🎓 GPA & CGPA Calculator (First 4 Semesters)")
st.write("Enter your course details for each semester to calculate GPA and CGPA.")

# ------------------------- #
# Helper Function: Grade Conversion
# ------------------------- #
def grade_from_marks(marks):
    if marks >= 85:
        return "A+", 4.00
    elif marks >= 80:
        return "A-", 3.66
    elif marks >= 75:
        return "B+", 3.33
    elif marks >= 70:
        return "B", 3.00
    elif marks >= 65:
        return "B-", 2.66
    elif marks >= 60:
        return "C+", 2.33
    elif marks >= 55:
        return "C", 2.00
    elif marks >= 50:
        return "D", 1.66
    else:
        return "F", 0.00

# ------------------------- #
# Tabs for 4 Semesters
# ------------------------- #
semester_tabs = st.tabs(["Semester 1", "Semester 2", "Semester 3", "Semester 4"])
all_semester_gpas = []
all_semester_data = []

for sem_index, sem_tab in enumerate(semester_tabs, start=1):
    with sem_tab:
        st.header(f"Semester {sem_index} Courses")
        n = st.number_input(f"How many courses did you take in Semester {sem_index}?", 
                            min_value=1, max_value=10, value=5, key=f"n_{sem_index}")
        
        course_data = []

        for i in range(1, n + 1):
            st.subheader(f"Course {i}")
            course_code = st.text_input(f"Course Code (e.g., CSC101)", key=f"code_{sem_index}_{i}")
            course_name = st.text_input(f"Course Title", key=f"name_{sem_index}_{i}")
            credit = st.number_input(f"Credit Hours", min_value=1, max_value=4, key=f"credit_{sem_index}_{i}")
            marks = st.number_input(f"Marks (0–100)", min_value=0, max_value=100, key=f"marks_{sem_index}_{i}")

            grade, gp = grade_from_marks(marks)
            course_data.append({
                "Course No": course_code,
                "Course Title": course_name,
                "Credit": credit,
                "Marks": marks,
                "L.G.": grade,
                "G.P.": gp
            })

        df_sem = pd.DataFrame(course_data)
        all_semester_data.append(df_sem)

        if st.button(f"Calculate GPA Semester {sem_index}", key=f"btn_{sem_index}"):
            if not df_sem.empty:
                df_sem["Total Points"] = df_sem["Credit"] * df_sem["G.P."]
                total_credits = df_sem["Credit"].sum()
                total_points = df_sem["Total Points"].sum()
                gpa = round(total_points / total_credits, 2)
                all_semester_gpas.append((sem_index, gpa))
                
                st.success(f"📊 GPA for Semester {sem_index}: {gpa}")
                st.write("### Semester Summary")
                st.dataframe(df_sem[["Course No", "Course Title", "Credit", "Marks", "L.G.", "G.P."]],
                             use_container_width=True)
            else:
                st.warning("Please fill in your course details first!")

# ------------------------- #
# Overall CGPA
# ------------------------- #
if len(all_semester_gpas) == 4:
    cgpa = round(sum([g[1] for g in all_semester_gpas])/4, 2)
    st.balloons()
    st.header(f"🎓 Your Overall CGPA (1st to 4th Semester): {cgpa}")

# ------------------------- #
# Display All Courses Entered
# ------------------------- #
st.header("📚 All Courses Entered Across Semesters")
for sem_index, df_sem in enumerate(all_semester_data, start=1):
    if not df_sem.empty:
        st.subheader(f"Semester {sem_index}")
        st.dataframe(df_sem[["Course No", "Course Title", "Credit", "Marks", "L.G.", "G.P."]],
                     use_container_width=True)

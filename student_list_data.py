# ----------------------------------------------------
# Student Marks Processing Program
# ----------------------------------------------------

# Sample student list
students = [
    {"name": "Motu", "maths": 78, "vlsi": 85, "python": 89},
    {"name": "Kiran", "maths": 88, "vlsi": 90, "python": 80},
    {"name": "Manu",  "maths": 92, "vlsi": 79, "python": 95},
    {"name": "Deepak",  "maths": 65, "vlsi": 70, "python": 60},
    {"name": "Abhi",  "maths": 95, "vlsi": 98, "python": 85}
]

# 1. Function to calculate total marks
def calculate_total(student):
    return student["maths"] + student["vlsi"] + student["python"]

# 2. Add 'total' key for each student
for s in students:
    s["total"] = calculate_total(s)

# 3. Sort students in descending order of total marks
students_sorted = sorted(students, key=lambda x: x["total"], reverse=True)

# Topper and lowest performer
topper = students_sorted[0]
lowest = students_sorted[-1]

# 4. Subject-wise highest scorers
highest_maths = max(students, key=lambda x: x["maths"])
highest_vlsi = max(students, key=lambda x: x["vlsi"])
highest_python = max(students, key=lambda x: x["python"])

# 5. Save report to text file
with open("student_report.txt", "w") as f:
    f.write("===== STUDENT PERFORMANCE REPORT =====\n\n")
    
    f.write("---- Sorted Student List (Highest to Lowest Total) ----\n")
    for s in students_sorted:
        f.write(f"{s['name']} | Maths: {s['maths']} | VLSI: {s['vlsi']} | Python: {s['python']} | Total: {s['total']}\n")
    
    f.write("\n---- Top Performer ----\n")
    f.write(f"{topper['name']} with {topper['total']} marks\n")
    
    f.write("\n---- Lowest Performer ----\n")
    f.write(f"{lowest['name']} with {lowest['total']} marks\n")
    
    f.write("\n---- Subject-wise Highest Scorers ----\n")
    f.write(f"Maths   : {highest_maths['name']} ({highest_maths['maths']})\n")
    f.write(f"VLSI    : {highest_vlsi['name']} ({highest_vlsi['vlsi']})\n")
    f.write(f"Python  : {highest_python['name']} ({highest_python['python']})\n")

print("Report generated successfully as 'student_report.txt'")

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
from datetime import datetime

# Load data
df = pd.read_csv("data.csv")

# Calculate Total and Average
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Assign Grades
def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(assign_grade)

# Plot Average Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Average"], color="green")
plt.title("Student Average Scores")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("chart.png")
plt.close()

# Create PDF
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Student Performance Report", ln=True, align="C")

pdf.ln(10)

# Date
pdf.set_font("Arial", size=10)
pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}", ln=True)
pdf.ln(5)

# Table Header
pdf.set_font("Arial", "B", 12)
columns = ["Name", "Maths", "Science", "English", "Total", "Average", "Grade"]
col_widths = [30, 20, 20, 20, 20, 25, 20]

for i, col in enumerate(columns):
    pdf.cell(col_widths[i], 10, col, 1, 0, 'C')
pdf.ln()

# Table Data
pdf.set_font("Arial", size=12)
for index, row in df.iterrows():
    pdf.cell(col_widths[0], 10, row["Name"], 1)
    pdf.cell(col_widths[1], 10, str(row["Maths"]), 1)
    pdf.cell(col_widths[2], 10, str(row["Science"]), 1)
    pdf.cell(col_widths[3], 10, str(row["English"]), 1)
    pdf.cell(col_widths[4], 10, str(row["Total"]), 1)
    pdf.cell(col_widths[5], 10, f"{row['Average']:.2f}", 1)
    pdf.cell(col_widths[6], 10, row["Grade"], 1)
    pdf.ln()

# Insert Chart
pdf.ln(5)
pdf.image("chart.png", x=30, w=150)

# Save PDF
filename = f"student_report_{datetime.now().strftime('%d%m%Y_%H%M%S')}.pdf"
pdf.output(filename)

# Clean up
os.remove("chart.png")

print(f"✅ Report generated with grades: {filename}")

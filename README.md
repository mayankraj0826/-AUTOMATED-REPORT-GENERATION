# -AUTOMATED-REPORT-GENERATION

COMPANY : CODTECH IT SOLUTIONS

NAME : MAYANK RAJ

INTERN ID :CT06DF1345

DOMAIN : PYTHON PROGRAMMING

DURATION : 6 WEEKS

MENTOR : NEELA SANTOSH


# 📘 Automated Student Performance Report Generator

## 📝 Project Overview

**Automated Student Performance Report Generator** is a Python-based project that reads student marks from a CSV file, calculates total and average, assigns grades, generates a performance chart, and exports a clean and structured PDF report. This tool is designed to automate the traditionally manual process of preparing student report cards, saving time and reducing errors.

The report includes:

* A structured marks table
* Total and average for each student
* Assigned grade based on performance
* A bar chart of average scores

---

## 🎯 Key Features

* ✅ Reads student data from a CSV file
* ✅ Calculates total and average marks
* ✅ Automatically assigns grades (A, B, C, F)
* ✅ Generates a bar chart using `matplotlib`
* ✅ Creates a formatted PDF report using `FPDF`
* ✅ Cleans up temporary files after generation
* ✅ Fully automated and error-handled

---

## 🔧 Tools & Libraries Used

| Tool/Library   | Purpose                        |
| -------------- | ------------------------------ |
| **Python 3.x** | Programming Language           |
| **pandas**     | Read and process CSV data      |
| **matplotlib** | Create bar chart visualization |
| **fpdf**       | Generate PDF reports           |
| **os**         | File handling and cleanup      |
| **datetime**   | Timestamping PDF output        |

> Install all dependencies using:

```bash
pip install pandas matplotlib fpdf
```

---

## 🛠️ How It Works

1. The user provides a `data.csv` file with student names and marks.
2. Python script reads the file using `pandas`.
3. Calculates:

   * Total marks
   * Average marks
   * Grade using custom logic:

     * A: 85 and above
     * B: 70–84
     * C: 50–69
     * F: Below 50
4. Generates a bar chart of student averages using `matplotlib`.
5. Compiles everything into a structured PDF using `FPDF`.
6. Deletes temporary chart image after PDF is created.

---

## 📁 Folder Structure

```
Student-Report-Generator/
│
├── data.csv                # Input marks data
├── generate_report.py      # Main Python script
├── chart.png               # (Temporary chart image)
├── student_report_*.pdf    # Final generated PDF
└── README.md               # Project documentation
```

---

## 📄 Sample `data.csv`

```
Name,Maths,Science,English
Alice,85,90,88
Bob,70,75,80
Charlie,95,92,94
David,60,65,70
Esha,40,45,35
```

---

## 📌 Applications

* For schools and colleges to generate report cards
* Educational dashboards and analytics
* Internal performance monitoring
* Demo project for Python beginners

---

## 🚀 Future Improvements

* Add email delivery of report cards
* GUI interface using Tkinter
* Subject-wise toppers
* Custom grading scale per school
* Export in Word/Excel format

---

## 🙌 Author

**Mayank**


> This project was built as part of a learning goal to automate real-world reporting using Python. Ready for GitHub and project submissions.

---



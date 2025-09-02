import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ================================
# 1. Load Dataset
# ================================
print("📂 Loading dataset...")
df = pd.read_csv("../data/employee_data.csv")

# ================================
# 2. Normalize Column Names
# ================================
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ================================
# 3. Data Cleaning
# ================================
print("🧹 Cleaning data...")

# Fill missing salary with mean
if "salary" in df.columns:
    df["salary"] = df["salary"].fillna(df["salary"].mean())

# Fill missing Employee IDs (forward fill)
if "employeeid" in df.columns:
    df["employeeid"] = df["employeeid"].fillna(method="ffill")

# Drop duplicates
df = df.drop_duplicates()

# Standardize Department and Job Titles
if "department" in df.columns:
    df["department"] = df["department"].str.strip().str.title()

    # Mapping for inconsistent names
    dept_mapping = {
        "It": "IT",
        "I.T.": "IT",
        "Information Technology": "IT",
        "Hr": "HR",
        "Human Resources": "HR"
    }
    df["department"] = df["department"].replace(dept_mapping)

if "job_title" in df.columns:
    df["job_title"] = df["job_title"].str.strip().str.title()

# ================================
# 4. Aggregations
# ================================
print("📊 Performing aggregations...")

avg_salary_dept = (
    df.groupby("department")["salary"].mean()
    if "department" in df.columns and "salary" in df.columns else None
)
employee_count = (
    df["department"].value_counts()
    if "department" in df.columns else None
)
avg_salary_job = (
    df.groupby("job_title")["salary"].mean()
    if "job_title" in df.columns and "salary" in df.columns else None
)

# Summary statistics
summary = df.describe(include="all")

# ================================
# 5. Reports
# ================================
print("📑 Exporting reports...")

os.makedirs("../outputs/charts", exist_ok=True)

df.to_csv("../data/cleaned_employee_data.csv", index=False)
summary.to_csv("../outputs/summary_statistics.csv")

if avg_salary_dept is not None:
    avg_salary_dept.to_csv("../outputs/avg_salary_by_dept.csv")

if employee_count is not None:
    employee_count.to_csv("../outputs/employee_count_by_dept.csv")

if avg_salary_job is not None:
    avg_salary_job.to_csv("../outputs/avg_salary_by_job.csv")

# Top 10 salaries (highest/lowest)
if "salary" in df.columns:
    df.nlargest(10, "salary").to_csv("../outputs/top_10_highest_salaries.csv", index=False)
    df.nsmallest(10, "salary").to_csv("../outputs/top_10_lowest_salaries.csv", index=False)

# ================================
# 6. Charts
# ================================
print("📈 Generating charts...")

if avg_salary_dept is not None:
    plt.figure(figsize=(8, 5))
    avg_salary_dept.plot(kind="bar", color="skyblue", title="Average Salary per Department")
    plt.ylabel("Average Salary")
    plt.tight_layout()
    plt.savefig("../outputs/charts/avg_salary_dept.png")
    plt.close()

if employee_count is not None:
    plt.figure(figsize=(8, 5))
    employee_count.plot(kind="bar", color="orange", title="Employee Count per Department")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("../outputs/charts/employee_count.png")
    plt.close()

if avg_salary_job is not None:
    plt.figure(figsize=(10, 6))
    avg_salary_job.sort_values().plot(kind="barh", color="green", title="Average Salary per Job Title")
    plt.xlabel("Average Salary")
    plt.tight_layout()
    plt.savefig("../outputs/charts/avg_salary_job.png")
    plt.close()

# ================================
# 7. Done
# ================================
print("✅ Data cleaning and reporting completed!")
print("   - Cleaned data: ../data/cleaned_employee_data.csv")
print("   - Reports: ../outputs/")
print("   - Charts: ../outputs/charts/")


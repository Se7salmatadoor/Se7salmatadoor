import os
import re

def extract_cv_data():
    # بيانات احترافية ديناميكية خاصة بحسين عبد الله
    name = "Hussein Abdallah"
    title = "Data Analyst & Technical Office / Document Control Specialist"
    
    skills = [
        "Power BI (Interactive Dashboards, DAX, Power Query)",
        "Advanced Excel (VLOOKUP, Pivot Tables, Data Modeling)",
        "SQL (Data Extraction, Query Optimization)",
        "Process Automation (Power Automate, GitHub Actions)",
        "Domain Tools (Aconex, Engineering Logs, EDMS)"
    ]
    
    experience = [
        {"role": "Technical Office & Document Control", "company": "EDECS", "duration": "Present"},
        {"role": "Data Analyst & HR Analytics Specialist", "company": "Professional Experience", "duration": "2025-2026"}
    ]
    
    readme_content = f"""# 📊 Welcome to My Dynamic Engineering Portfolio

## 👤 Profile
* **Name:** {name}
* **Role:** {title}

---

## 🛠️ Automatically Extracted Technical Skills
This section is automatically updated whenever a new CV is uploaded using Python & GitHub Actions!

"""
    for skill in skills:
        readme_content += f"- ✅ {skill}\n"
        
    readme_content += "\n--- \n## 📁 Professional Experience\n"
    for exp in experience:
        readme_content += f"* **{exp['role']}** at *{exp['company']}* ({exp['duration']})\n"
        
    readme_content += """
---
## 📬 Connect With Me
* **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/hussein-abdallah-tolba-b5676318a)
* **Email:** [hussaintolba2@gmail.com](mailto:hussaintolba2@gmail.com)
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("README.md updated successfully via Automation!")

if __name__ == "__main__":
    extract_cv_data()


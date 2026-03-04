
import streamlit as st
import pandas as pd
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).parent
image_path = BASE_DIR / "IMAGES" / "logo.png"

st.sidebar.image(image_path, width=100)
st.set_page_config(page_title="Career Analyzer", page_icon="🚀")

st.sidebar.text("CAREER ANALYZER")
with st.sidebar.expander("""Career Options:
"""):
    st.write("""1. AIML Engineer
                 """)
    st.write("""
                2. Data Sceintist
                 """)
    st.write("""
                3. Data Analyst
               """)
    st.write("""
                4. Full Stack Web Developer
                """)
    st.write("""
                5. Blockchain Security Engineer """)
    
st.title("   AI Career Readiness Analyzer")
st.markdown("### Analyze your readiness for your dream tech domain")


career_map = {
    "AI": {
        "skills": ["PYTHON", "LINEAR ALGEBRA", "PROBABILITY"],
        "weight": 1.3
    },
    "ML": {
        "skills": ["PYTHON", "LINEAR ALGEBRA", "PROBABILITY"],
        "weight": 1.3
    },
    "DATA VISUALIZATION": {
        "skills": ["POWERBI/TABLEAU", "SQL"],
        "weight": 1.1
    },
    "WEB DEVELOPMENT": {
        "skills": ["HTML", "CSS", "JAVASCRIPT", "SQL"],
        "weight": 1.0
    },
    "CYBERSECURITY": {
        "skills": ["NETWORKING", "LINUX", "PYTHON", "CRYPTOGRAPHY"],
        "weight": 1.2
    },
    "DEVOPS": {
        "skills": ["LINUX", "DOCKER", "KUBERNETES", "AWS"],
        "weight": 1.25
    },
    "BLOCKCHAIN": {
        "skills": ["CRYPTOGRAPHY", "PYTHON", "DATA STRUCTURES"],
        "weight": 1.15
    }
}


st.subheader("🛠 Select Your Skills")

skills = st.multiselect(
    "",
    ["PYTHON","SQL","HTML","CSS","JAVASCRIPT","CRYPTOGRAPHY",
     "POWERBI/TABLEAU","CALCULUS","LINEAR ALGEBRA","PROBABILITY",
     "NETWORKING","LINUX","DOCKER","KUBERNETES","AWS","GIT",
     "DATA STRUCTURES","CI/CD","AUTOMATION"]
)

st.subheader("GPA")
GPA = st.number_input("", min_value=0.0, max_value=10.0)

st.subheader("Number of Projects")
project_count = st.slider("", 0, 15)

st.subheader("Internship Experience")
intern = st.radio("", ["NO", "YES"])

st.subheader("Interested Domain")
interested_domain = st.selectbox("", list(career_map.keys()))

def calculate_score():
    score = 0
    
    # GPA Score (30%)
    score += (GPA / 10) * 30
    
    # Projects Score (20%)
    score += min(project_count * 2, 20)
    
    
    if intern == "YES":
        score += 10
  
    required_skills = career_map[interested_domain]["skills"]
    weight = career_map[interested_domain]["weight"]
    
    matched = [s for s in skills if s in required_skills]
    skill_score = (len(matched) / len(required_skills)) * 40 * weight
    
    score += skill_score
    
    final_score = min(round(score, 2), 100)
    
    return final_score, matched, required_skills


if st.button("Analyze My Profile "):
    
    score, matched, required = calculate_score()
    missing = list(set(required) - set(matched))
    
    st.subheader(f" Career Readiness Score: {score}%")
    st.progress(int(score))
    
    if score >= 75:
        st.success(" You are strongly prepared for this domain!")
    elif score >= 50:
        st.warning(" You are moderately prepared. Improve missing skills.")
    else:
        st.error(" You need significant improvement before targeting this domain.")
    
    # Skill Breakdown
    st.subheader(" Skill Analysis")
    st.write("Matched Skills:", matched if matched else "None")
    st.write("Missing Skills:", missing if missing else "None")
    
    # Visualization
    st.bar_chart({
        "Matched Skills": [len(matched)],
        "Missing Skills": [len(missing)]
    })
    
    # Smart Suggestions
    st.subheader("Recommendations")
    
    if missing:
        for skill in missing:
            st.write(f"->Focus on improving **{skill}**")
    
    if project_count < 3:
        st.write("->Build at least 2–3 strong domain-based projects.")
    
    if intern == "NO":
        st.write("->Try getting internship or contributing to open source.")
    
    st.write("->Participate in hackathons to increase visibility.")
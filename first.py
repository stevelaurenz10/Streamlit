import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Steve Laurenz J. Villas - Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .main-title {
            font-size: 3rem;
            font-weight: bold;
            color: #3A3B3C;
            animation: fadeIn 2s ease-in-out;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            padding: 10px;
            background-color: #2C3E50;
            color: white;
            animation: fadeIn 3s ease-in-out;
        }
        .footer a {
            color: white;
            margin: 0 10px;
        }
        .portfolio-item {
            margin: 1px;
            padding: 5px;
            background: linear-gradient(135deg, #000428, #004e92);
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
            animation: fadeIn 2s ease-in-out;
            font-size: 1.3rem;
            font-weight: bold;
            color: white;
            font-family: 'Courier New', Courier, monospace;
            transition: transform 0.3s, box-shadow 0.3s, background 0.3s;
        }
        .portfolio-item:hover {
            transform: scale(1.1);
            box-shadow: 0 12px 20px rgba(0, 0, 0, 0.3);
        }
        .image-container {
            display: flex;  
            justify-content: center;  
            align-items: center;  
            animation: fadeIn 2.5s ease-in-out;
        }
        .image-container img {
            border: 1px solid #ddd;
            border-radius: 10px;
        }
        .fade-in-section {
            animation: fadeIn 2s ease-in-out;
        }
        .education-section h3 {
            margin: 0;
            font-size: 1.2rem;
            font-weight: bold;
            color: #333;
        }
        .education-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }
        .education-item p {
            margin: 0;
        }
        .education-location, .education-date {
            text-align: right;
            color: #666;
        }
    </style>
""", unsafe_allow_html=True)

cols = st.columns([1, 2])  

with cols[0]:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    display_image = Image.open("pic.jpg") 
    st.image(display_image, caption='Steve Laurenz J. Villas', width=250)  
    st.markdown('</div>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<h1 class="main-title" id="home-section">Hello Everyone</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="fade-in-section">Welcome to my basic Streamlit application showing a simple autobiography and portfolio.</h3>', unsafe_allow_html=True)

st.markdown('<h2 id="autobiography-section" class="fade-in-section">Autobiography</h2>', unsafe_allow_html=True)
st.write("""
Hello! I'm Steve Laurenz J. Villas, a passionate 4th-year BSIT student at CIT University in Cebu, Philippines. 
I may not be an expert in this field yet, I'm always excited to learn and become better. I'm a hardworking student who is interested in 
programming and working with computer systems. I keep learning and improving as I go. I see every problem as a chance to get better.
""")

st.markdown('<h2 id="skills-section" class="fade-in-section">Skills</h2>', unsafe_allow_html=True)
skills = {
    "Programming Languages": ["Java", "C", "Python", "JavaScript"],
    "System Administration": ["Basic knowledge and practical skills in system administration tasks"],
    "Web Technologies": ["HTML", "CSS", "JavaScript"]
}

cols = st.columns(len(skills))
icons = ["💻", "🛠️", "🌐"]  
for col, (skill, details), icon in zip(cols, skills.items(), icons):
    with col:
        st.markdown(f"**{icon} {skill}:**")
        st.write(", ".join(details))

st.markdown('<h2 id="portfolio-section" class="fade-in-section">Portfolio</h2>', unsafe_allow_html=True)
st.write("Here are some of the projects I've worked on with my teammates:")

portfolio_cols = st.columns(3)
with portfolio_cols[0]:
    st.markdown('<div class="portfolio-item"><a href="https://github.com/Wrecage/SocialSphere.git" target="_blank" style="color: white;">🔗 SocialSphere</a></div>', unsafe_allow_html=True)
with portfolio_cols[1]:
    st.markdown('<div class="portfolio-item"><a href="https://github.com/sc-tompar/ReflectDaily.git" target="_blank" style="color: white;">🔗 ReflectDaily</a></div>', unsafe_allow_html=True)
with portfolio_cols[2]:
    st.markdown('<div class="portfolio-item"><a href="https://github.com/stevelaurenz10/Hey.git" target="_blank" style="color: white;">🔗 Hey</a></div>', unsafe_allow_html=True)

st.markdown('<h2 id="education-section" class="fade-in-section">Education</h2>', unsafe_allow_html=True)
st.markdown('<div class="education-section">', unsafe_allow_html=True)
st.markdown("""
<div class="education-item">
    <div>
        <h3>UNIVERSITY OF SAN CARLOS – TALAMBAN CAMPUS</h3>
        <p>Senior High School - STEM</p>
    </div>
    <div class="education-location-date">
        <p class="education-location">Cebu City, Philippines</p>
        <p class="education-date">2019 - 2021</p>
    </div>
</div>
<div class="education-item">
    <div>
        <h3>CEBU INSTITUTE OF TECHNOLOGY - UNIVERSITY</h3>
        <p>Bachelor of Science in Information Technology</p>
    </div>
    <div class="education-location-date">
        <p class="education-location">Cebu City, Philippines</p>
        <p class="education-date">Present</p>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h2 id="certifications-section" class="fade-in-section">Certifications</h2>', unsafe_allow_html=True)
st.write("""
- Kaggle – Data Visualization Online Course
- Alison – Data Analytics Online Course
- Huawei Online – HCIP Storage Expert Course
- Cebu ICT Student Congress 2024
""")

st.markdown('<h2 id="quote-section" class="fade-in-section">Words I Live By</h2>', unsafe_allow_html=True)
st.markdown("""
<blockquote style="font-size:18px; font-style:italic; border-left: 4px solid #ddd; padding-left: 16px; color: #555;">
"Passion and dedication are the keys to success. I believe that when you truly love what you do, you can achieve great things."
</blockquote>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <p>© 2024 villaslaurenzo</p>
    <p>
        <a href="https://www.facebook.com/Stevelaurenz11" target="_blank">Facebook</a> | 
        <a href="https://github.com/stevelaurenz10" target="_blank">GitHub</a> | 
        <a href="mailto:stevelaurenzvillas@gmail.com">Email</a>
    </p>
</div>
""", unsafe_allow_html=True)

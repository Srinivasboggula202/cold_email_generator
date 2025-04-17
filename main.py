import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Set page config FIRST
st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="✉️")

# Custom CSS for animations and styling
st.markdown("""
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .fadeIn {
        animation: fadeIn 1.5s ease-in-out;
    }
    .stRadio > div {
        display: flex;
        justify-content: space-between;
        gap: 20px;
    }
    .stRadio > div > label {
        flex: 1;
        text-align: center;
        padding: 20px;
        border: 2px solid #4CAF50;
        border-radius: 10px;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.3s;
    }
    .stRadio > div > label:hover {
        background-color: #4CAF50;
        color: white;
        transform: scale(1.05);
    }
    .stRadio > div > label[data-baseweb="radio"] {
        margin: 0;
    }
    .stButton > button {
        width: 100%;
        padding: 10px;
        font-size: 16px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stTextInput > div > input, .stTextArea > div > textarea {
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    .stMarkdown > div > pre {
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
    }
    </style>
    """, unsafe_allow_html=True)

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("🚀 Cold Email Generator")
    st.markdown("<div class='fadeIn'>", unsafe_allow_html=True)
    
    # Side-by-side radio buttons for input type
    input_type = st.radio(
        "Choose how you want to generate the email:",
        ("Generate Email by URL", "Generate Email by Text"),
        horizontal=True
    )
    
    if input_type == "Generate Email by URL":
        st.markdown("### 🌐 Enter Job Posting URL")
        url_input = st.text_input("Paste the URL here:")
        submit_button = st.button("Generate Email")
        
        if submit_button:
            try: 
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(data)
                
                for job in jobs:
                    skills = job.get("skills", [])
                    portfolio_urls = portfolio.query_links(skills)
                    email = llm.write_email(job, portfolio_urls)
                    st.markdown("### ✉️ Generated Email")
                    st.code(email, language="markdown")

            except Exception as e:
                st.error(f"❌ An Error Occurred: {e}")
    
    else:  # Generate Email by Text
        st.markdown("### 📝 Enter Job Description Text")
        text_input = st.text_area("Paste the job description here:")
        submit_button = st.button("Generate Email")
        
        if submit_button:
            try:
                cleaned_text = clean_text(text_input)
                portfolio.load_portfolio()
                jobs = llm.extract_jobs(cleaned_text)
                
                for job in jobs:
                    skills = job.get("skills", [])
                    portfolio_urls = portfolio.query_links(skills)
                    email = llm.write_email(job, portfolio_urls)
                    st.markdown("### ✉️ Generated Email")
                    st.code(email, language="markdown")

            except Exception as e:
                st.error(f"❌ An Error Occurred: {e}")
    
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio(file_path = "./sample_portfolio.csv")
    create_streamlit_app(chain, portfolio, clean_text)
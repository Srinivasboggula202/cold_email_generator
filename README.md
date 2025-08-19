# 💼 Cold Email Generator for Services Companies

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Langchain](https://img.shields.io/badge/Langchain-00BFFF?style=flat&logo=OpenAI&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-228B22?style=flat)
![LLaMA 3.1](https://img.shields.io/badge/LLaMA-3.1-blueviolet)

> An AI-powered web application that automates the creation of cold emails for services companies using advanced LLM technology.

---

## 🚀 Project Overview

Cold Email Generator is a smart and efficient tool that helps service-based companies craft personalized and professional cold emails in seconds. Built with LLaMA 3.1, Langchain, ChromaDB, and Streamlit, this app demonstrates the potential of Generative AI and vector databases in real-world business communication.

This project was designed to showcase modern AI applications for outreach and sales, and reflects strong backend development, prompt engineering, and deployment skills.

---

## 🎯 Key Features

- ✉️ Generate personalized cold emails with just a few inputs
- ⚙️ Uses **LLaMA 3.1** to produce high-quality content
- 🧠 Employs **Langchain** for chaining prompts and maintaining conversation flow
- 📚 Integrates **ChromaDB** for storing and retrieving context using vector embeddings
- 🖥️ Built with **Streamlit** to deliver a simple and intuitive web interface
- 🔁 Dynamic, fast, and relevant cold email generation

---

## 🧑‍💻 Technologies Used

|  Technology | Purpose                                     |
| ------------|---------------------------------------------|
|  Python     | Core backend logic                              |
|  LLaMA 3.1  | Large Language Model for email content          |
|  Langchain  | Prompt chaining and LLM management              |
|  ChromaDB   | Vector database for context-based retrieval     |
|  Streamlit  | User-friendly frontend interface                |

---

## 📸 Screenshots

<img width="1834" height="879" alt="Screenshot 2025-08-19 114757" src="https://github.com/user-attachments/assets/dd3bd844-c722-4a6b-89f4-bf1e2ba70f5d" />

## sample email for python developer position
{
Subject: Experienced Python Developer for Collaboration Opportunities

Dear Hiring Manager,

I am reaching out to introduce myself as a seasoned Python Developer with 4 years of experience in crafting innovative solutions using Python. With a strong foundation in programming principles and a passion for delivering high-quality code, I am confident in my ability to make a valuable contribution to your team.

Throughout my career, I have developed a solid expertise in Python, with a proven track record of successfully completing projects that showcase my skills. I would like to invite you to explore my portfolio, which includes:

* https://github.com/user/project2
* https://github.com/user/project1

These projects demonstrate my proficiency in Python and my ability to design, develop, and deploy efficient solutions.

I am excited about the opportunity to discuss how my skills and experience align with your needs. If you are looking for a dedicated and skilled Python Developer to collaborate on upcoming projects, I would welcome the chance to explore this further.

Please do not hesitate to contact me to arrange a discussion at your convenience. I look forward to the opportunity to contribute my expertise and learn more about your team's work.

Best regards,
[Your Name]

}


## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/Srinivasboggula202/cold-email-generator.git
cd cold-email-generator

# Create and activate virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

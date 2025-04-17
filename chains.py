import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

# load_env()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
                        model="llama-3.3-70b-versatile",
                        temperature=0,
                        max_tokens=None,
                        timeout=None,
                        max_retries=2)
    
    
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template("""
                I will give you scraped text from the job posting. 
                Your job is to extract the job details & requirements in a JSON format containing the following keys: 'role', 'experience', 'skills', and 'description'. 
                Only return valid JSON. No preamble, please.
                Here is the scraped text: {page_data}
                """)    
        
        chain_extract = prompt_extract | self.llm
        response = chain_extract.invoke(input={"page_data" : cleaned_text})
        
        try:
            json_parser = JsonOutputParser()
            response = json_parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException("Content too big, unable to parse jobs.")
        
        return response if isinstance(response, list) else [response]


    def write_email(self, job_description, portfolio_urls):
        prompt_email = PromptTemplate.from_template(
                """
               I will provide you with a job description and a list of portfolio URLs. Your task is to write a professional cold email to the hiring manager, introducing yourself and showcasing your expertise based on the job description and portfolio URLs.

        Your email should:
        1. Be concise and professional.
        2. Highlight your skills and experience relevant to the job description.
        3. Include the portfolio URLs to showcase your work.
        4. Avoid mentioning any specific consultancy or firm.
        5. End with a call to action, inviting the hiring manager to discuss further.

        JOB DESCRIPTION: {job_description}
        PORTFOLIO URLS: {portfolio_urls} 
                """)
        
        chain_email = prompt_email | self.llm
        response = chain_email.invoke({"job_description": str(job_description), "portfolio_urls": portfolio_urls})

        return response.content
        
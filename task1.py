from langchain_groq import ChatGroq
from pydantic import BaseModel,Field,EmailStr
from typing import List
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

load_dotenv()

# Model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    max_tokens= 500
)




class ResumeAnalysis(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: EmailStr = Field(description="Valid email address")
    phone: str = Field(description="Phone number of the candidate")
    skills: List[str] = Field(description="Technical and professional skills")
    project: str = Field(description="Summary of projects and contributions")
    experience: float = Field(description="Years of professional experience")


parser = PydanticOutputParser(pydantic_object=ResumeAnalysis)

prompt = PromptTemplate(
    template="""
Analyze the provided resume and extract the candidate's information.
Use only information explicitly stated in the resume.
Do not invent missing details.

Resume:
{resume}

{format_instructions}
""",
    input_variables=["resume"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = prompt | model | parser

resume = """resume


Name: Rahul Sharma

Email: rahul.sharma@example.com

Phone: +91 98765 43210

Professional Summary:
Python Developer with 2 years of experience in software
development, API integration, and AI application development.

Technical Skills:
Python, C++, SQL, LangChain, FastAPI, Streamlit,
Prompt Engineering, Git, GitHub, REST APIs.

Projects:
1. AI Resume Analyzer:
   Developed an AI-powered application to analyze resumes,
   extract candidate details, and evaluate technical skills.

2. AI Chatbot:
   Built a chatbot using Python, LangChain, and an LLM API
   to answer user queries.

Experience:
2 years of professional experience as a Python Developer.

Education:
Bachelor of Technology in Computer Science and Engineering.
"""

result : ResumeAnalysis = chain.invoke({"resume":resume})

print(result.model_dump_json(indent=4))
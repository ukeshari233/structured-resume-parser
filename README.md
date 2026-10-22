# Resume Parser with LangChain and Groq

A Python application that extracts structured candidate information from resume text using a Groq-hosted language model and Pydantic validation.

## Features

- Extract candidate name, email, and phone number.
- Identify technical and professional skills.
- Summarize projects and contributions.
- Extract years of professional experience.
- Validate the output against a Pydantic schema.
- Return structured JSON output.

## Tech Stack

- Python
- LangChain
- Groq API
- Pydantic
- python-dotenv

## Output
{
    "name": "Rahul Sharma",
    "email": "rahul.sharma@example.com",
    "phone": "+91 98765 43210",
    "skills": [
        "Python",
        "C++",
        "SQL",
        "LangChain",
        "FastAPI",
        "Streamlit",
        "Prompt Engineering",
        "Git",
        "GitHub",
        "REST APIs"
    ],
    "project": "Developed an AI-powered Resume Analyzer to extract candidate details and evaluate technical skills. Built an AI Chatbot using Python, LangChain, and an LLM API to answer user queries.",
    "experience": 2.0
}




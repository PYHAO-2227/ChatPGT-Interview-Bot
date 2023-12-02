from fastapi import FastAPI
from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_API_ORG")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


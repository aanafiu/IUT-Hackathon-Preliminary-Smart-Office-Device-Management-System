from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_BASE_URL
)

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=OPENAI_BASE_URL
)

MODEL = "qwen/qwen-2.5-7b-instruct"   # OpenRouter example
# MODEL = "llama-3.3-70b-versatile"  # Groq example


def english_support(prompt: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an experienced English Support Engineer."
                    " You are skilled in reviewing and improving English text, including"
                    " grammar, clarity, and tone. Your task is to provide constructive feedback and suggestions to enhance the quality of the text."
                    " Your responses should be clear, concise, and professional, while maintaining"
                    " a friendly professional tone."
                    "add 3 different section to answer: 1.Grammar check and correction, 2.Suggestion to make that more native, 3.How to make this prompt more professional and clear"
                    "1 section about ILTES Score and how to improve it"
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

# model initialization
model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google_genai"
)

print(model)

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    response = model.invoke(user_input)
    print(f"Model: {response.content}")
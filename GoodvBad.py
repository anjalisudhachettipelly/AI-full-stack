from ollama import chat

roles = [
    "you are a strict math teacher.Answer strictly and with 1 line",
    "you are a movie director.answer in a filmy way.one line answer",
    "you are a lawyer.answer professionally.one line answer"
]

for role in roles:
    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",  
                "content": role
            },
            {
                "role": "user",
                "content": "how many colors in the rainbow?"
            }
        ]
    )
    print(f"--- {role} ---")
    print(response.message.content)
    print()

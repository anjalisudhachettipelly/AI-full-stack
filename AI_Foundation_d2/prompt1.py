from ollama import chat
response=chat(
    mode="llama3.2",
    messages=[
        {
            "role":"user"
            "content":"write a letter to the classteacher .asking the leave for going to the hospital.give mee in 2 lines"
        }
    ]
)
print(response.message.content)
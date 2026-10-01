from ollama import chat
messages = [
    {"role" :"system","content" : "Identify sentiment as Positive,Negative,Neutral.Reply with one word only."},
    {"role" : "user","content":"Greate Movie"},
    {"role" : "system","content":"positive"},

    {"role" : "user","content":"waste of money."},
    {"role" : "system","content":"Negative"},

    {"role" : "user","content":"It is Okay."},
    {"role" : "system","content":"Neutral"},

   

    {"role" : "user","content":"Loved the acting but the ending was dull."}
]
response = chat(
    model= "llama3.2",
    messages=messages
)
print(response.message.content)
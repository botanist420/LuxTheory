import os
import openai

def generate_answer(prompt):
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        raise Exception("OpenAI API key not found in environment variables.")

    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"].strip()



answer = generate_answer(input("Please type What do you want to ask:\n"))
print(answer)
import os
import openai

# Authenticate with OpenAI

os.getenv("OPENAI_API_KEY") # Remember to export OPENAI_API_KEY="your API key here" in the terminal first. 

# Define a function to prompt the user for input and generate a response
def generate_response(prompt):
    # Call the OpenAI API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content":"This is the year 2099.I am a cyberpunk AI. Ask me anything."},{'role': 'user', 'content': prompt}],
        max_tokens=1024,
        n=1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    # Get the response text from the API response
    response_text = response['choices'][0]['message']['content']

    return response_text

# Start the conversation with the user
print("Welcome to your cybersecurity lesson with a cyberpunk AI in the year 2099! Let's begin:")

# Loop to continue the conversation until the user exits
while True:
    # Prompt the user for input
    prompt = input("Cybersecurity student: ")

    # Generate a response to the user input
    response = generate_response(prompt)

    # Print the response
    print("Cyberpunk AI:", response)

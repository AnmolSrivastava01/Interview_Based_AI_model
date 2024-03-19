import openai

# Set your correct OpenAI API key
openai.api_key = 'xxx'
# Provide the question and answer for classification
question = "What is the capital of France?"
user_answer = "Paris is the capital of France."

# Create a prompt that includes the question and the user's answer
prompt = f"Question: {question}\nAnswer: {user_answer}\nIs the answer correct or incorrect?"

# Make a request to the OpenAI API for classification using the gpt-3.5-turbo engine
response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
    prompt=prompt,
    max_tokens=50,
)

# Access the generated classification label from the API response
classification_label = response['choices'][0]['text'].strip()
score=0
# Output the classification label
if "correct" in classification_label:
    score+=1
print("Classification Label:", classification_label,score)

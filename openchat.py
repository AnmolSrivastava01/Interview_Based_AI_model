import pandas as pd
from gtts import gTTS
import os
import openai

# Function to convert text to speech
def text_to_speech(text, language='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    os.system(f'start {filename}')  # This command works on Windows. For other OS, you might need to adjust it.

if __name__ == "__main__":
    # Replace 'project.xlsx' with your actual file path
    file_path = 'project.xlsx'

    # Read the Excel sheet into a DataFrame
    df = pd.read_excel(file_path)   

    # Access questions and subjects columns
    questions = df['Question'].tolist()
    subjects = df['Subject'].tolist()

    # Set your OpenAI API key
    openai.api_key = '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'

    # Initialize score
    score = 0

    # Loop through questions and subjects
    for i in range(len(questions)):
        question = questions[i]
        subject = subjects[i]

        # Create a prompt with the question and the subject
        prompt = f"Question: {question}\nSubject: {subject}\nIs the answer correct or incorrect?"

        # Make a request to the OpenAI API for classification using the gpt-3.5-turbo engine
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
            prompt=prompt,
            max_tokens=50,
        )

        # Access the generated classification label from the API response
        classification_label = response['choices'][0]['text'].strip()

        # Output the classification label
        print("Question:", question)
        print("Classification Label:", classification_label)

        # If the answer is correct, increment the score
        if "correct" in classification_label:
            score += 1

        # Convert question to speech
        text_to_speech(question)

        # Wait for the user to press the "Next" button
        input("Press Enter for the next question...")

    # Display the final score
    print("Final Score:", score)

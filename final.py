from flask import Flask, render_template, request, jsonify
import pandas as pd
import openai
import speech_recognition as sr
import os

app = Flask(__name__)

openai.api_key = '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'

# Function to fetch questions from an Excel file
def fetch_questions_from_excel(file_path='project.xlsx'):
    df = pd.read_excel(file_path)
    questions = df['Question'].tolist()
    return questions

# Function to convert audio to text using Google's Speech Recognition API
def convert_audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text

# Function to check if the answer is correct using OpenAI API
def check_answer(question, answer):
    prompt = f"Question: {question}\nAnswer: {answer}\nIs the answer correct or incorrect?"
    response = openai.Completion.create(
        engine="davinci",  # Using the davinci engine for text classification
        prompt=prompt,
        max_tokens=50,
    )
    classification_label = response['choices'][0]['text'].strip()
    return "correct" in classification_label

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch questions from the Excel file
        questions = fetch_questions_from_excel()

        # Retrieve current question index
        current_question_index = int(request.form['currentQuestionIndex'])

        print(f'answer_{current_question_index}')
        # Retrieve user audio answer file from the form
        audio_file = request.files[f'answer_{current_question_index}']
    
        
        # Save the audio file to a temporary location
        audio_file_path = f"temp_{current_question_index}.wav"
        print(audio_file_path)
        audio_file.save(audio_file_path)
        
        # Convert audio file to text
        answer_text = convert_audio_to_text(audio_file_path)
        
        # Remove the temporary audio file
        # os.remove(audio_file_path)
        
        # Check if the answer is correct
        question = questions[current_question_index]
        is_correct = check_answer(question, answer_text)

        # Update score if the answer is correct
        score = int(request.form['score'])
        if is_correct:
            score += 1

        # Increment the question index for the next iteration
        current_question_index += 1

        # Prepare data to send back to client-side JavaScript
        data = {
            'score': score,
            'currentQuestionIndex': current_question_index,
            'isEnd': current_question_index >= len(questions),
            'recognizedText': answer_text  # Add the recognized text to the response data
        }

        return jsonify(data)

    # Render the template with questions when the page is loaded
    questions = fetch_questions_from_excel()
    return render_template('index.html', questions=questions, score=0, currentQuestionIndex=0)


if __name__ == '__main__':
    app.run(debug=True)

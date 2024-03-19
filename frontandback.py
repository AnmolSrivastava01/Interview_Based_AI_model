from flask import Flask, render_template, request
import pandas as pd
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

def fetch_questions_from_excel(file_path='project.xlsx'):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Access the 'Question' column
    questions = df['Question'].tolist()
    return questions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve user answers from the form
        answers = request.form.getlist('answer')

        # Fetch questions from the Excel file
        questions = fetch_questions_from_excel()

        # Initialize score
        score = 0

        # Loop through questions and user answers
        for i, answer in enumerate(answers):
            question = questions[i]

            # Create a prompt with the question and the user's answer
            prompt = f"Question: {question}\nAnswer: {answer}\nIs the answer correct or incorrect?"

            # Make a request to the OpenAI API for classification using the gpt-3.5-turbo engine
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",  # Choose the appropriate engine
                prompt=prompt,
                max_tokens=50,
            )

            # Access the generated classification label from the API response
            classification_label = response['choices'][0]['text'].strip()

            # If the answer is correct, increment the score
            if "correct" in classification_label:
                score += 1

        # Display the final score
        return f'Your score is: {score}'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

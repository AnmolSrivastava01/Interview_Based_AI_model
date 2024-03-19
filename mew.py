import speech_recognition as sr
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak about yourself for a job interview:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)

    try:
        print("Transcribing speech...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None

def extract_job_domain(text):
    # In a real-world scenario, you might use more advanced techniques for job domain extraction
    # For simplicity, we'll check for specific keywords in the text
    if any(keyword in text.lower() for keyword in ["developer", "engineer", "designer"]):
        return "Software Development"
    elif any(keyword in text.lower() for keyword in ["manager", "coordinator", "leader"]):
        return "Management"
    else:
        return "Unknown"

def generate_questions(job_domain):
    # Define sample questions for different job domains
    question_dict = {
        "Software Development": [
            "Can you tell us about your experience with programming languages?",
            "What projects have you worked on in the past?",
        ],
        "Management": [
            "How do you handle team collaboration and leadership?",
            "Tell us about a challenging situation you successfully managed.",
        ],
        "Unknown": [
            "We're not sure about your specific job domain. Can you provide more details?",
            "What skills do you believe make you a valuable candidate?",
        ],
    }

    return question_dict.get(job_domain, question_dict["Unknown"])

def main():
    student_intro = speech_to_text()

    if student_intro:
        job_domain = extract_job_domain(student_intro)
        print(f"\nJob Domain: {job_domain}")

        questions = generate_questions(job_domain)

        print("\nSuitable Questions:")
        for i, question in enumerate(questions, start=1):
            print(f"{i}. {question}")

if __name__ == "__main__":
    main()

import speech_recognition as sr
from docx import Document

def convert_speech_to_text_and_save():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        # Save text to a Word document
        save_to_word(text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Error with the API request; {e}")

def save_to_word(text):
    document = Document()
    document.add_paragraph(text)

    file_path = "anmol121.docx"
    document.save(file_path)
    print(f"Text saved to '{file_path}'")

if __name__ == "__main__":
    convert_speech_to_text_and_save()

import openai
openai.api_key = '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'

with open("Recording.m4a", "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        file = audio_file,
        model = "whisper-1",
        response_format="text",
        language="en"
    )
print(transcript)
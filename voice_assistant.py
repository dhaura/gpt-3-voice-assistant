import openai
import pyttsx3
import speech_recognition as sr

# import OpenAI API key
openai.api_key = "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"

# initialize the text-to-speech engine
tts_engine = pyttsx3.init()


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Unknown Error\n")


def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]


def speak_text(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

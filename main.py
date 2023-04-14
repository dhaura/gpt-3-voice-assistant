import speech_recognition as sr
import voice_assistant as va


def run_voice_assistant():
    while True:
        # activate voice assistant by saying "Iris"
        print("Say \"Iris\" to activate...")
        va.speak_text("Say Iris to activate")

        print("Say \"Stop\" to exit...")
        va.speak_text("Say Stop to exit")

        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                user_command = recognizer.recognize_google(audio)
                print(user_command.lower())
                if user_command.lower() == "iris":
                    # record audio
                    input_filename = 'user-audio.wav'
                    print("How can I help you ?\n")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(input_filename, "wb") as audio_file:
                            audio_file.write(audio.get_wav_data())

                    # transcribe the audio to text
                    text = va.transcribe_audio_to_text(input_filename)
                    if text:
                        print(f"Question you asked: {text}\n")

                        # generate a response using Chat GPT-3
                        response = va.generate_response(text)
                        print(f"Chat GPT-3 says: {response}\n")

                        # read out the response
                        va.speak_text(response)
                elif user_command.lower() == "stop":
                    break
            except Exception as e:
                print(f"Error occurred: {e}\n")


if __name__ == '__main__':
    run_voice_assistant()


import pyttsx3
import speech_recognition
import openai
import config

openai.api_key = config.API_Key

recognizer = speech_recognition.Recognizer()
tts = pyttsx3.init()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized --> {text}")
            tts.say(text)
            tts.runAndWait()

            # Generate response using OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": text},
                ],
            )

            # Extract the reply from the OpenAI response
            reply = response.choices[0].message.content
            print(f"Reply --> {reply}")
            tts.say(reply)
            tts.runAndWait()

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue

    except KeyboardInterrupt:
        print("Program interrupted by the user.")
        break

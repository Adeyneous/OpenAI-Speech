# OpenAI-Speech
This code sets up a voice assistant that can listen to user input, convert it to text using speech recognition, generate a response using the OpenAI GPT-3.5 Turbo model, and speak the response back to the user using text-to-speech.

Here's a breakdown of what the code does:

It imports the necessary libraries: pyttsx3 for text-to-speech, speech_recognition for speech recognition, openai for using the OpenAI API, and config for storing the API key.

The OpenAI API key is set using openai.api_key = config.API_Key. This allows the code to authenticate and make requests to the OpenAI API.

The code initializes the speech recognition engine (recognizer) and the text-to-speech engine (tts).

The program enters a while loop that runs continuously until the user interrupts it. Within the loop:

a. The microphone is opened as a context using speech_recognition.Microphone().

b. The ambient noise is adjusted for with recognizer.adjust_for_ambient_noise(mic, duration=0.2) to account for any background noise.

c. Audio is captured from the microphone using recognizer.listen(mic) and stored in the audio variable.

d. The captured audio is converted to text using recognizer.recognize_google(audio), and the recognized text is stored in the text variable. It is also converted to lowercase.

e. The recognized text is printed to the console, spoken aloud using text-to-speech (tts.say(text)), and the program waits until the speech is finished (tts.runAndWait()).

f. The OpenAI API is called to generate a response using the GPT-3.5 Turbo model. The conversation history is provided as messages, including a system message and the user's input.

g. The response from OpenAI is extracted and stored in the reply variable. It is printed to the console, spoken aloud, and the program waits until the speech is finished.

The code handles exceptions:

a. If the speech recognition engine fails to recognize any speech (speech_recognition.UnknownValueError), it continues listening for new input by reinitializing the recognizer object.

b. If the user interrupts the program by pressing Ctrl+C or sending a KeyboardInterrupt signal, the loop is broken, and the program is terminated.

Overall, this code allows the voice assistant to listen, convert speech to text, generate responses using OpenAI, and communicate with the user through text-to-speech.

# Import necessary modules
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

# Initialize recognizer and microphone objects
r = sr.Recognizer()
mic = sr.Microphone()

# Prompt user to speak
print("Speak something in English:")
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

# Use speech recognition to convert speech to text
try:
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Could not understand audio.")
    exit()
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    exit()

# Use Google Translate API to translate text to Hindi
translator = Translator()
translated_text = translator.translate(text, src="en", dest="hi").text
print("Translated text: " + translated_text)

# Use Google Text-to-Speech API to generate voice file
tts = gTTS(text=translated_text, lang="hi")
tts.save("translated_audio.mp3")

# Use OS module to play back voice file
os.system("start translated_audio.mp3")

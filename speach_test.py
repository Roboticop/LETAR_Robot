from gtts import gTTS
import os
from playsound import playsound

text = "I am going to say some stuff to test out the speech module"
language = "en"

speech = gTTS(text = text, lang = language, slow = False)

speech.save("text.mp3")
playsound("text.mp3")
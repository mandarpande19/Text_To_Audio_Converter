from gtts import gTTS
from playsound import playsound
audio = input("Enter the file name in .mp3 : ")
language = 'en'
TEXT = input("Enter Ur text: ")
sp = gTTS(TEXT, lang=language, slow=False)
sp.save(audio)
playsound(audio)

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import asyncio
import random

duration = 5  # secondi di registrazione
sample_rate = 44100



parole=["cane", "gatto", "uccello", "beluga"]

parola_casuale=random.choice(parole)

try:
    translator = Translator()
    traduzione = translator.translate(parola_casuale, dest='es')      
    parola_tradotta=traduzione.text


except sr.UnknownValueError:             # - se Google non è riuscito a comprendere il discorso a causa di rumori o silenzi
    print("Il parlato non è stato riconosciuto.")
except sr.RequestError as e:             # - se non c'è connessione Internet o l'API non è disponibile
    print(f"Errore di servizio: {e}")


print(f"benvenuto nel gioco dellla traduzione traduci questa parola:{parola_casuale}")
recording = sd.rec(
  int(duration * sample_rate), # il numero di campioni da registrare
  samplerate=sample_rate,      # frequenza di campionamento
  channels=1,                  # 1 significa registrazione mono
  dtype="int16")               # tipo di dati per i campioni registrati
sd.wait()  # in attesa che la registrazione finisca

wav.write("output.wav", sample_rate, recording)
print("Registrazione completata, ora in fase di riconoscimento...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="es-ES")
    print("Hai detto:", text)

    if text == parola_tradotta:
        print(f"la tua risposta è corretta {parola_casuale} si traduce in {parola_tradotta}")
    else:
        print(f"nn sai lo spagnolo stupid lil bro, la traduzione è {traduzione}")    

except sr.UnknownValueError:             # - se Google non è riuscito a comprendere il discorso a causa di rumori o silenzi
    print("Il parlato non è stato riconosciuto.")
except sr.RequestError as e:             # - se non c'è connessione Internet o l'API non è disponibile
    print(f"Errore di servizio: {e}")
import os
from pytube import YouTube
from pydub import AudioSegment
import speech_recognition as sr

def download_audio(youtube_url):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download(filename='audio')
    return audio_file

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    audio_segment = AudioSegment.from_file(audio_file)
    audio_segment.export("audio.wav", format="wav")

    with sr.AudioFile("audio.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        with open("captions.txt", "w") as file:
            file.write(text)
        print("Transcription terminée. Le texte est enregistré dans captions.txt")
    except sr.UnknownValueError:
        print("Audio non compris")
    except sr.RequestError as e:
        print(f"Erreur lors de la requête ; {e}")

if __name__ == "__main__":
    url = input("Entrez l'URL de la vidéo YouTube : ")
    audio_file = download_audio(url)
    transcribe_audio(audio_file)
    os.remove(audio_file)

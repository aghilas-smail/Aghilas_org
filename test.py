import speech_recognition as sr

def transcribe_live_audio():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Réglage du bruit ambiant...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    print("Transcription en direct en cours... (Appuyez sur Ctrl+C pour arrêter)")

    try:
        while True:
            with microphone as source:
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio, language="fr-FR")
                    print("Vous avez dit : " + text)
                except sr.UnknownValueError:
                    print("Audio non compris")
                except sr.RequestError as e:
                    print(f"Erreur lors de la requête ; {e}")
    except KeyboardInterrupt:
        print("Transcription arrêtée.")

if __name__ == "__main__":
    transcribe_live_audio()

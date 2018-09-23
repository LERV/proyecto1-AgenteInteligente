import speech_recognition as sr
r = sr.Recognizer()

def escuchar():
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        print("System predicts:"+r.recognize_google(audio, language = "es-ES"))
    except Exception:
        print ("Something went wrong")

while(1):
    escuchar()
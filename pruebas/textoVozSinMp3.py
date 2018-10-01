import pyttsx3
engine = pyttsx3.init()

#Con esta linea el mae, escoge de las voces que tengo instaladas a Sabina, sino por defecto usa la del idioma de la compu que fue David(Ingles)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')



engine.say('Hola hola ciudadano, el perro come comida piña, jocote, avión, agüero')
engine.runAndWait()



#COdigo para escuchar el mensaje en todos los idiomas instalados

##engine = pyttsx3.init()
##voices = engine.getProperty('voices')
##for voice in voices:
##   engine.setProperty('voice', voice.id)
##   engine.say('The quick brown fox jumped over the lazy dog.')
##engine.runAndWait()

import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

name = 'Alexa' #nombre de nuestra asistente virtual 
key = 'AIzaSyALlxbBFBarxci-TMtL5luWHAw6VGnagxM'
listener = sr.Recognizer()
mon = pyttsx3.init()
voices = mon.getProperty('voices')
mon.setProperty('voice',voices[2].id)

#for voice in voices:
    #print(voice)
def talk(text):
    mon.say(text)
    mon.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("escuchando...")
            voice = listener.listen(source)
            #voice = listener.adjust_for_ambient_noise(voice)
            rec = listener.recognize_google(voice)
            #rec = rec.lower()
            print (rec)
            if name in rec:
                rec = rec.replace(name,'') #para quitar el nombre del texto introducido
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce','')
        talk('Reproduciendo...'+ music)
        pywhatkit.playonyt(music)

    if 'cuantos suscriptores tiene' in rec:
        name_subs = rec.replace('cuantos suscriptores tiene', '')
        data = urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=' + name_subs.strip() + '&key=' + key).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs + "tiene {:,d}".format(int(subs)) + " suscriptores!")

    if 'hora' in rec:
        hora = datetime.datetime().now().strftime('%I:%M %p')
        talk("Son las "+hora)

    if 'busca' or 'Busca'in rec:
        order = rec.replace('busca','')
        talk(order)
        info = wikipedia.summary(order,1)
        talk(info)
    else:
        talk("lo siento, no pude entenderte")
while True:
    run()

    


#buscar python pyjoke 
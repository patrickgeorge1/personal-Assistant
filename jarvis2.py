from gtts import gTTS
from io import BytesIO
import subprocess
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import smtplib
import timeit
import datetime

                          # vorbeste
def talkToMe(text, engine):       # trebuie instalat sudo apt-install espeak-ng....
    engine.say(text)
    engine.runAndWait()


def setVoice():                                           # set some voice parameters
    engine = pyttsx3.init(driverName='espeak')
    engine.setProperty('rate',137)  #120 words per minute
    engine.setProperty('volume',0.9) 
    engine.setProperty('voice', 'english')  # also 'romanian'
    return engine


def setMic():
    "Configure the mic https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst"
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True          # when it s active you can configure manually
    r.energy_threshold = 4000                  # sensitivity for a average room
    #r.pause_threshold = 1
    #r.dynamic_energy_adjustment_ratio = 3.5
    r.pause_threshold = 0.5                    # time that wait until end the phase
    #with sr.Microphone() as source:
    #    r.adjust_for_ambient_noise(source, duration=1.5)
    return r
 





def myCommand(r):                          
    "listens for commands"
    with sr.Microphone() as source:                  # asculta
        print("Go")
        audio = r.listen(source, None, 2)               # asteapta max 1 sec si asculta max 2 sec
        #audio = r.listen(source)
 
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        #talkToMe(command, engine)
        assistant(command)

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand(r);

    return command

 





def assistant(command):                                  #exec
    if 'open google' in command:                                                      # open Google
        talkToMe(command, engine)
        chrome_path = '/usr/bin/google-chrome'
        url = "https://www.google.com/"
        webbrowser.get(chrome_path).open(url)
        #talkToMe("Reddit")
    if 'exit' in command:                                                             # shut down itself 
        talkToMe("Goodbye creator", engine)
        quit()
    if 'who is the out boss' in command:                                              # know reality
        talkToMe("God is", engine)
    if 'search for' in command:                                                       # know how to browse on google  
        talkToMe(command, engine)
        no_wites = command.split(" ")
        parsed = no_wites[2]
        for x in range(3, len(no_wites)):
            parsed = parsed + "+" + no_wites[x]
        link = "https://www.google.ro/search?q=" + parsed
        chrome_path = '/usr/bin/google-chrome'
        webbrowser.get(chrome_path).open(link)

    if 'shutdown my pc' in command:                                                   # shutdown my pc 
        talkToMe("shutting down", engine)
        os.system('systemctl poweroff')
    if 'what time' in command:
        talkToMe("Time is", engine)
        now = datetime.datetime.now()
        engine.setProperty('rate',110)
        talkToMe("Hour . " + str(now.hour) + " .  Minutes  .  " + str(now.minute) ,engine)
        engine.setProperty('rate',137)
    if '' in command:
        pass



engine = setVoice()
r = setMic()                  # set the mic parameters
talkToMe("Hello Patrick !", engine)
while True:
    myCommand(r)
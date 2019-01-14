from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import timeit

def talkToMe(audio):                          # vorbeste
    #start = timeit.timeit()
    print(audio)
    tts = gTTS(text=audio, lang="en")
    tts.save("audio.mp3")
    os.system('mpg123 audio.mp3')
    #end = timeit.timeit()
    #print("Time = " + str(end - start))




def set():
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
        talkToMe(command)

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand(r);

    return command

 





def assistant(command):                                  #executa
    if 'reddit' in command:
        '''
        chrome_path = '/usr/bin/google-chrome'
        url = "https://www.reddit.com/r/python"
        webbrowser.get(chrome_path).open(url)'''
        #talkToMe("Reddit")





r = set()                  # set the mic parameters
talkToMe("Hello Patrick !")
while True:
    myCommand(r)
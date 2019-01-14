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
	os.system('mpg321 audio.mp3')
	#end = timeit.timeit()
	#print("Time = " + str(end - start))



 
def myCommand():                           # asculta
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        start = timeit.timeit()
        audio = r.listen(source)
        print("with")

    try:
        command = r.recognize_google(audio).lower()
        end = timeit.timeit()
        print("Time = " + str(end - start))
        talkToMe(command)
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

 
def assistant(command):                                  #executa
	if 'reddit' in command:
		'''
		chrome_path = '/usr/bin/google-chrome'
		url = "https://www.reddit.com/r/python"
		webbrowser.get(chrome_path).open(url)'''
		#talkToMe("Reddit")


talkToMe("Hello Patrick !")
while True:
	assistant(myCommand())
import pyttsx3

x = input()

engine = pyttsx3.init()
engine.say(x)
engine.runAndWait()

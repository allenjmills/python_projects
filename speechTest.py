#!/Python27/

import speech_recognition as sr
from ouimeaux.environment import Environment

def on_switch(sw):
	print  "Switch found!", sw.name

env = Environment(); env.start()
env.discover(5)

barLights = env.get_switch("Bar Lights")
bedroomLight = env.get_switch("Bedroom Light")

#obrain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)

# recognize speech using Wit.ai
WIT_AI_KEY = "S6GRTNGQSDYWIBFSCYBGS6DZMYRGHS52"
try:
	print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
	print("Wit.ai could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Wit.ai service; {0}".format(e))

if r.recognize_wit(audio, key=WIT_AI_KEY) == "turn on the bar lights":
	barLights.on();
elif r.recognize_wit(audio, key=WIT_AI_KEY) == "turn off the bar lights":
	barLights.off();
elif r.recognize_wit(audio, key=WIT_AI_KEY) == "turn on the bedroom light":
	bedroomLight.on();
elif r.recognize_wit(audio, key=WIT_AI_KEY) == "turn off the bedroom light":
	bedroomLight.off();
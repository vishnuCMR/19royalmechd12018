import speech_recognition as sr


r = sr.Recognizer()

with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source ,duration=5)
	r.dynamic_energy_threshold = True
	print("Say Something")
	audio=r.listen(source)



try:
	print("you said : " + r.recognize_google(audio))
except sr.UnknownValueError:
	print("Google speech recognititon could not understand audio")
except sr.Requesterror as e:
	print("could not request result from google speech recognititon service: {0}".format(e))

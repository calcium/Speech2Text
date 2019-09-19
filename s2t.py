# https://realpython.com/python-speech-recognition/
import speech_recognition as sr
sr.__version__
r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
# print r.recognize_bing(audio)  #: Microsoft Bing Speech
# print r.recognize_google_cloud(audio)  #: Google Cloud Speech - requires installation of the google-cloud-speech package
# print r.recognize_houndify(audio)  #: Houndify by SoundHound
# print r.recognize_ibm(audio)  # IBM Speech to Text
# print r.recognize_google(audio)  #: Google Web Speech API
print r.recognize_sphinx(audio)  #: CMU Sphinx - requires installing PocketSphinx
# print r.recognize_wit(audio) #  Wit.ai

import sys
import speech_recognition as sr

fn = sys.argv[1]

print 'Speech to text of', fn

r = sr.Recognizer()
pcmfile = sr.AudioFile(fn)
with pcmfile as source:
    audio = r.record(source)

# https://azure.microsoft.com/en-au/pricing/details/cognitive-services/speech-services/
print "google heard {}".format(r.recognize_google(audio))
print "sphinx heard says {}".format(r.recognize_sphinx(audio))
print "IBM heard {}".format(r.recognize_ibm(audio))
print "bing says {}".format(r.recognize_bing(audio))

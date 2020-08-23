#Step1:import required python libraries 
import speech_recognition as sr
import sys

#Step2:read duration from the arguments
duration = int(sys.argv[1])

#Step3: initialize the recognizer
r = sr.Recognizer()
print("Please talk")

with sr.Microphone() as source:

#Step4 read the audio data from the default microphone
    audio_data = r.record(source, duration=duration)
    print("Recognizing...")
    
#Step5 convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
    
    
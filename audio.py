# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 07:41:20 2020

@author: saimi
"""

import wave
import pyaudio
import speech_recognition as sr
import subprocess
from commands import Commander


running = True

def say(text):
    subprocess.call('say ' + text, shell = True)
    #subprocess.call("PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('"+ text +"')", shell=True)

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    
    stream = pa.open(
            format = pa.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True)
    
    data_stream = wf.readframes(chunk)
    
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
        
    stream.close()
    pa.terminate()
    
    
r = sr.Recognizer()
cmd = Commander()

def init_speech():
    print("Listening..")
    play_audio("./audio/audio_initiate.wav")
    
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
        
    play_audio("./audio/audio_end.wav")        
        
    command = ""
    
    try:
        command = r.recognize_google(audio)
    except:
        print("Could not understand you")
        
    print("Your Command:")
    print(command)
    if command in ["quit", "exit", "bye", "goodbye"]:
        global running
        running = False
        
    cmd.discover(command)    
# =============================================================================
#     say('You said: ' + command)    #   change speak to say ********
# =============================================================================
 
while running == True:   
    init_speech()    
    
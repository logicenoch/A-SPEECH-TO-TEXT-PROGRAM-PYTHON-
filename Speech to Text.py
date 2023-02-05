# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 01:48:33 2023
@author: OKEKE ENOCH CHIBUZO
"""

import speech_recognition as sr
from time import sleep

# Instantiation of the Recognizer class
rEngine = sr.Recognizer()

def header():
    disp_msg = """
    #####################################################
    #####################################################
    ############ SPEECH TRANSCRIPTION SYSTEM ############
    #####################################################
    #####################################################            
    """
    print(disp_msg)

def getFileName():
    # Gets the audio file(name) to be transcribed
    filename = input("Audio Filename(ends with .wav, .flac, .aiff): ")
    return filename.lower().strip()


def getAudioData(filename):
    # Gets the Audiofile instance of the file,
    # Reads the content of the Audiofile instance,
    # Performs a bit DSP on the audo file(ambient noise),
    # and returns the audio data object of the Audiofile instance.
    audf_instance = sr.AudioFile(filename)
    print(f"Reading {filename}...")
    sleep(5)
    with audf_instance as aud_source:
        rEngine.adjust_for_ambient_noise(aud_source, duration=0.5)
        print("Adjusting ambient noise...")
        sleep(5)
        aud_Data = rEngine.record(aud_source)

    return aud_Data


def getTranscription(aud_data):
    # Returns the transcription of the said audio data
    # instance of the audio file.
    try:
        print("Transcribing the audio file...")
        sleep(5)
        transcribed = rEngine.recognize_google(aud_data, language="en-USA")
    except Exception as error:
        print(f"An error occurred during transcription, {error}")
        return None

    return transcribed


def main():
    # main function
    header()
    audio_file = getFileName()
    audio_Data = getAudioData(audio_file)
    final = getTranscription(audio_Data)
    print("\n\n")
    print("||||||||||TRANSCRIPTION||||||||||\n")
    print(final)


main()

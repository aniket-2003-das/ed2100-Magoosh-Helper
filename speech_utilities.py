import sys
import os
import datetime
import pyttsx3
import time

# Currently age and female properties are not available
# They are just added as skeleton
# When a workaround or provision for such properties will be available,
# then at that time this function will modified to get voice property of that
# Currently only by accent voice proprety is returned


def get_voice_property(engine, age=30, gender='female', accent='english-us'):
    voices = engine.getProperty('voices')
    for voice in voices:
        if accent in str(voice.name):
            return voice

    raise ValueError('Demanded accent does not matched')


def onStartUtterance(name):
    print(name)


def speak_sentences(sentences, max_sentences_to_be_spoken=sys.maxsize):
    max_sentences_to_be_spoken = min(
        max_sentences_to_be_spoken, len(sentences))

    i = 1
    for s in sentences:
        if i > max_sentences_to_be_spoken:
            break
        print(s)
        speak_single_sentence(s)
        i += 1


def speak_single_sentence(sentence):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)

    voice = get_voice_property(engine, age=10, gender='female', accent='hindi')
    voice = get_voice_property(
        engine, age=10, gender='female', accent='english')
    voice = get_voice_property(
        engine, age=10, gender='female', accent='default')
    voice = get_voice_property(
        engine, age=10, gender='female', accent='english-north')
    voice = get_voice_property(
        engine, age=10, gender='female', accent='english_rp')
    voice = get_voice_property(
        engine, age=10, gender='female', accent='english_wmids')
    voice = get_voice_property(
        engine, age=10, gender='female', accent='default')

    engine.setProperty('voice', voice.id)
    engine.say(sentence)
    engine.runAndWait()


if __name__ == '__main__':
    pass

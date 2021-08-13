import pyttsx3
import wikipedia
engine = pyttsx3.init()
def say(audio):
    engine.say(audio)
    engine.runAndWait()
def searcher(text):
    tt = wikipedia.summary(text)
    print(tt)
    say(tt)
    name = input('MORE WORD FINDER IS READY: ')
    print('YOU HAVE SEARCHED: ', name)
    searcher(name)

searcher('text')

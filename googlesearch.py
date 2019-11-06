
import speech_recognition as sr
import webbrowser
sr.
r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source,timeout=2,phrase_time_limit=2)
    try:
        g = r.recognize_google(audio)
        webbrowser.open("https://www.google.com/search?sxsrf=ACYBGNSsWLZjlbHNh3WTQAog6vpOC91CXw%3A1573021112275&source=hp&ei=uGXCXf6QDtqb9QPz7bCQCA&q="+g+"&btnK=Google+Search")
        print(g)
        
    except Exception as e:
        print(e)

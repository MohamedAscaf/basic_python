import speech_recognition as sr
import webbrowser as wb
r=sr.Recognizer()
url="https://www.google.co.in/search?q="
#url="https://www.youtube.com/results?search_query="
with sr.Microphone() as source:
        print("speak....., It is the Google Search..., what do you want to Search..")
        audio=r.listen(source)
        try:
            get=r.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError as e:
            print('failed'.format(e))
        except:
            print("Microphone not detected")

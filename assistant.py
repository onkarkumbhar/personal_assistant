###########################################
### This will be import section
import webbrowser
import speech_recognition as sr
import selenium
from gtts import gTTS
from playsound import playsound
import os
###########################################
b = 1
myobj = gTTS(text="Hi there. please Enter your name?", lang="en", slow=False)
myobj.save("sample00.mp3")
playsound('sample00.mp3')
os.remove("sample00.mp3")
name=input("Enter Your Name:-")
if name == 'onkar-boss':
    myobj = gTTS(text="Hi Boss. I miss you so much. Welcome you back.",lang="en", slow=False)
    myobj.save("sample00.mp3")
    playsound('sample00.mp3')
    os.remove("sample00.mp3")
    os.system('cls')
else:
    myobj = gTTS(text="Hi there. I am Onkar's best friend. I am here to help you. Onkar gave you this, so you are also my friend now onwards. Below tasks I can do.", lang="en", slow=False)
    myobj.save("sample00.mp3")
    playsound('sample00.mp3')
    os.remove("sample00.mp3")
    print("--help\nsearch <query>\nopen chrome\nopen youtube\nopen google\nopen gmail\nopen notepad\nopen calculator\nopen teams\nopen whatsapp\nopen discord\nopen slack\n0")
while b:
    wish = input("Enter what you want to do?")
    count = 0

    if wish == '--help' or wish == '-h':
        print("Welcome To Onkar's assistant")
        if name == "onkar-boss":
            myobj = gTTS(text="Hi Boss.I am here to help you. Below tasks I can do. Enter 0 to exit.",lang="en", slow=False)
            myobj.save("sample00.mp3")
        else:
            myobj = gTTS(text="Hi there. I am Onkar's best friend. I am here to help you. Below tasks I can do. Enter 0 to exit.", lang="en", slow=False)
            myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        print("--help\nsearch <query>\nopen chrome\nopen youtube\nopen google\nopen gmail\nopen notepad\nopen calculator\nopen teams\nopen whatsapp\nopen discord\nopen slack\n0")
        count += 1

    if "search" in wish:
        myobj = gTTS(text="Searching query using google chrome", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        query = 'https://www.google.com/search?q='
        for i in range(7, len(wish)):
            query += wish[i]
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(query)
        #webbrowser.open_new(query)
        count += 1
    if wish == "open discord":
        myobj = gTTS(text="Opening discord", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        webbrowser.open_new("https://discord.com/channels/")
        count += 1

    if wish == "open slack":
        myobj = gTTS(text="Opening Slack", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        os.system("start slack:")
        count += 1

    if wish == "open whatsapp":
        myobj = gTTS(text="Opening Whatsapp", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        os.system("start whatsapp:")
        count += 1

    if wish == "open teams":
        myobj = gTTS(text="Opening MS teams", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        os.system("start msteams:")
        count += 1

    if wish == "open notepad":
        myobj = gTTS(text="Opening notepad", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        os.system('start notepad')
        count += 1

    if wish == "open chrome":
        myobj = gTTS(text="Opening Google chrome", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        os.startfile("C:\Program Files\Google\Chrome Dev\Application\chrome.exe")
        #os.system('start Google Chrome Dev:')
        count += 1

    if wish == "open calculator":
        myobj = gTTS(text="Opening calculator", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        os.system('start Calculator:')
        count += 1

    if wish == "open youtube":                     # here we will open youtube
        a = webbrowser.open_new('www.youtube.com')
        if a == True:
            myobj = gTTS(text="Opening Youtube", lang="en", slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')
        else:
            myobj = gTTS(text="Not able to open Youtube", lang="en", slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')
        count += 1

    if wish == "open google":
        a = webbrowser.open_new('www.google.com')
        if a == True:
            myobj = gTTS(text="Opening google", lang="en", slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')
        else:
            myobj = gTTS(text="Not able to open google", lang="en", slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')
        count += 1

    if wish == "open gmail":
        a = webbrowser.open_new('https://mail.google.com/mail')
        if a == True:
            myobj = gTTS(text="Opening gmail", lang="en", slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')
        else:
            myobj = gTTS(text="Not able to open gmail", lang="en", slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')
        count += 1

    if wish == '0':
        if name == "onkar-boss":
            myobj = gTTS(text="Boss.I will miss you so much. Have a good day. We will meet soon.Thank you.",lang="en", slow=False)
            myobj.save("sample00.mp3")
        else:
            myobj = gTTS(text="Thank You. for engaging with me !!See You soon", lang="en", slow=False)
            myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        b = 0
        count += 1

    if count == 0:
        myobj = gTTS(text="Sorry I didn't get you. Can you recheck your input?. You can type dash dash help to get help. Thanks", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')

    os.remove('sample00.mp3')
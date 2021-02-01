###########################################
### @Author:= Kumbhar Onkar Sandeep
### Sub:-Personal Assistant
### Note:-1)Please Do not edit Author name
###       2)Change code with your comfortness
##########################################
import webbrowser
import argparse
import time
import os
import random
###########################################
parser = argparse.ArgumentParser(description="This is onkar's personal assistant")
parser.add_argument("-o", "--online", help="Enter 1 if you are online else enter 0",type=int)
option = parser.parse_args()
os.system("cls")
os.system("color 4")
print("\t\t  ___                    ___  ")
print("\t\t (o o)                  (o o)")
print("\t\t(  V  ) @Onkar Kumbhar (  V  )")
print("\t\t--m-m--------------------m-m--\n\n\n")
os.system("color 2")
if option.online == 1:
    print("Ya I got it...You are online....Procedding to online mode\n")
    from gtts import gTTS
    from playsound import playsound
    b = 1
    myobj = gTTS(text="Hi there. please Enter your name?", lang="en", slow=False)
    myobj.save("sample00.mp3")
    playsound('sample00.mp3')
    os.remove("sample00.mp3")
    name = input("Enter Your Name:-")
    os.system("color 1")
    if name == 'onkar-boss':
        myobj = gTTS(text="Hi Boss. I miss you so much. Welcome you back.", lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        os.remove("sample00.mp3")
        os.system('cls')
    else:
        myobj = gTTS(
            text="Hi there. I am Onkar's best friend. I am here to help you. Onkar gave you this, so you are also my friend now onwards. Below tasks I can do.",
            lang="en", slow=False)
        myobj.save("sample00.mp3")
        playsound('sample00.mp3')
        os.remove("sample00.mp3")
        print(
            "--help\nsearch <query>\nopen chrome\nopen youtube\nopen google\nopen gmail\nopen notepad\nopen calculator\nopen teams\nopen whatsapp\nopen discord\nopen slack\n0")
    while b:
        wish = input("Enter what you want to do?")
        count = 0

        if wish == '--help' or wish == '-h':
            print("Welcome To Onkar's assistant")
            if name == "onkar-boss":
                myobj = gTTS(text="Hi Boss.I am here to help you. Below tasks I can do. Enter 0 to exit.", lang="en",
                             slow=False)
                myobj.save("sample00.mp3")
            else:
                myobj = gTTS(
                    text="Hi there. I am Onkar's best friend. I am here to help you. Below tasks I can do. Enter 0 to exit.",
                    lang="en", slow=False)
                myobj.save("sample00.mp3")
            playsound('sample00.mp3')
            print(
                "--help\nsearch <query>\nopen chrome\nopen youtube\nopen google\nopen gmail\nopen notepad\nopen calculator\nopen teams\nopen whatsapp\nopen discord\nopen slack\n0")
            count += 1

        if wish == "thank you" or wish == "thanks":
            myobj = gTTS(text="You are welcome. I am here to help you. Available for 24 hours for you.", lang="en",
                         slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')
            count += 1

        if "search" in wish:
            myobj = gTTS(text="Searching query using google chrome", lang="en", slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')
            query = 'https://www.google.com/search?q='
            for i in range(7, len(wish)):
                query += wish[i]
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(query)
            # webbrowser.open_new(query)
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
            # os.system('start Google Chrome Dev:')
            count += 1

        if wish == "open calculator":
            myobj = gTTS(text="Opening calculator", lang="en", slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')
            os.system('start Calculator:')
            count += 1

        if wish == "open youtube":  # here we will open youtube
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
                myobj = gTTS(text="Boss.I will miss you so much. Have a good day. We will meet soon.Thank you.",
                             lang="en", slow=False)
                myobj.save("sample00.mp3")
            else:
                myobj = gTTS(text="Thank You. for engaging with me !!See You soon", lang="en", slow=False)
                myobj.save("sample00.mp3")
            playsound('sample00.mp3')
            b = 0
            count += 1

        if count == 0:
            myobj = gTTS(
                text="Sorry I didn't get you. Can you recheck your input?. You can type dash dash help to get help. Thanks",
                lang="en", slow=False)
            myobj.save("sample00.mp3")
            playsound('sample00.mp3')

        os.remove('sample00.mp3')
        r = random.randint(1, 7)
        color = "color "+str(r)
        os.system(color)
else:
    print("So you want to be in offline mode...Procedding to it....\n")
    time.sleep(1.5)
    print("Hi there,...I am Onkar's best friend and personal assistant\n")
    time.sleep(1.5)
    name = input("Enter Your Name:-")
    print("Those tasks I can do:-\n")
    time.sleep(0.5)
    print("--help\nsearch <query>\nopen chrome\nopen youtube\nopen google\nopen gmail\nopen notepad\nopen calculator\nopen teams\nopen whatsapp\nopen discord\nopen slack\n0")
    b = 1
    while b:
        wish = input("Enter what you want to do?")
        count = 0

        if wish == '--help' or wish == '-h':
            print("Welcome To Onkar's assistant\n")
            time.sleep(1)
            print("--help\nsearch <query>\nopen chrome\nopen youtube\nopen google\nopen gmail\nopen notepad\nopen calculator\nopen teams\nopen whatsapp\nopen discord\nopen slack\n0")
            count += 1

        if wish == "thank you" or wish == "thanks":
            print("You are welcome. I am here to help you. Available for 24 hours for you.\n")
            time.sleep(2)
            count += 1

        if "search" in wish:
            print("Searching query using google chrome\n")
            query = 'https://www.google.com/search?q='
            for i in range(7, len(wish)):
                query += wish[i]
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(query)
            count += 1
            time.sleep(1)
        if wish == "open discord":
            print("Opening discord\n")
            webbrowser.open_new("https://discord.com/channels/")
            count += 1
            time.sleep(1)
        if wish == "open slack":
            print("Opening Slack\n")
            os.system("start slack:")
            count += 1
            time.sleep(1)
        if wish == "open whatsapp":
            print("Opening Whatsapp\n")
            os.system("start whatsapp:")
            count += 1
            time.sleep(1)
        if wish == "open teams":
            print("Opening MS teams\n")
            os.system("start msteams:")
            count += 1
            time.sleep(1)
        if wish == "open notepad":
            print("Opening notepad\n")
            os.system('start notepad')
            count += 1
            time.sleep(1)
        if wish == "open chrome":
            print("Opening Google chrome\n")
            os.startfile("C:\Program Files\Google\Chrome Dev\Application\chrome.exe")
            # os.system('start Google Chrome Dev:')
            count += 1
            time.sleep(1)
        if wish == "open calculator":
            print("Opening calculator\n")
            os.system('start Calculator:')
            count += 1
            time.sleep(1)
        if wish == "open youtube":  # here we will open youtube
            a = webbrowser.open_new('www.youtube.com')
            if a == True:
                print("Opening Youtube\n")
            else:
                print("Not able to open Youtube\n")
            count += 1
            time.sleep(1)
        if wish == "open google":
            a = webbrowser.open_new('www.google.com')
            if a == True:
                print("Opening google\n")
            else:
                print("Not able to open google\n")
            count += 1
            time.sleep(1)
        if wish == "open gmail":
            a = webbrowser.open_new('https://mail.google.com/mail')
            if a == True:
                print("Opening gmail\n")
            else:
                print("Not able to open gmail\n")
            count += 1
            time.sleep(1)
        if wish == '0':
            if name == "onkar-boss":
                print("Boss.I will miss you so much. Have a good day. We will meet soon.Thank you.\n")
            else:
                print("Thank You. for engaging with me !!See You soon\n")
            b = 0
            count += 1
            time.sleep(1)
        if count == 0:
            print("Sorry I didn't get you. Can you recheck your input?. You can type dash dash help to get help. Thanks\n")
            time.sleep(1)
        r = random.randint(1, 7)
        color = "color " + str(r)
        os.system(color)
import sys
try:
    import pyttsx3,webbrowser,smtplib,random,wikipedia,datetime,wolframalpha,os,sys,feedparser,pyjokes
    import speech_recognition as sr

    engine = pyttsx3.init('sapi5')

    client = wolframalpha.Client('9UX7KT-4XR2YEALXK')

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[len(voices)-1].id)

    def speak(audio):
        print('Jarvis : ' + audio)
        engine.say(audio)
        engine.runAndWait()

    def greetMe():
        currentH = int(datetime.datetime.now().hour)
        if currentH >= 0 and currentH < 12:
            speak('Good Morning!')

        if currentH >= 12 and currentH < 18:
            speak('Good Afternoon!')

        if currentH >= 18 and currentH !=0:
            speak('Good Evening!')

    greetMe()

    username = str(input("Enter your username : "))
    password = str(input("Enter your password : "))

    if username == '' or username == 'default':
        username ='skp09876789@gmail.com'
    if password == '' or password == 'default':
        password ='hello everyone'



    speak('Hello sir, I am your digital assistant!!!!')
    speak('How may I help you?')
    speak('I can help you in two ways : ')
    speak('1 - Through voice command!')
    speak('2 - Through typing')
    speak('To enable voice command say  : activate voice command')
    speak('To enable typing say  : activate typing')
    speak('I am developed by  the Santosh Prajapati')

    re = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        re.pause_threshold =  1
        audio = re.listen(source)
    try:
        queryte = re.recognize_google(audio, language='en-in')
        print('User: ' + queryte + '\n')

    except :
        speak('sorry sir! due to some error by default typing mode is activated ')
        queryte='text mode'


    if queryte =='1' or queryte == 'voice' or queryte == 'voice command' or queryte == 'activate voice command' or queryte == 'activate voice mode' :
        speak('sir you have choosen voice mode')
        def myCommand():
                r = sr.Recognizer()                                                                                   
                with sr.Microphone() as source:                                                                       
                    print("Listening...")
                    r.pause_threshold =  1
                    audio = r.listen(source)
                try:
                    query = r.recognize_google(audio, language='en-in')
                    print('User: ' + query + '\n')
                    return query
                except sr.UnknownValueError:
                    plzMsgs = ['Sorry sir! I didn\'t get that! Try typing the command!!','sorry sir i am unable to recognise your voice kindly try typing the command','sir plz type the command']
                    speak(random.choice(plzMsgs))
                    query = str(input('Command: '))
                    print('User: ' + query + '\n')
                    return query
                except  sr.RequestError:
                    onMsgs = ['sorry sir! i am not online now','sorry sir! i am unable to talk to the internet','sorry sir i and internet are\'t talking now',]
                    speak(random.choice(onMsgs))
                    sys.exit()

    else:
        speak('sir you have choosen text mode')
        def myCommand():
            query = str(input('Command: '))
            return query


    def news():
        def parseRSS( rss_url ):
            return feedparser.parse( rss_url )
        
        def getHeadlines(rss_url):
            headlines = []
        
            feed = parseRSS(rss_url)
            for newsitem in feed['items']:
                headlines.append(newsitem['title'])
        
            return headlines
        
        allheadlines = []
        
        newsurls = {'googlenews': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',}
        
        for key, url in newsurls.items():
            
            allheadlines.extend(getHeadlines(url))
        
        
        for hl in allheadlines:
            newstell=hl
            speak(newstell)


    if __name__ == '__main__':

        while True:
        
            query = myCommand()
            query = query.lower()
            
            if query == 'open youtube' or query == 'youtube' or query == 'www.youtube.com' or query == 'youtube.com' :
                stMsgs = ['oening youtube','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                webbrowser.open('www.youtube.com')

            elif query == 'open google' or query == 'google' or query == 'www.google.com' or query == 'google.com' :
                stMsgs = ['oening google','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                webbrowser.open('www.google.com')

            elif query == 'open gmail' or query == 'open mail' :
                stMsgs = ['oening email','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                webbrowser.open('www.gmail.com')

            elif query == 'news' or query =='news please' or query == 'tell me some news'  or query == 'kindly tell me some news' or query == 'get me some news' or query == 'update me with news' or query == 'update me with whats going  across world':
                stMsgs = ['Telling news','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                news()

            elif query == 'what is your name' or query == 'tell me your name' or query == 'your name please' :
                speak('my name is jarvis sir')
                speak('i am your degital assistant')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))
            
            elif query == 'tell me about yourself' or query == 'give me your intro' or query == 'tell me something about you' or query == 'who made you' or query == 'who is your creator' or query == 'who is your god':
                speak('my name is jarvis sir')
                speak('i am your degital assistant')
                speak('i am under development by the Santosh Prajapti')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))

            elif query == 'jarvis' or query == 'jarvis are you online' or query == 'are you active now' or query == 'jarvis are you ready' or query == 'jarvis i need your help' or query == 'jarvis can you help me':
                speak('yes sir')
                speak('i am resay and online now')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))

            elif query == 'where is your home' or query == 'where do you live' or query == 'your address please' or query == 'tell me your address' or query == 'tell me your address please': 
                stMsgs = ['thank you for asking such a intro','thank you sir for such question','i am glad to know that you want to know about me']
                speak(random.choice(stMsgs))
                speak('thank you for asking such a intro')
                speak('i am your degital assistant')
                speak('i am under development by the Santosh Prajapti')
                speak('currently i don\'n have any home')
                stMsgs = ['how can i help you','let me help you','may you need my help']
                speak(random.choice(stMsgs))

            elif query == "what\'s up" or query == 'how are you' or query == 'what about you':
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy' , 'i am feeloing chilled waht about you sir']
                speak(random.choice(stMsgs))

            elif query == 'thanks' or query == 'thank you jarvis' or query == 'thank you' or query == 'thank you for help' or query == 'thank you for doing my things' or query == 'thanks fro help' :
                stMsgs = ['welcome sir','same to you sir','welcome to you sir']
                speak(random.choice(stMsgs))
                stMsgs = ['Just doing my things!','just doing my jobs sir', 'no need to say thanks sir', 'same to you sir', 'thank you sir i am nice and full of energy' , 'i am feeloing chilled now sir what abou you sir']
                speak(random.choice(stMsgs))
                
            elif query == 'thanks for help ' or query  == 'thaks you so much' or query == 'thank for all jarvis' or query == 'thaks jarvis' :
                stMsgs = ['welcome sir','same to you sir','welcome to you sir']
                speak(random.choice(stMsgs))
                stMsgs = ['Just doing my things!','just doing my jobs sir', 'no need to say thanks sir', 'same to you sir', 'thank you sir i am nice and full of energy' , 'i am feeloing chilled now sir what abou you sir']
                speak(random.choice(stMsgs))




            elif query == 'email' or query == 'send email' or query == 'send mail' :
                speak('Who is the recipient? ')
                recipient = myCommand()

                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(username,password)
                    server.sendmail(username, recipient+'@gmail.com', content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry sir! I am unable to send your message at this moment!')


            elif query =='nothing' or query == 'abort' or query == 'stop' or query == 'go away' or query == 'quit' or query == 'good by' :
                speak('okay')
                speak('Bye sir, have a good day.')
                sys.exit()
            

            elif query  == 'what is the time now' or query == 'tell me the time' or query == 'tell me systam time' or query == 'time now':
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"sir, the time is {strTime}")
                
            
            elif query == 'hello' or query == 'hi' or query == 'hii' or query == 'hy' or query == 'hyy' :
                hiMsgs = ['hello','hii','hi','hy','hello sir']
                speak(random.choice(hiMsgs))

            elif 'bye' in query or 'byy' in query or query == 'by' :
                speak('Bye sir, have a good day.')
                sys.exit()
                                        
            elif 'play music' in query or 'play song' in query or 'play my favourite song' in query :
                stMsgs = ['opening songs','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                webbrowser.open('https://play.google.com/music/listen')
                
                    

            elif query == 'jokes' or query == 'tell me a joke' or query == 'speak me joke' or query == 'speak joke':
                speak(pyjokes.get_joke(category='all'))
            
            elif query == 'restart' or query == 'restart my PC' or query == 'please restart my PC' or query == 'please restart' or query == 'reboot' or query == 'reboot my PC ' or query == 'restart my computer' or query == 'reboot my computer':
                speak('Rebooting')
                os.system("shutdown -t 10 -r -f") 
                sys.exit()

            elif query == 'shutdown' or query == 'shutdown my PC' or query == 'please shutdown my PC' or query == 'please shutdown' or query == 'shutdown my computer' or query == 'shutdown my computer':
                speak('Rebooting')
                os.system("shutdown -t 10 -s -f")
                sys.exit()

            elif 'search for on google' in query or 'search on google for' in query :
                stMsgs = ['opening google','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                if 'search for on google ' in query :
                    query=query.replace("search for on google",'')
                elif 'search on google for' in query :
                    query = query.replace('search on google for','')
                webbrowser.open('https://www.google.com/search?q='+query)

            elif 'search for on youtube' in query :
                stMsgs = ['opening youtube','ok processing ... your request ....','please wait... your request is being processed','ok']
                speak(random.choice(stMsgs))
                if 'search for on youtube ' in query :
                    query=query.replace("search for on youtube",'')
                elif 'search on youtube for' in query :
                    query = query.replace('search on youtube for','')
                webbrowser.open('https://www.youtube.com/results?search_query='+query)

            else:
                query = query
                speak('Searching...')
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).all
                        speak('I got this !!!')
                        speak(results)
                        
                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak('Got it.')
                        speak('WIKIPEDIA says - ')
                        speak(results)
            
                except:
                    webbrowser.open('https://www.google.com/search?q='+query)
            
            speak('Next Command! sir!')
except:
    print('An error occured kindly restart the program') 
    sy=input("Hit enter to exit ")
    sys.exit()
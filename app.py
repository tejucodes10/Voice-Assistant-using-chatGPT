import streamlit as st
import openai
import pyttsx3
import speech_recognition as sr
import webbrowser
from gtts import gTTS
import os


openai.api_key = "Enter-Your-API key"
completion = openai.Completion()
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def mic():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        st.write('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        st.write(f'User : {query}\n') 
    except Exception as e:
        st.write("Say that again please...")
        return "None"  

    return query

def open_website(query):
    query_parts = query.split()
    website = query_parts[query_parts.index("open") + 1]
    website = "www." + website + ".com"
    if 'youtube' in website:
        webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
    else : 
        webbrowser.open(website)

def answer(question):
    prompt = f'User : {question}\n Jarvis : '
    response = completion.create(prompt=prompt,engine="text-davinci-002",stop=['\\User'],max_tokens=2000)
    answer = response.choices[0].text.strip()
    return answer

def main():
    st.title("Hi! I'm Jarvis")
    question = mic()
    ans = answer(question)
    st.success(ans)
    speak(ans)
    if ans:
        tts = gTTS(text=ans, lang='en')
        tts.save("output.mp3")
        os.system("start output.mp3")
    
    if "open" in question:
        open_website(question)

if __name__ == '__main__':
    st.set_page_config(page_title="AI", page_icon=":guardsman:", layout="wide")
    html_temp = """
    <div style ="background-image:'C:/Users/ADITHYA VEDHAMANI/powerfull_jarvis_python/patterned-chaos-5k-2u.jpg'; padding: 13px">
    <h1 style ="color:#fff;text-align:center;">AI Voice Assistant  </h1>
    </div>
    """

        # this line allows us to display the front end aspects we have
    # defined in the above code
    
    st.markdown(html_temp, unsafe_allow_html = True)
    
    main()

    

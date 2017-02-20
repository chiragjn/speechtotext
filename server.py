import os
import time
import speech_recognition as sr
from flask import Flask, request

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET', 'POST'])
def convert():
    wav_url = request.form['recording_url']
    print wav_url
    os.system("wget -O Twilio.wav " + wav_url)
    # time.sleep(3)
    text = "Failed to transcribe"
    r = sr.Recognizer()
    try:
        with sr.WavFile('Twilio.wav') as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio, language="en-us", show_all=False)
            print text
        except LookupError, e:
            print "Lookup Error!"
            print e.message
    except Exception, e:
        print "File Download error"
        print e.message
    return text

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("8000")
  )

# speechtotext
Flask based app

Give a wav file url to '/' and get back as text the transcription of the wav file

POST request<br/>
'recording_url' = \<wav file url\>
<br/>

Will take time proportional to size of the wav file

# Dependencies<br/>
<br/>
Flask<br/>
requests<br/>
SpeechRecognition<br/>

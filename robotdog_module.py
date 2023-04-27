import cv2
import openai
import pyttsx3
import gtts
import os
import json
import requests








class RobotDog:

    def startRecording():
        vid = cv2.VideoCapture(0)

        while(True):
            ret, frame = vid.read()
            cv2.imshow('Robot Dog', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        vid.release()
        cv2.destroyAllWindows()

    

    def askQuestion():
        engine = pyttsx3.init()

        openai.api_key = "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"
        question = input("What is your question?")
        response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo' ,
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question},
        ])

        message = response.choices[0]['message']
        print(message['content'])
        engine.say(message)
        engine.runAndWait()


    def test():
        openai.api_key = "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"
        question = input("wuz ur question?")
        response = openai.ChatCompletion.create( model='gpt-3.5-turbo', messages=[ {"role": "system", "content": "Your are a helpful assistant."}, {"role": "user", "content": question}, ])
        message = response.choices[0]['message']
        print(message['content'])
        url = "https://api.uberduck.ai/speak"
        payload = { "pace": 1, "speech": message['content'] }
        headers = { "accept": "application/json", "uberduck-id": "anonymous", "content-type": "application/json", "authorization": "Basic cHViX2xhc2doa2NncnRjb256Z2tybjpwa185OTkyZDY4YS1mNWI0LTQ1MjktYjMyNi04YTM2MjA2OGY3Mzg=" }
        response = requests.post(url, json=payload, headers=headers)
        print(json.loads(response.text)["uuid"])
        url = "https://api.uberduck.ai/speak-status?uuid=" + json.loads(response.text)["uuid"]
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        print(response.text)

        print("The URL is: " + url)
        #print(url + '/audio.wav')
        link = requests.get(url + '/audio.wav')
        open('audio.wav', 'wb').write(link)

#RobotDog.startRecording()
#RobotDog.askQuestion()
RobotDog.test()
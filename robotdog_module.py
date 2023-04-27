import cv2
import openai
import pyttsx3
import gtts


from playsound import playsound

import os






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
        tts = gtts.gTTS("Hola Mundo", lang="en")
        tts.save("hola.mp3")
        playsound("hola.mp3")


#RobotDog.startRecording()
#RobotDog.askQuestion()
RobotDog.test()
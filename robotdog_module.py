import cv2
  


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

    

#RobotDog.startRecording()
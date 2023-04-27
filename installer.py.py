import os 
import platform
import time


class OperatingSystem:
    name = platform.system()
    release = platform.release()
    version = platform.version()


print(OperatingSystem.name, OperatingSystem.release, OperatingSystem.version)


if OperatingSystem.name == 'Windows':
    os.system('pip install opencv-python')
    os.system('pip install openai')
    os.system('pip install pyttsx3')
    time.sleep(5)
else: 
    os.system('pip3 install opencv-python')
    os.system('pip3 install openai')
    os.system('pip3 install pyttsx3')
    time.sleep(5)

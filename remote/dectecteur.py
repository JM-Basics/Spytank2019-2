import spytank
from threading import Thread
from gtts import tts
import os
import time

class newDetecteur(Thread):
    def _init_(self, stop):
        Thread.__init__(self)
        self.stop = stop
        self.audio = tts.gTTS("bip bip", lang="fr")
        self.audio.save("bip.mp3")


    def run(self):
        #le code à executer durant l'opération
        distance = spytank.litDistance()
        if distance < 10:
            self.stop = True
            spytank.stop()
            os.system("mpg321 bip.mp3")
        else: 
            self.stop = False
        time.sleep(0.2)
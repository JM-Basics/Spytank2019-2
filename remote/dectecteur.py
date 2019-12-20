import spytank
from threading import Thread
from gtts import tts
import os

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
            os.system("mpg321 bip.mp3")
        else: 
            self.stop = False
#-------------------------
# D. Williams 29507820
# This class is used to play audio files without interrupting the main game functions
#-------------------------

import stdaudio, threading

class Sound:

    @staticmethod
    def playsound(filename):
        threading.Thread(target = stdaudio.playFile, args = (filename,), daemon = True).start()

    

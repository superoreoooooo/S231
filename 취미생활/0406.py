import winsound
import threading
import time

sound = {"c5" : 523, "d5" : 587, "e5" : 659, "f5" : 698, "g5" : 783, "a5" : 880, "b5" : 987, "c6" : 1046}

threading.Thread(target = winsound.Beep(sound["f5"], 300)).start()
threading.Thread(target = winsound.Beep(sound["g5"], 300)).start()

time.sleep(0.3)

threading.Thread(target = winsound.Beep(sound["f5"], 300)).start()
threading.Thread(target = winsound.Beep(sound["g5"], 300)).start()

time.sleep(0.3)

threading.Thread(target = winsound.Beep(sound["f5"], 300)).start()
threading.Thread(target = winsound.Beep(sound["g5"], 300)).start()

time.sleep(0.3)


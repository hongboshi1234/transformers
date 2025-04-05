import os
import time
class Timer:
    def __init__(self):
        self.start_time = time.time()

    def end(self, msg=""):
        if os.getenv('TIMING_ENABLED', 'False') == 'True':
            end_time = time.time()
            print(f"time for {msg}: {end_time - self.start_time} seconds ")

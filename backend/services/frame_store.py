"""
frame_store.py

Thread-safe storage for
latest processed camera frame.
"""


import threading
import time



class FrameStore:


    def __init__(self):

        self.frame = None

        self.lock = threading.Lock()

        self.timestamp = None



    def update(
        self,
        frame
    ):


        with self.lock:


            self.frame = frame.copy()

            self.timestamp = time.time()




    def get(self):


        with self.lock:


            if self.frame is None:

                return None



            return self.frame.copy()




    def get_age(self):


        with self.lock:


            if self.timestamp is None:

                return None



            return (
                time.time()
                -
                self.timestamp
            )




    def clear(self):


        with self.lock:

            self.frame = None

            self.timestamp = None




frame_store = FrameStore()
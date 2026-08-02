"""
video_stream.py

Streams processed camera frames
to factory safety dashboard.
"""


import cv2
import time

from backend.services.frame_store import frame_store



STREAM_FPS = 15

FRAME_DELAY = 1 / STREAM_FPS



def generate_frames():


    last_time = 0



    while True:


        current_time = time.time()



        # FPS control

        if (
            current_time - last_time
            <
            FRAME_DELAY
        ):

            time.sleep(0.005)
            continue



        last_time = current_time



        frame = frame_store.get()



        if frame is None:

            time.sleep(0.01)

            continue




        success, buffer = cv2.imencode(
            ".jpg",
            frame,
            [
                cv2.IMWRITE_JPEG_QUALITY,
                80
            ]
        )



        if not success:

            continue



        frame_bytes = buffer.tobytes()



        try:

            print("Streaming frame...")
            yield (

                b"--frame\r\n"

                b"Content-Type: image/jpeg\r\n\r\n"

                +
                frame_bytes

                +
                b"\r\n"

            )


        except GeneratorExit:


            break
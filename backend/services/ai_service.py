import threading

from ai.main import main


class AIService:

    def __init__(self):
        self.thread = None
        self.running = False
        self.stop_event = None

    def start(self):

        if self.running:
            return {
                "status": "already_running"
            }

        self.stop_event = threading.Event()

        self.thread = threading.Thread(
            target=main,
            args=(self.stop_event,),
            daemon=True
        )

        self.thread.start()

        self.running = True

        return {
            "status": "AI Started"
        }

    def stop(self):

        print("STOP CALLED")

        if not self.running:
            return {
                "status": "AI not running"
            }

        self.stop_event.set()

        print("STOP EVENT SET")

        if self.thread:
            self.thread.join()

        print("THREAD JOINED")

        self.running = False

        print("RUNNING = FALSE")

        return {
            "status": "AI Stopped"
        }

    def status(self):

        return {
            "running": self.running
        }


ai_service = AIService()
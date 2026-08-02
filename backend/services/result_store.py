from datetime import datetime


class ResultStore:

    def __init__(self):

        self.latest_result = {

            "risk_level": "LOW",

            "violations": [],

            "detections": [],

            "alert": None,

            "timestamp": None
        }


    def update(self, data):

        data["timestamp"] = datetime.now().isoformat()

        self.latest_result = data



    def get(self):

        return self.latest_result



result_store = ResultStore()
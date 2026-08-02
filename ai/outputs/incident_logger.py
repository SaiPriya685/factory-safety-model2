"""
incident_logger.py

Stores factory safety incidents.
"""


import json
import os
import uuid

from datetime import datetime

from ai.utils.logger import Logger



class IncidentLogger:



    def __init__(self):


        self.logger = Logger.get_logger(
            "IncidentLogger"
        )


        self.folder = (
            "ai/outputs/incidents"
        )


        self.file = (
            f"{self.folder}/incidents.json"
        )


        # seconds before same incident can appear again
        self.cooldown_seconds = 60



        os.makedirs(
            self.folder,
            exist_ok=True
        )



        if not os.path.exists(self.file):

            with open(
                self.file,
                "w"
            ) as f:

                json.dump(
                    [],
                    f,
                    indent=4
                )



        self.logger.info(
            "Incident logger initialized."
        )





    def load_incidents(self):


        with open(
            self.file,
            "r"
        ) as f:

            return json.load(f)





    def get_violation_signature(
        self,
        violations
    ):


        """
        Creates unique violation identity.

        Example:

        [
          Fire Detected,
          Missing Helmet
        ]

        becomes:

        Fire Detected|Missing Helmet
        """


        types = sorted(
            [
                v["type"]
                for v in violations
            ]
        )


        return "|".join(types)





    def is_duplicate(
        self,
        incident
    ):


        incidents = self.load_incidents()



        if not incidents:

            return False



        current_time = datetime.strptime(
            incident["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )



        new_signature = (
            self.get_violation_signature(
                incident["violations"]
            )
        )



        for old in reversed(incidents):


            old_time = datetime.strptime(
                old["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )



            difference = (
                current_time-old_time
            ).total_seconds()



            if difference > self.cooldown_seconds:

                break



            old_signature = (
                self.get_violation_signature(
                    old["violations"]
                )
            )



            if old_signature == new_signature:


                return True



        return False





    def save(
        self,
        alert,
        analysis,
        risk=None
    ):



        violations = analysis.get(
            "violations",
            []
        )



        # no violations = no incident

        if not violations:

            return None


        incident = {

    "incident_id":
        str(uuid.uuid4())[:8],

    "timestamp":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

    "location":
        "Factory Floor",

    "status":
        "OPEN",

    "alert":
        alert,

    "risk":
        risk if risk else {},

    "violations":
        analysis.get(
            "violations",
            []
        ),

    "detections":
        analysis.get(
            "detections",
            []
        ),

}

        





        if self.is_duplicate(
            incident
        ):



            self.logger.info(
                "Duplicate incident ignored."
            )


            return None





        incidents = self.load_incidents()



        incidents.append(
            incident
        )



        with open(
            self.file,
            "w"
        ) as f:


            json.dump(
                incidents,
                f,
                indent=4
            )



        self.logger.warning(
            "Safety incident saved."
        )



        return incident
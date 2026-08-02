"""
alert_manager.py

Handles factory safety alerts.
"""


from datetime import datetime

from ai.utils.logger import Logger



class AlertManager:


    def __init__(self):

        self.logger = Logger.get_logger(
            "AlertManager"
        )

        self.logger.info(
            "Alert manager initialized."
        )



    def generate_alert(
        self,
        risk_data
    ):


        level = risk_data.get(
            "risk_level",
            "LOW"
        )


        score = risk_data.get(
            "risk_score",
            0
        )


        violations = risk_data.get(
            "violations",
            []
        )


        reasons = risk_data.get(
            "risk_reasons",
            []
        )


        action = risk_data.get(
            "recommended_action",
            "Monitor safety condition"
        )



        alert = {


            "time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),



            "risk_level":
            level,



            "risk_score":
            score,



            "violations":
            violations,



            "reasons":
            reasons,



            "recommended_action":
            action,



            "message":
            self.get_message(
                level,
                violations
            )

        }



        if level in [
            "CRITICAL",
            "HIGH"
        ]:


            self.logger.warning(
                alert["message"]
            )


        else:


            self.logger.info(
                alert["message"]
            )



        return alert





    def get_message(
        self,
        level,
        violations
    ):



        if violations:


            violation_names = [

                v["type"]

                for v in violations

            ]


            if level == "CRITICAL":


                return (

                    "🚨 CRITICAL ALERT | "

                    "Emergency risk detected: "

                    +
                    ", ".join(
                        violation_names
                    )

                )



            elif level == "HIGH":


                return (

                    "⚠️ HIGH RISK ALERT | "

                    +
                    ", ".join(
                        violation_names
                    )

                )



            elif level == "MEDIUM":


                return (

                    "⚠️ Safety warning: "

                    +
                    ", ".join(
                        violation_names
                    )

                )



        messages = {


            "LOW":

            "Normal operation. No safety threat detected.",



            "MEDIUM":

            "Safety condition requires monitoring.",



            "HIGH":

            "Immediate supervisor attention required.",



            "CRITICAL":

            "Emergency response required immediately."

        }



        return messages.get(
            level,
            "Unknown risk level"
        )
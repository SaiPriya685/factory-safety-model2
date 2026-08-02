"""
Risk Engine

Calculates factory safety risk
based on detected violations.
"""


from ai.utils.logger import Logger



class RiskEngine:


    def __init__(self):

        self.logger = Logger.get_logger(
            "RiskEngine"
        )


        self.logger.info(
            "Risk engine initialized."
        )



    def calculate(self, analysis):


        violations = analysis.get(
            "violations",
            []
        )


        risk_score = 0


        reasons = []



        for violation in violations:


            severity = violation["severity"]

            confidence = violation.get(
                "confidence",
                0.5
            )


            # Severity weights

            if severity == "CRITICAL":

                weight = 80


            elif severity == "HIGH":

                weight = 50


            elif severity == "MEDIUM":

                weight = 25


            else:

                weight = 10



            # confidence based score

            score = int(
                weight * confidence
            )


            risk_score += score



            reasons.append(
                violation["type"]
            )



        # Maximum score

        risk_score = min(
            risk_score,
            100
        )



        # Risk classification

        if risk_score >= 75:


            risk_level = "CRITICAL"



            action = (
                "Immediate evacuation "
                "and emergency response required"
            )



        elif risk_score >= 45:


            risk_level = "HIGH"



            action = (
                "Supervisor attention required"
            )



        elif risk_score > 0:


            risk_level = "MEDIUM"



            action = (
                "Monitor safety condition"
            )



        else:


            risk_level = "LOW"



            action = (
                "Normal operation"
            )



        result = {


            "risk_score":
            risk_score,


            "risk_level":
            risk_level,


            "violations":
            violations,


            "risk_reasons":
            reasons,


            "recommended_action":
            action


        }



        return result
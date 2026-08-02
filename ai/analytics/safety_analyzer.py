"""
Safety Analyzer

Converts AI detections into
factory safety violations.
"""


from ai.utils.logger import Logger


class SafetyAnalyzer:


    def __init__(self):

        self.logger = Logger.get_logger(
            "SafetyAnalyzer"
        )

        self.history = []

        self.required_frames = 3


        self.logger.info(
            "Safety analyzer initialized."
        )



    def analyze(self, detections):


        violations = []


        detected_names = {
            item["name"]
            for item in detections
        }



        # ---------------------------------
        # PPE conflict handling
        # ---------------------------------

        has_helmet = (
            "helmet" in detected_names
        )


        has_no_helmet = (
            "no_helmet" in detected_names
        )


        has_vest = (
            "safety_vest" in detected_names
        )


        has_no_vest = (
            "no_vest" in detected_names
        )



        for item in detections:


            name = item["name"]

            confidence = item["confidence"]



            # -----------------------------
            # Helmet violation
            # -----------------------------

            if name == "no_helmet":


                # Ignore if helmet is detected
                if has_helmet:

                    continue



                violations.append(
                    {
                        "type": "Missing Helmet",

                        "severity": "HIGH",

                        "confidence": confidence
                    }
                )



            # -----------------------------
            # Vest violation
            # -----------------------------

            elif name == "no_vest":


                # Ignore if safety vest exists
                if has_vest:

                    continue



                violations.append(
                    {
                        "type": "Missing Safety Vest",

                        "severity": "MEDIUM",

                        "confidence": confidence
                    }
                )



            # -----------------------------
            # Fire
            # -----------------------------

            elif name == "fire":


                violations.append(
                    {
                        "type": "Fire Detected",

                        "severity": "CRITICAL",

                        "confidence": confidence
                    }
                )



            # -----------------------------
            # Smoke
            # -----------------------------

            elif name == "smoke":


                violations.append(
                    {
                        "type": "Smoke Detected",

                        "severity": "HIGH",

                        "confidence": confidence
                    }
                )



        # Remove duplicate violation types
        violations = self.remove_duplicates(
            violations
        )


        # Confirm violation across frames
        confirmed = self.confirm_violations(
            violations
        )


        if confirmed:

            self.logger.warning(
                f"Confirmed violations: {confirmed}"
            )


        return {


            "detections": detections,


            "violations": confirmed

        }




    def confirm_violations(
        self,
        violations
    ):


        current = [
            v["type"]
            for v in violations
        ]



        self.history.append(
            current
        )



        if len(self.history) > self.required_frames:

            self.history.pop(0)



        # Wait until enough frames collected
        if len(self.history) < self.required_frames:

            return []



        common = set(
            self.history[0]
        )



        for item in self.history:

            common &= set(item)



        confirmed = []



        for violation in violations:


            if violation["type"] in common:

                confirmed.append(
                    violation
                )



        return confirmed




    def remove_duplicates(
        self,
        violations
    ):


        unique = {}



        for violation in violations:


            violation_type = violation["type"]



            if violation_type not in unique:


                unique[violation_type] = violation



            else:


                if (
                    violation["confidence"]
                    >
                    unique[violation_type]["confidence"]
                ):


                    unique[violation_type] = violation



        return list(
            unique.values()
        )
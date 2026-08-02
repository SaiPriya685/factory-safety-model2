from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_incident_report(incident):


    filename = (
        f"incident_report_{incident.id}.pdf"
    )


    filepath = (
        f"reports/{filename}"
    )


    doc = SimpleDocTemplate(
        filepath,
        pagesize=letter
    )


    styles = getSampleStyleSheet()


    content = []


    title = Paragraph(
        "AI Factory Safety Incident Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(1,20)
    )


    details = f"""

    <b>Incident ID:</b> {incident.id}<br/>

    <b>Date:</b> {incident.created_at}<br/>

    <b>Location:</b> {incident.location}<br/>

    <b>Violation:</b> {incident.violation}<br/>

    <b>Severity:</b> {incident.severity}<br/>

    """


    content.append(
        Paragraph(
            details,
            styles["Normal"]
        )
    )


    content.append(
        Spacer(1,20)
    )


    # AI Recommendations

    if incident.violation == "Fire Detected":

        recommendation = """
        <b>AI Recommendation:</b><br/>
        Immediate emergency response required.<br/>
        Activate fire safety protocols.<br/>
        Inspect affected factory area.
        """


    elif incident.violation == "Missing Helmet":

        recommendation = """
        <b>AI Recommendation:</b><br/>
        Worker must wear required PPE.<br/>
        Stop unsafe activity until compliance.
        """


    else:

        recommendation = """
        <b>AI Recommendation:</b><br/>
        Review safety conditions immediately.
        """


    content.append(
        Paragraph(
            recommendation,
            styles["Normal"]
        )
    )


    doc.build(content)


    return filepath
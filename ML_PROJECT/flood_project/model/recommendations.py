"""
Safety recommendations module for Flood Prediction Disaster System.
Provides concise, citizen-friendly actionable tips categorized by risk level.
"""

RECOMMENDATIONS = {
    "Safe": [
        "No flood risk right now.",
        "Keep an eye on weather updates.",
        "No action needed today.",
    ],
    "Warning": [
        "Avoid low-lying areas.",
        "Keep emergency contacts ready.",
        "Move valuables to higher ground.",
        "Watch for official alerts.",
    ],
    "Danger": [
        "Evacuate low-lying areas now.",
        "Avoid contact with flood water.",
        "Keep an emergency kit ready.",
        "Follow official evacuation routes.",
        "Call for help if trapped.",
    ],
}

def get_recommendation(risk_level: str) -> list[str]:
    """Return list of short safety tips for the specified risk level."""
    return RECOMMENDATIONS.get(risk_level, ["No recommendation available."])

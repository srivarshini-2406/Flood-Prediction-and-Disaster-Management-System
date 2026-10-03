"""
Emergency Information Module for Flood Prediction Disaster System.

NOTE: This is representative demo data, not a live API.
A real deployment would use a live maps API (e.g., Google Maps Platform / GPS)
for real-time nearest-facility lookup based on the user's exact geolocation.
"""

# Static emergency contacts and facilities for all 8 supported Tamil Nadu districts
EMERGENCY_INFO = {
    "Chennai": {
        "helpline": "1077 (Tamil Nadu State Disaster Management Helpline)",
        "ambulance": "108",
        "hospital": "Government General Hospital (Rajiv Gandhi GGH), Chennai",
        "shelter": "Contact district collectorate for nearest relief shelter",
    },
    "Coimbatore": {
        "helpline": "1077 (Tamil Nadu State Disaster Management Helpline)",
        "ambulance": "108",
        "hospital": "Coimbatore Medical College Hospital (CMCH), Coimbatore",
        "shelter": "Contact district collectorate for nearest relief shelter",
    },
    "Madurai": {
        "helpline": "1077 (Tamil Nadu State Disaster Management Helpline)",
        "ambulance": "108",
        "hospital": "Government Rajaji Hospital (GRH), Madurai",
        "shelter": "Contact district collectorate for nearest relief shelter",
    },
    "Tiruchirappalli": {
        "helpline": "1077 (Tamil Nadu State Disaster Management Helpline)",
        "ambulance": "108",
        "hospital": "Mahatma Gandhi Memorial Government Hospital, Trichy",
        "shelter": "Contact district collectorate for nearest relief shelter",
    },
    "Salem": {
        "helpline": "1077 (Tamil Nadu State Disaster Management Helpline)",
        "ambulance": "108",
        "hospital": "Government Mohan Kumaramangalam Medical College Hospital, Salem",
        "shelter": "Contact district collectorate for nearest relief shelter",
    },
    "Tirunelveli": {
        "helpline": "1077 (Tamil Nadu State Disaster Management Helpline)",
        "ambulance": "108",
        "hospital": "Tirunelveli Medical College Hospital (TVMCH), Tirunelveli",
        "shelter": "Contact district collectorate for nearest relief shelter",
    },
    "Erode": {
        "helpline": "1077 (Tamil Nadu State Disaster Management Helpline)",
        "ambulance": "108",
        "hospital": "Government Headquarters Hospital (GH), Erode",
        "shelter": "Contact district collectorate for nearest relief shelter",
    },
    "Vellore": {
        "helpline": "1077 (Tamil Nadu State Disaster Management Helpline)",
        "ambulance": "108",
        "hospital": "Government Vellore Medical College Hospital (GVMCH), Vellore",
        "shelter": "Contact district collectorate for nearest relief shelter",
    },
}

def get_emergency_info(district: str) -> dict:
    """Return emergency contact information for the given district."""
    return EMERGENCY_INFO.get(
        district,
        {
            "helpline": "1077 (Tamil Nadu State Disaster Management Helpline)",
            "ambulance": "108",
            "hospital": "Nearest Government District Hospital",
            "shelter": "Contact district collectorate for nearest relief shelter",
        },
    )

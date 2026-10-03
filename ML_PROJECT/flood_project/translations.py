"""
Multilingual Translations Module for Flood Prediction Disaster System.
Provides full English ('en') and Tamil ('ta') string maps for all UI components.
"""

TRANSLATIONS = {
    "en": {
        # App & Navigation
        "home_title": "Flood Prediction System",
        "home_tagline": "Know your flood risk in seconds and stay safe.",
        "nav_home": "Home",
        "nav_prediction": "Prediction",
        "nav_analytics": "Analytics",
        "nav_overview": "Area Overview",
        "nav_about": "About",
        "nav_emergency": "Emergency Info",
        "lang_selector_label": "Language / மொழி",

        # Home Navigation Cards
        "card_predict_title": "Predict Flood Risk",
        "card_predict_desc": "Enter your area readings to instantly check risk level",
        "card_analytics_title": "Disaster Analytics",
        "card_analytics_desc": "Explore historical patterns and weather trends",
        "card_emergency_title": "Emergency Directory",
        "card_emergency_desc": "Access 24/7 disaster helplines and hospital contacts",

        # Prediction Form & Inputs
        "prediction_header": "Check Your Area Flood Risk",
        "prediction_subheader": "Fill in local environmental measurements below to assess real-time risk level.",
        "select_district": "Select District",
        "rainfall_label": "Rainfall (mm)",
        "water_level_label": "Water Level (m)",
        "soil_moisture_label": "Soil Moisture (%)",
        "humidity_label": "Humidity (%)",
        "predict_button": "Check Flood Risk",
        "validation_error_negative": "Input values cannot be negative. Please enter valid numbers.",
        
        # Risk Labels & Results
        "risk_safe": "Safe",
        "risk_warning": "Warning",
        "risk_danger": "Danger",
        "risk_level_label": "Assessed Flood Risk Level",
        "confidence_label": "Model Confidence",
        "probability_breakdown": "Class Probability Breakdown",
        "probability_chart_title": "Confidence Distribution Across Classes",

        # Safety & Emergency Info
        "safety_tips_header": "Safety Tips & Recommendations",
        "emergency_header": "Emergency Information & Contacts",
        "helpline_label": "Disaster Helpline",
        "ambulance_label": "Ambulance",
        "hospital_label": "Nearest Government Hospital",
        "shelter_label": "Relief Shelter Info",
        "emergency_demo_note": "Representative demo data. Real-time deployment integrates GPS and live mapping APIs for the nearest facility.",

        # Safety Tips Items
        "tip_safe_1": "No flood risk right now.",
        "tip_safe_2": "Keep an eye on weather updates.",
        "tip_safe_3": "No action needed today.",
        "tip_warning_1": "Avoid low-lying areas.",
        "tip_warning_2": "Keep emergency contacts ready.",
        "tip_warning_3": "Move valuables to higher ground.",
        "tip_warning_4": "Watch for official alerts.",
        "tip_danger_1": "Evacuate low-lying areas now.",
        "tip_danger_2": "Avoid contact with flood water.",
        "tip_danger_3": "Keep an emergency kit ready.",
        "tip_danger_4": "Follow official evacuation routes.",
        "tip_danger_5": "Call for help if trapped.",

        # Analytics Page
        "analytics_title": "Disaster Analytics & Environmental Patterns",
        "analytics_subtitle": "Statistical exploration of environmental parameters and flood vulnerability.",
        "dist_plots_header": "Environmental Feature Distributions",
        "district_risk_header": "Flood Risk Breakdown by District",
        "corr_heatmap_header": "Feature Correlation Heatmap",
        "correlation_intro": "This shows how strongly two factors move together.",
        "corr_explanation": "{feat1} and {feat2} show the strongest correlation, rising together in flood-prone conditions.",
        "corr_caption": "Correlation coefficient: {val:.2f}",
        "feature_Rainfall_mm": "Rainfall (mm)",
        "feature_WaterLevel_m": "Water Level (m)",
        "feature_SoilMoisture_percent": "Soil Moisture (%)",
        "feature_Humidity_percent": "Humidity (%)",
        "feature_District_encoded": "District Code",

        # Area Overview Page
        "overview_title": "Area Overview & Citizen Summary",
        "overview_subtitle": "Non-technical snapshot of current safety status and community readiness.",
        "recent_prediction_header": "Your Latest Assessment",
        "no_prediction_yet": "No assessment conducted yet. Go to the Prediction page to test your area readings!",
        "district_risk_snapshot_header": "Regional Risk Snapshot",
        "areas_at_risk_axis": "Areas at risk today",
        "active_checklist_header": "Citizen Safety Checklist",
        "checklist_intro": "Essential actions recommended for your current risk status:",
        "district_label": "District",
        "status_label": "Status",

        # About Page
        "about_title": "About Flood Prediction Disaster System",
        "problem_statement_header": "Problem Statement",
        "problem_statement_text": "Floods cause severe socio-economic devastation, displacement, and loss of life across vulnerable districts in Tamil Nadu. Traditional alerts often reach citizens late or in complex formats. This system bridges the gap by providing instant, localized, AI-powered risk classification designed directly for citizens.",
        "objectives_header": "Key Objectives",
        "obj_1": "Provide instant, accessible, non-technical flood risk categorization (Safe, Warning, Danger).",
        "obj_2": "Deliver actionable, concise safety instructions and district-specific emergency contacts.",
        "obj_3": "Support bilingual interaction (English & Tamil) for regional accessibility.",
        "obj_4": "Visualize meteorological and hydrological risk patterns interactively.",
        "workflow_header": "End-to-End System Workflow",
        "workflow_steps": "1. User Input → 2. Input Validation → 3. StandardScaler Normalization → 4. Keras Neural Network Inference → 5. Risk & Confidence Calculation → 6. Bilingual Recommendations & Emergency Dispatch → 7. Area Overview Log",
        "tech_stack_header": "Technology Stack",
        "model_arch_header": "Deep Learning Architecture",
        "model_arch_details": "• Architecture: Keras Sequential Neural Network\n• Input Layer: 5 Features (Encoded District, Rainfall, Water Level, Soil Moisture, Humidity)\n• Hidden Layer 1: Dense (64 units, ReLU) + Dropout (0.2)\n• Hidden Layer 2: Dense (32 units, ReLU) + Dropout (0.2)\n• Output Layer: Dense (3 units, Softmax for Safe / Warning / Danger)\n• Optimization: Adam Optimizer, Categorical Crossentropy Loss",
        "future_scope_header": "Future Scope & Real-World Integration",
        "future_scope_details": "• Live IoT sensor integration for automated water level telemetry\n• Real-time OpenWeather / IMD meteorological API feeds\n• SMS and WhatsApp broadcast emergency warning system\n• GPS-based live routing to nearest rescue shelters & hospitals\n• Mobile native application for offline safety caches\n• Generative AI for customized local language voice alerts",
    },
    "ta": {
        # App & Navigation
        "home_title": "வெள்ள முன்னறிவிப்பு அமைப்பு",
        "home_tagline": "உங்கள் வெள்ள ஆபத்தை சில நொடிகளில் அறியுங்கள்.",
        "nav_home": "முகப்பு",
        "nav_prediction": "கணிப்பு",
        "nav_analytics": "பகுப்பாய்வு",
        "nav_overview": "பகுதி நிலவரம்",
        "nav_about": "பற்றி",
        "nav_emergency": "அவசர தகவல்",
        "lang_selector_label": "மொழி / Language",

        # Home Navigation Cards
        "card_predict_title": "வெள்ள ஆபத்தை கணிக்கவும்",
        "card_predict_desc": "உங்கள் பகுதி அளவீடுகளை உள்ளிட்டு ஆபத்து அளவை உடனே சரிபார்க்கவும்",
        "card_analytics_title": "பேரிடர் பகுப்பாய்வு",
        "card_analytics_desc": "வரலாற்று போக்குகள் மற்றும் வானிலை வடிவங்களை காண்க",
        "card_emergency_title": "அவசர உதவி எண்கள்",
        "card_emergency_desc": "24/7 பேரிடர் உதவி எண்கள் மற்றும் நிவாரண தகவல்களை அணுகவும்",

        # Prediction Form & Inputs
        "prediction_header": "உங்கள் பகுதி வெள்ள அபாயத்தை சரிபார்க்கவும்",
        "prediction_subheader": "நேரடி ஆபத்து அளவை மதிப்பிட கீழே உள்ள சுற்றுச்சூழல் அளவீடுகளை உள்ளிடவும்.",
        "select_district": "மாவட்டத்தை தேர்ந்தெடுக்கவும்",
        "rainfall_label": "மழைவீழ்ச்சி (மி.மீ)",
        "water_level_label": "நீர் மட்டம் (மீ)",
        "soil_moisture_label": "மண் ஈரப்பதம் (%)",
        "humidity_label": "ஈரப்பதம் (%)",
        "predict_button": "வெள்ள ஆபத்தை சரிபார்க்கவும்",
        "validation_error_negative": "உள்ளீட்டு மதிப்புகள் எதிர்மறையாக இருக்கக்கூடாது. சரியான எண்களை உள்ளிடவும்.",

        # Risk Labels & Results
        "risk_safe": "பாதுகாப்பானது",
        "risk_warning": "எச்சரிக்கை",
        "risk_danger": "ஆபத்து",
        "risk_level_label": "மதிப்பிடப்பட்ட வெள்ள அபாய நிலை",
        "confidence_label": "மாதிரி நம்பிக்கை",
        "probability_breakdown": "விரிவான நிகழ்தகவு விவரம்",
        "probability_chart_title": "வகுப்புகளுக்கான நிகழ்தகவு பரவல்",

        # Safety & Emergency Info
        "safety_tips_header": "பாதுகாப்பு குறிப்புகள் & வழிகாட்டுதல்கள்",
        "emergency_header": "அவசர தகவல் & தொடர்பு எண்கள்",
        "helpline_label": "பேரிடர் உதவி எண்",
        "ambulance_label": "ஆம்புலன்ஸ்",
        "hospital_label": "அருகிலுள்ள அரசு மருத்துவமனை",
        "shelter_label": "நிவாரண தங்குமிட தகவல்",
        "emergency_demo_note": "மாதிரி தகவல் மட்டுமே. நேரடி அமைப்பில் ஜிபிஎஸ் மற்றும் நேரடி வரைபடங்கள் மூலம் அருகிலுள்ள வசதிகள் காண்பிக்கப்படும்.",

        # Safety Tips Items
        "tip_safe_1": "தற்போது வெள்ள அபாயம் இல்லை.",
        "tip_safe_2": "வானிலை அறிவிப்புகளை கவனிக்கவும்.",
        "tip_safe_3": "இன்று அவசர நடவடிக்கை தேவையில்லை.",
        "tip_warning_1": "தாழ்வான பகுதிகளை தவிர்க்கவும்.",
        "tip_warning_2": "அவசர உதவி எண்களை தயாராக வைக்கவும்.",
        "tip_warning_3": "பொருட்களை உயரமான இடத்திற்கு மாற்றவும்.",
        "tip_warning_4": "அதிகாரப்பூர்வ எச்சரிக்கைகளை கவனிக்கவும்.",
        "tip_danger_1": "தாழ்வான பகுதிகளை உடனே காலி செய்யவும்.",
        "tip_danger_2": "வெள்ள நீருடன் தொடர்பை தவிர்க்கவும்.",
        "tip_danger_3": "அவசர முதலுதவி பெட்டியை தயாராக வைக்கவும்.",
        "tip_danger_4": "அரசு வெளியேற்ற வழிகளை பின்பற்றவும்.",
        "tip_danger_5": "சிக்கியிருந்தால் உடனே உதவிக்கு அழைக்கவும்.",

        # Analytics Page
        "analytics_title": "பேரிடர் பகுப்பாய்வு & சுற்றுச்சூழல் வடிவங்கள்",
        "analytics_subtitle": "சுற்றுச்சூழல் காரணிகள் மற்றும் வெள்ள பாதிப்பு குறித்த புள்ளியியல் ஆய்வு.",
        "dist_plots_header": "சுற்றுச்சூழல் காரணிகளின் பரவல்",
        "district_risk_header": "மாவட்ட வாரியாக வெள்ள அபாய எண்ணிக்கை",
        "corr_heatmap_header": "காரணிகளின் தொடர்பு வரைபடம் (Heatmap)",
        "correlation_intro": "இரண்டு காரணிகள் எவ்வளவு நெருக்கமாக மாறுகின்றன என்பதை இது காட்டுகிறது.",
        "corr_explanation": "{feat1} மற்றும் {feat2} வலுவான தொடர்பைக் கொண்டுள்ளன, வெள்ளம் ஏற்படும் சூழ்நிலைகளில் இரண்டும் ஒன்றாக உயர்கின்றன.",
        "corr_caption": "தொடர்பு குணகம் (Correlation): {val:.2f}",
        "feature_Rainfall_mm": "மழைவீழ்ச்சி (மி.மீ)",
        "feature_WaterLevel_m": "நீர் மட்டம் (மீ)",
        "feature_SoilMoisture_percent": "மண் ஈரப்பதம் (%)",
        "feature_Humidity_percent": "ஈரப்பதம் (%)",
        "feature_District_encoded": "மாவட்ட குறியீடு",

        # Area Overview Page
        "overview_title": "பகுதி நிலவரம் & குடிமக்கள் சுருக்கம்",
        "overview_subtitle": "தற்போதைய பாதுகாப்பு நிலை மற்றும் சமூக தயார்நிலை குறித்த எளிய பார்வை.",
        "recent_prediction_header": "உங்கள் சமீபத்திய மதிப்பீடு",
        "no_prediction_yet": "இன்னும் மதிப்பீடு செய்யப்படவில்லை. உங்கள் பகுதி அளவீடுகளை சோதிக்க கணிப்பு பக்கத்திற்கு செல்லவும்!",
        "district_risk_snapshot_header": "பிராந்திய அபாய சுருக்கம்",
        "areas_at_risk_axis": "இன்றைய அபாயத்தில் உள்ள பகுதிகள்",
        "active_checklist_header": "குடிமக்கள் பாதுகாப்பு சரிபார்ப்பு பட்டியல்",
        "checklist_intro": "உங்கள் தற்போதைய அபாய நிலைக்கு பரிந்துரைக்கப்படும் முக்கிய நடவடிக்கைகள்:",
        "district_label": "மாவட்டம்",
        "status_label": "நிலை",

        # About Page
        "about_title": "வெள்ள முன்னறிவிப்பு அமைப்பு பற்றி",
        "problem_statement_header": "சிக்கல் அறிக்கை",
        "problem_statement_text": "வெள்ளம் தமிழ்நாட்டின் பாதிக்கப்படக்கூடிய மாவட்டங்களில் கடுமையான சமூக-பொருளாதார சேதத்தையும் மனித உயிரிழப்பையும் ஏற்படுத்துகிறது. வழக்கமான எச்சரிக்கைகள் பெரும்பாலும் தாமதமாகவோ அல்லது சிக்கலான வடிவிலோ பொதுமக்களை சென்றடைகின்றன. இந்த அமைப்பு எளிய குடிமக்களுக்காக நேரடியாக வடிவமைக்கப்பட்ட உடனடி, உள்ளூர்மயமாக்கப்பட்ட AI எச்சரிக்கைகளை வழங்குகிறது.",
        "objectives_header": "முக்கிய நோக்கங்கள்",
        "obj_1": "உடனடி, எளிய வெள்ள அபாய வகைப்பாட்டை வழங்குதல் (பாதுகாப்பானது, எச்சரிக்கை, ஆபத்து).",
        "obj_2": "செயல்படக்கூடிய பாதுகாப்பு குறிப்புகள் மற்றும் மாவட்ட அவசர உதவி எண்களை வழங்குதல்.",
        "obj_3": "தமிழ் மற்றும் ஆங்கிலத்தில் இருமொழி ஆதரவு வழங்குதல்.",
        "obj_4": "வானிலை மற்றும் நீரியல் தரவுகளை வரைபடங்கள் மூலம் எளிமையாக விளக்குதல்.",
        "workflow_header": "கணினி பணிப்பாய்வு",
        "workflow_steps": "1. பயனர் உள்ளீடு → 2. உள்ளீடு சரிபார்ப்பு → 3. தரவு இயல்பாக்கம் (StandardScaler) → 4. நியூரல் நெட்வொர்க் கணிப்பு → 5. ஆபத்து & நம்பிக்கை கணக்கீடு → 6. இருமொழி பாதுகாப்பு & அவசர வழிகாட்டுதல் → 7. பகுதி நிலவர பதிவு",
        "tech_stack_header": "தொழில்நுட்ப கட்டமைப்பு",
        "model_arch_header": "ஆழ்ந்த கற்றல் கட்டமைப்பு (Deep Learning)",
        "model_arch_details": "• கட்டமைப்பு: Keras Sequential Neural Network\n• உள்ளீட்டு அடுக்கு: 5 காரணிகள் (மாவட்டம், மழை, நீர் மட்டம், மண் ஈரப்பதம், ஈரப்பதம்)\n• மறைக்கப்பட்ட அடுக்கு 1: Dense (64 அலகுகள், ReLU) + Dropout (0.2)\n• மறைக்கப்பட்ட அடுக்கு 2: Dense (32 அலகுகள், ReLU) + Dropout (0.2)\n• வெளியீட்டு அடுக்கு: Dense (3 அலகுகள், Softmax)\n• உகப்பாக்கம்: Adam Optimizer, Categorical Crossentropy Loss",
        "future_scope_header": "எதிர்கால விரிவாக்கம்",
        "future_scope_details": "• நேரடி IoT நீர்மட்ட உணரிகள் இணைப்பு\n• நேரடி வானிலை API இணைப்பு\n• அவசர SMS மற்றும் WhatsApp எச்சரிக்கை அமைப்பு\n• ஜிபிஎஸ் அடிப்படையிலான உடனடி தங்குமிட வழிகாட்டுதல்\n• மொபைல் செயலி உருவாக்கம்\n• பிராந்திய மொழி குரல் எச்சரிக்கைகள்",
    },
}

def get_text(key: str, lang: str = "en") -> str:
    """Retrieve translated text by key with fallback to English and key name."""
    lang_dict = TRANSLATIONS.get(lang, TRANSLATIONS["en"])
    return lang_dict.get(key, TRANSLATIONS["en"].get(key, key))

def get_translated_risk(risk_en: str, lang: str = "en") -> str:
    """Return localized risk title (Safe / Warning / Danger)."""
    mapping = {
        "Safe": "risk_safe",
        "Warning": "risk_warning",
        "Danger": "risk_danger",
    }
    key = mapping.get(risk_en, "risk_safe")
    return get_text(key, lang)

def get_translated_tips(risk_en: str, lang: str = "en") -> list[str]:
    """Return localized list of concise safety tips."""
    if risk_en == "Safe":
        return [
            get_text("tip_safe_1", lang),
            get_text("tip_safe_2", lang),
            get_text("tip_safe_3", lang),
        ]
    elif risk_en == "Warning":
        return [
            get_text("tip_warning_1", lang),
            get_text("tip_warning_2", lang),
            get_text("tip_warning_3", lang),
            get_text("tip_warning_4", lang),
        ]
    elif risk_en == "Danger":
        return [
            get_text("tip_danger_1", lang),
            get_text("tip_danger_2", lang),
            get_text("tip_danger_3", lang),
            get_text("tip_danger_4", lang),
            get_text("tip_danger_5", lang),
        ]
    return [get_text("tip_safe_1", lang)]

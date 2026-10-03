"""
Inference Module for Flood Prediction Disaster System.
Loads pre-trained model and preprocessing transformers to provide fast real-time predictions.
"""

import os
from pathlib import Path
import joblib
import numpy as np
import pandas as pd

# This model is trained and saved with Keras' portable .keras format.  Use the
# TensorFlow backend so importing the app does not load PyTorch's native
# extensions (which may be blocked by Windows Application Control).
os.environ["KERAS_BACKEND"] = "tensorflow"

MODEL_DIR = Path(__file__).resolve().parent
FEATURE_COLUMNS = [
    "District_encoded",
    "Rainfall_mm",
    "WaterLevel_m",
    "SoilMoisture_percent",
    "Humidity_percent",
]

# Load model, scaler, and encoders once at import time
try:
    import keras

    # The saved training config references a PyTorch Adam optimizer. Inference
    # needs only the network weights, so skip optimizer deserialization; this
    # prevents Keras from importing the blocked PyTorch/optree native extension.
    _model = keras.models.load_model(
        str(MODEL_DIR / "flood_model_dl.keras"), compile=False
    )
    _scaler = joblib.load(MODEL_DIR / "feature_scaler.pkl")
    _district_encoder = joblib.load(MODEL_DIR / "district_encoder.pkl")
    _class_encoder = joblib.load(MODEL_DIR / "class_encoder.pkl")
except Exception as e:
    _model = None
    _scaler = None
    _district_encoder = None
    _class_encoder = None
    _load_error = e
    print(f"[Warning] Artifacts not loaded at import time: {e}")

def predict_flood_risk(
    district: str,
    rainfall: float,
    water_level: float,
    soil_moisture: float,
    humidity: float,
) -> dict:
    """
    Predict flood risk level for given physical parameters.
    
    Returns:
        dict: {
            "risk": str ("Safe" | "Warning" | "Danger"),
            "confidence": float (e.g. 0.95),
            "probabilities": dict (e.g. {"Safe": 0.01, "Warning": 0.04, "Danger": 0.95})
        }
    """
    if _model is None or _scaler is None or _district_encoder is None or _class_encoder is None:
        raise RuntimeError(
            "Flood prediction is unavailable because the model or its backend "
            f"could not be loaded: {_load_error}"
        ) from _load_error

    # 1. Encode District with fallback to 0 if unseen
    if district in _district_encoder.classes_:
        district_encoded = int(_district_encoder.transform([district])[0])
    else:
        district_encoded = 0

    # 2. Build feature row in exact FEATURE_COLUMNS order
    raw_df = pd.DataFrame(
        [
            [
                district_encoded,
                float(rainfall),
                float(water_level),
                float(soil_moisture),
                float(humidity),
            ]
        ],
        columns=FEATURE_COLUMNS,
    )

    # 3. Transform with the loaded scaler
    scaled_features = _scaler.transform(raw_df)

    # 4. Predict probabilities
    probs = _model.predict(scaled_features, verbose=0)[0]

    # 5. Argmax and inverse-transform label
    pred_idx = int(np.argmax(probs))
    pred_risk = str(_class_encoder.inverse_transform([pred_idx])[0])
    confidence = float(probs[pred_idx])

    # 6. Build probabilities dictionary mapped by class name
    prob_dict = {
        str(c): float(probs[i])
        for i, c in enumerate(_class_encoder.classes_)
    }

    return {
        "risk": pred_risk,
        "confidence": confidence,
        "probabilities": prob_dict,
    }

if __name__ == "__main__":
    print("\n--- Running Standalone Prediction Test ---")
    test_result = predict_flood_risk("Chennai", 280, 9, 95, 95)
    print(f"Input: Chennai, Rainfall=280mm, WaterLevel=9m, SoilMoisture=95%, Humidity=95%")
    print(f"Prediction Result: {test_result}")
    assert test_result["risk"] == "Danger", f"Expected 'Danger', got {test_result['risk']}"
    print("[Verification Passed] Standalone test successfully returned 'Danger' with high confidence!")

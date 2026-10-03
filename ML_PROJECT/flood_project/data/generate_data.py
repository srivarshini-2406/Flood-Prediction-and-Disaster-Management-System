"""
Data Generation Script for Flood Prediction Disaster System.
Generates synthetic flood risk dataset with realistic physical correlations,
controlled noise, and injected data quality anomalies (duplicates and nulls).
"""

import os
from pathlib import Path
import numpy as np
import pandas as pd

DISTRICTS = [
    "Chennai",
    "Coimbatore",
    "Madurai",
    "Tiruchirappalli",
    "Salem",
    "Tirunelveli",
    "Erode",
    "Vellore",
]

def generate_flood_data(
    base_rows: int = 500,
    seed: int = 42,
    num_duplicates: int = 8,
    num_nulls: int = 10,
) -> pd.DataFrame:
    """Generate flood risk dataset with simulated physical attributes and labels."""
    np.random.seed(seed)

    # Random generation of features
    districts = np.random.choice(DISTRICTS, size=base_rows)
    rainfall_mm = np.random.uniform(0.0, 300.0, size=base_rows)
    water_level_m = np.random.uniform(0.0, 10.0, size=base_rows)
    soil_moisture_pct = np.random.uniform(10.0, 100.0, size=base_rows)
    humidity_pct = np.random.uniform(30.0, 100.0, size=base_rows)

    # Weighted ground truth score calculation
    score = (
        0.40 * (rainfall_mm / 300.0)
        + 0.30 * (water_level_m / 10.0)
        + 0.20 * (soil_moisture_pct / 100.0)
        + 0.10 * (humidity_pct / 100.0)
    )

    # Add Gaussian noise (mean 0, std 0.05)
    noise = np.random.normal(loc=0.0, scale=0.05, size=base_rows)
    final_score = score + noise

    # Discretize into Safe, Warning, Danger classes
    flood_risk = np.where(
        final_score < 0.45,
        "Safe",
        np.where(final_score < 0.70, "Warning", "Danger"),
    )

    df = pd.DataFrame(
        {
            "District": districts,
            "Rainfall_mm": np.round(rainfall_mm, 2),
            "WaterLevel_m": np.round(water_level_m, 2),
            "SoilMoisture_percent": np.round(soil_moisture_pct, 2),
            "Humidity_percent": np.round(humidity_pct, 2),
            "FloodRisk": flood_risk,
        }
    )

    # Inject data-quality issue 1: Append duplicate rows
    dup_indices = np.random.choice(df.index, size=num_duplicates, replace=False)
    duplicates = df.loc[dup_indices].copy()
    df = pd.concat([df, duplicates], ignore_index=True)

    # Inject data-quality issue 2: Null out 10 values across numeric columns
    numeric_cols = ["Rainfall_mm", "SoilMoisture_percent", "Humidity_percent"]
    null_rows = np.random.choice(len(df), size=num_nulls, replace=False)
    null_cols = np.random.choice(numeric_cols, size=num_nulls, replace=True)

    for r_idx, col in zip(null_rows, null_cols):
        df.at[r_idx, col] = np.nan

    return df

def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Save DataFrame to CSV and print summary statistics."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[Data Generation] Dataset successfully saved to: {output_path}")
    print(f"[Data Generation] Total row count: {len(df)}")
    print(f"[Data Generation] Null counts:\n{df.isnull().sum()}")
    print(f"[Data Generation] Class distribution (including injected duplicates):\n{df['FloodRisk'].value_counts()}")

if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    out_file = script_dir / "flood_data.csv"
    data = generate_flood_data()
    save_data(data, str(out_file))

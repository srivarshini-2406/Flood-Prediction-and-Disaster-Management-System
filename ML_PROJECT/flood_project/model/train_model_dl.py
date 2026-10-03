"""
Model Training Script for Flood Prediction Disaster System.
Trains a Deep Learning model (Keras/TensorFlow/PyTorch backend) with proper preprocessing,
metrics evaluation, confusion matrix, training history visualization, and artifact serialization.
"""

import os
from pathlib import Path
import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Keep training on the same backend used by inference. This also avoids
# importing PyTorch native extensions on Windows.
os.environ["KERAS_BACKEND"] = "tensorflow"
import keras
from keras import layers
from keras.utils import to_categorical

FEATURE_COLUMNS = [
    "District_encoded",
    "Rainfall_mm",
    "WaterLevel_m",
    "SoilMoisture_percent",
    "Humidity_percent",
]
TARGET_CLASSES = ["Safe", "Warning", "Danger"]

def train_flood_model(
    data_path: str,
    output_dir: str,
    random_state: int = 42,
) -> dict:
    """Train Deep Learning model and export model artifacts and evaluation plots."""
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # 1. Load CSV
    print(f"\n--- 1. Loading Dataset from {data_path} ---")
    df = pd.read_csv(data_path)
    initial_rows = len(df)
    print(f"Loaded {initial_rows} initial rows.")

    # 2. Drop duplicates
    print("\n--- 2. Handling Duplicates ---")
    df_clean = df.drop_duplicates().copy()
    duplicates_removed = initial_rows - len(df_clean)
    print(f"Removed {duplicates_removed} duplicate rows. Remaining rows: {len(df_clean)}")

    # 3. Fill missing numeric values with column median
    print("\n--- 3. Handling Missing Values ---")
    numeric_cols = ["Rainfall_mm", "WaterLevel_m", "SoilMoisture_percent", "Humidity_percent"]
    total_missing_before = df_clean[numeric_cols].isnull().sum().sum()
    for col in numeric_cols:
        col_missing = df_clean[col].isnull().sum()
        if col_missing > 0:
            median_val = df_clean[col].median()
            df_clean[col] = df_clean[col].fillna(median_val)
            print(f"Filled {col_missing} missing values in '{col}' with median: {median_val:.2f}")
    print(f"Total missing values filled: {total_missing_before}")

    # 4. LabelEncoder on District -> District_encoded
    print("\n--- 4. Encoding Categorical Features ---")
    district_encoder = LabelEncoder()
    df_clean["District_encoded"] = district_encoder.fit_transform(df_clean["District"])
    print(f"District encoder classes: {list(district_encoder.classes_)}")

    # 5. Feature columns, in exact required order
    X = df_clean[FEATURE_COLUMNS].copy()
    y_raw = df_clean["FloodRisk"].copy()

    # 6. LabelEncoder + to_categorical() on FloodRisk target
    class_encoder = LabelEncoder()
    # Fit with explicit classes order to guarantee consistent index mapping
    class_encoder.fit(TARGET_CLASSES)
    y_encoded = class_encoder.transform(y_raw)
    y_cat = to_categorical(y_encoded, num_classes=3)
    print(f"Class encoder classes: {list(class_encoder.classes_)}")

    # 7. Train/test split: 80/20, random_state=42, stratify=integer target
    print("\n--- 5. Train / Test Split (80/20 Stratified) ---")
    X_train, X_test, y_train_cat, y_test_cat, y_train_int, y_test_int = train_test_split(
        X,
        y_cat,
        y_encoded,
        test_size=0.20,
        random_state=random_state,
        stratify=y_encoded,
    )
    print(f"Training samples: {len(X_train)} | Testing samples: {len(X_test)}")

    # 8. StandardScaler — fit ONLY on training data, reuse for test/prediction
    print("\n--- 6. Feature Scaling (StandardScaler) ---")
    feature_scaler = StandardScaler()
    X_train_scaled = feature_scaler.fit_transform(X_train)
    X_test_scaled = feature_scaler.transform(X_test)
    print("StandardScaler fitted strictly on training partition.")

    # 9. Model Architecture
    print("\n--- 7. Building Deep Learning Model ---")
    keras.utils.set_random_seed(random_state)
    model = keras.Sequential([
        layers.Input(shape=(5,)),
        layers.Dense(64, activation="relu"),
        layers.Dropout(0.2),
        layers.Dense(32, activation="relu"),
        layers.Dropout(0.2),
        layers.Dense(3, activation="softmax"),
    ])
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    model.summary()

    # 10. Training Config
    print("\n--- 8. Training Neural Network ---")
    early_stopping = keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=15,
        restore_best_weights=True,
    )

    history = model.fit(
        X_train_scaled,
        y_train_cat,
        epochs=150,
        batch_size=16,
        validation_split=0.15,
        callbacks=[early_stopping],
        verbose=1,
    )

    # 11. Model Evaluation
    print("\n--- 9. Evaluating Model Performance ---")
    y_pred_probs = model.predict(X_test_scaled)
    y_pred_int = np.argmax(y_pred_probs, axis=1)

    y_test_labels = class_encoder.inverse_transform(y_test_int)
    y_pred_labels = class_encoder.inverse_transform(y_pred_int)

    acc = float(accuracy_score(y_test_int, y_pred_int))
    prec = float(precision_score(y_test_int, y_pred_int, average="weighted", zero_division=0))
    rec = float(recall_score(y_test_int, y_pred_int, average="weighted", zero_division=0))
    f1 = float(f1_score(y_test_int, y_pred_int, average="weighted", zero_division=0))

    metrics = {
        "accuracy": acc,
        "precision": prec,
        "recall": rec,
        "f1": f1,
    }

    print(f"\nFinal Test Metrics:")
    print(f"Accuracy : {acc * 100:.2f}%")
    print(f"Precision: {prec * 100:.2f}%")
    print(f"Recall   : {rec * 100:.2f}%")
    print(f"F1-Score : {f1 * 100:.2f}%")

    print("\nFull Classification Report:")
    print(classification_report(y_test_labels, y_pred_labels, labels=TARGET_CLASSES))

    # 12. Confusion Matrix Plot (Safe / Warning / Danger order)
    print("\n--- 10. Generating Plots ---")
    cm = confusion_matrix(y_test_labels, y_pred_labels, labels=TARGET_CLASSES)
    fig_cm, ax_cm = plt.subplots(figsize=(6, 5))
    cax = ax_cm.matshow(cm, cmap=plt.cm.Blues, alpha=0.85)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax_cm.text(
                x=j,
                y=i,
                s=str(cm[i, j]),
                va="center",
                ha="center",
                fontsize=13,
                fontweight="bold",
                color="white" if cm[i, j] > (cm.max() / 2) else "black",
            )
    fig_cm.colorbar(cax)
    ax_cm.set_xticks([0, 1, 2])
    ax_cm.set_yticks([0, 1, 2])
    ax_cm.set_xticklabels(TARGET_CLASSES, fontsize=11)
    ax_cm.set_yticklabels(TARGET_CLASSES, fontsize=11)
    ax_cm.set_xlabel("Predicted Label", fontsize=12, labelpad=10)
    ax_cm.set_ylabel("True Label", fontsize=12, labelpad=10)
    ax_cm.set_title("Confusion Matrix (Deep Learning)", fontsize=13, pad=15, fontweight="bold")
    plt.tight_layout()
    cm_path = out_path / "confusion_matrix_dl.png"
    plt.savefig(cm_path, dpi=300)
    plt.close(fig_cm)
    print(f"Saved confusion matrix to: {cm_path}")

    # 13. Training History Plot
    fig_hist, (ax_loss, ax_acc) = plt.subplots(1, 2, figsize=(12, 4.5))
    epochs_ran = range(1, len(history.history["loss"]) + 1)

    ax_loss.plot(epochs_ran, history.history["loss"], label="Train Loss", color="#4FA3D9", lw=2)
    ax_loss.plot(epochs_ran, history.history["val_loss"], label="Val Loss", color="#E74C3C", lw=2, linestyle="--")
    ax_loss.set_title("Loss Progression", fontsize=12, fontweight="bold")
    ax_loss.set_xlabel("Epoch")
    ax_loss.set_ylabel("Categorical Crossentropy")
    ax_loss.legend()
    ax_loss.grid(True, alpha=0.3)

    ax_acc.plot(epochs_ran, history.history["accuracy"], label="Train Accuracy", color="#2ECC71", lw=2)
    ax_acc.plot(epochs_ran, history.history["val_accuracy"], label="Val Accuracy", color="#F39C12", lw=2, linestyle="--")
    ax_acc.set_title("Accuracy Progression", fontsize=12, fontweight="bold")
    ax_acc.set_xlabel("Epoch")
    ax_acc.set_ylabel("Accuracy")
    ax_acc.legend()
    ax_acc.grid(True, alpha=0.3)

    plt.tight_layout()
    hist_path = out_path / "training_history.png"
    plt.savefig(hist_path, dpi=300)
    plt.close(fig_hist)
    print(f"Saved training history to: {hist_path}")

    # 14. Save Artifacts
    print("\n--- 11. Saving Model Artifacts ---")
    model_save_path = out_path / "flood_model_dl.keras"
    model.save(str(model_save_path))
    print(f"Saved Keras model to: {model_save_path}")

    joblib.dump(feature_scaler, out_path / "feature_scaler.pkl")
    joblib.dump(district_encoder, out_path / "district_encoder.pkl")
    joblib.dump(class_encoder, out_path / "class_encoder.pkl")
    joblib.dump(metrics, out_path / "metrics_dl.pkl")
    print("Saved feature_scaler.pkl, district_encoder.pkl, class_encoder.pkl, metrics_dl.pkl.")

    return metrics

if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    project_dir = script_dir.parent
    data_csv = project_dir / "data" / "flood_data.csv"
    train_flood_model(str(data_csv), str(script_dir))

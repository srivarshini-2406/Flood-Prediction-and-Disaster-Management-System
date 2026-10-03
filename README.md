# 🌊 Flood Prediction Disaster Management System

A **Deep Learning-based Flood Prediction and Disaster Management System** that predicts flood risk using environmental parameters such as **rainfall, water level, soil moisture, and humidity**.

The system classifies the current condition into three risk levels:

* 🟢 **Safe**
* 🟡 **Warning**
* 🔴 **Danger**

It provides a simple **Streamlit-based web interface** with support for **English and Tamil**, making the system easier to use for different users.

---

## 📌 Project Overview

Floods can cause significant damage to human lives, infrastructure, agriculture, and the environment. Early prediction and timely warnings can help reduce the impact of flooding.

This project uses environmental data and a **Deep Learning classification model** to identify the current flood-risk level.

The system takes four major environmental parameters:

| Input Parameter  | Description              |
| ---------------- | ------------------------ |
| 🌧️ Rainfall     | Amount of rainfall       |
| 💧 Water Level   | Current water level      |
| 🌱 Soil Moisture | Moisture content in soil |
| 💦 Humidity      | Atmospheric humidity     |

Based on these inputs, the trained model predicts one of the following:

**Safe → Warning → Danger**

---

## 🎯 Objectives

* Predict flood-risk conditions using environmental parameters.
* Develop a machine-learning-based flood prediction system.
* Provide early warnings based on predicted flood severity.
* Create a simple and user-friendly interface.
* Support both **English and Tamil** languages.
* Demonstrate the use of Deep Learning for disaster management.

---

## 🧠 Machine Learning Model

The project uses a **Deep Learning Neural Network** implemented using **TensorFlow/Keras**.

### Model Architecture

```text
Input Layer
    ↓
Dense Layer - 32 neurons
    ↓
Dense Layer - 16 neurons
    ↓
Output Layer - 3 classes
    ↓
Safe / Warning / Danger
```

### Activation Functions

* Hidden layers: **ReLU**
* Output layer: **Softmax**

### Optimizer

**Adam**

### Loss Function

**Categorical Cross-Entropy**

---

## 📊 Input Features

The model uses four input features:

```text
1. Rainfall
2. Water Level
3. Soil Moisture
4. Humidity
```

The prediction is generated based on the relationship between these environmental conditions and flood-risk categories.

---

## 🚦 Prediction Classes

### 🟢 Safe

Environmental conditions indicate a relatively low flood risk.

### 🟡 Warning

Environmental conditions indicate an increasing possibility of flooding and users should remain alert.

### 🔴 Danger

Environmental conditions indicate a high flood-risk condition requiring immediate attention.

---

## 🖥️ User Interface

The project uses **Streamlit** to provide an interactive web interface.

The interface allows users to:

* Enter environmental values.
* Select language.
* Generate flood-risk predictions.
* View the predicted risk category.
* Receive an appropriate warning based on the prediction.

### Supported Languages

* 🇬🇧 English
* 🇮🇳 Tamil

---

## 🛠️ Technologies Used

* **Python**
* **TensorFlow**
* **Keras**
* **Streamlit**
* **NumPy**
* **Pandas**
* **Scikit-learn**
* **Matplotlib**

---

## 📂 Project Structure

```text
Flood-Prediction-Disaster-Management-System/
│
├── app.py
├── model/
│   └── flood_prediction_model.h5
│
├── dataset/
│   └── flood_dataset.csv
│
├── notebooks/
│   └── model_training.ipynb
│
├── requirements.txt
├── README.md
└── LICENSE
```

> Adjust the filenames/folders above if your actual GitHub project structure uses different names.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Flood-Prediction-Disaster-Management-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Flood-Prediction-Disaster-Management-System
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📋 Example Prediction

Example environmental inputs:

```text
Rainfall      : 120 mm
Water Level   : 8.5 m
Soil Moisture : 75%
Humidity      : 85%
```

The model processes these values and produces a flood-risk classification such as:

```text
Prediction: DANGER
```

---

## 📈 Model Evaluation

The current project report documents the following final evaluation values:

| Metric    | Final Result |
| --------- | -----------: |
| Accuracy  |          82% |
| Precision |          79% |
| Recall    |          75% |

These values represent the results documented in the project report and should be updated if further model testing produces different results.

---

## 🌐 Future Scope

The system can be further improved by:

* Integrating real-time IoT sensors.
* Using live rainfall and water-level data.
* Adding geographical location-based predictions.
* Integrating weather APIs.
* Developing mobile applications.
* Adding SMS and notification-based alerts.
* Improving model accuracy using larger datasets.
* Integrating GIS and flood-zone mapping.
* Deploying the system on cloud platforms.

---

## 👥 Project Team

**Flood Prediction Disaster Management System**

Developed as a **Project-Based Learning (PBL)** project.

---

## 📜 License

This project is developed for **academic and educational purposes**.

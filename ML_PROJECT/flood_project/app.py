"""
Streamlit Application for Flood Prediction Disaster System.
Citizen-facing bilingual interface for real-time AI flood risk assessment,
environmental analytics, localized emergency assistance, and safety checklists.
"""

from datetime import datetime
import os
from pathlib import Path

# Select Keras' inference backend before importing any application modules.
# The model archive was trained with a PyTorch optimizer, but prediction uses
# only weights; predictor.py loads it with compile=False.
os.environ["KERAS_BACKEND"] = "tensorflow"

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Set page configuration first
st.set_page_config(
    page_title="Flood Prediction Disaster System",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Resolve project paths
APP_DIR = Path(__file__).resolve().parent
DATA_PATH = APP_DIR / "data" / "flood_data.csv"

# Import local modules
import sys
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from emergency_data import EMERGENCY_INFO, get_emergency_info
from model.predict import predict_flood_risk
from model.recommendations import get_recommendation
from translations import (
    TRANSLATIONS,
    get_text,
    get_translated_risk,
    get_translated_tips,
)

# --- B1 & B2: Theme Styling and Element Clean-up ---
st.markdown(
    """
    <style>
        /* Hide Streamlit default toolbar, deploy button, and footer */
        #MainMenu {visibility: hidden;}
        .stDeployButton {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0;
        }

        /* Container Card Styling */
        .info-card {
            background-color: #FFFFFF;
            border: 1.5px solid #D1E7F5;
            border-radius: 12px;
            padding: 22px;
            box-shadow: 0 4px 6px -1px rgba(79, 163, 217, 0.08);
            margin-bottom: 16px;
        }

        .action-card {
            background-color: #FFFFFF;
            border: 1.5px solid #D1E7F5;
            border-radius: 14px;
            padding: 24px 20px;
            text-align: center;
            box-shadow: 0 4px 10px -2px rgba(79, 163, 217, 0.12);
            transition: transform 0.2s ease, border-color 0.2s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .action-card:hover {
            border-color: #4FA3D9;
            transform: translateY(-3px);
            box-shadow: 0 8px 18px -3px rgba(79, 163, 217, 0.2);
        }

        .action-icon {
            font-size: 38px;
            margin-bottom: 10px;
        }

        .action-title {
            font-size: 20px;
            font-weight: 700;
            color: #1C1C1C;
            margin-bottom: 8px;
        }

        .action-desc {
            font-size: 14px;
            color: #555555;
            line-height: 1.4;
            margin-bottom: 16px;
        }

        /* Risk Badges */
        .risk-badge-Safe {
            background-color: #EBFBF2;
            color: #2ECC71;
            border: 2px solid #2ECC71;
            border-radius: 10px;
            padding: 14px 24px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            letter-spacing: 0.5px;
        }

        .risk-badge-Warning {
            background-color: #FFF9EE;
            color: #F39C12;
            border: 2px solid #F39C12;
            border-radius: 10px;
            padding: 14px 24px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            letter-spacing: 0.5px;
        }

        .risk-badge-Danger {
            background-color: #FDF0F0;
            color: #E74C3C;
            border: 2px solid #E74C3C;
            border-radius: 10px;
            padding: 14px 24px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            letter-spacing: 0.5px;
        }

        .emergency-box {
            background-color: #FFF5F5;
            border: 1.5px solid #F8B4B4;
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
        }

        .contact-row {
            padding: 8px 0;
            border-bottom: 1px solid #FFE3E3;
            font-size: 15px;
        }
        .contact-row:last-child {
            border-bottom: none;
        }

        /* Streamlit Button Tweaks */
        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Session State Initialization ---
if "language" not in st.session_state:
    st.session_state.language = "en"

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

if "last_prediction" not in st.session_state:
    st.session_state.last_prediction = None

lang = st.session_state.language

# --- B3: Sidebar Navigation & Language Selector ---
with st.sidebar:
    st.markdown("### 🌐 " + get_text("lang_selector_label", lang))
    lang_choice = st.selectbox(
        label="Language Selection",
        options=["English", "தமிழ்"],
        index=0 if lang == "en" else 1,
        label_visibility="collapsed",
    )
    new_lang = "en" if lang_choice == "English" else "ta"
    if new_lang != st.session_state.language:
        st.session_state.language = new_lang
        st.rerun()

    st.markdown("---")
    st.markdown("### 🧭 Navigation")

    nav_pages = [
        ("Home", "nav_home", "🏠"),
        ("Prediction", "nav_prediction", "⚡"),
        ("Analytics", "nav_analytics", "📊"),
        ("Area Overview", "nav_overview", "🗺️"),
        ("About", "nav_about", "ℹ️"),
    ]

    for page_key, trans_key, icon in nav_pages:
        label = f"{icon} {get_text(trans_key, lang)}"
        btn_type = "primary" if st.session_state.page == page_key else "secondary"
        if st.button(label, key=f"nav_btn_{page_key}", use_container_width=True, type=btn_type):
            st.session_state.page = page_key
            st.rerun()

    st.markdown("---")
    st.caption("🌊 Tamil Nadu Flood Disaster Support")


# Helper function to navigate
def navigate_to(page_name: str):
    st.session_state.page = page_name
    st.rerun()


# ==========================================
# PAGE: HOME (B5 — Minimalist & Action-Focused)
# ==========================================
if st.session_state.page == "Home":
    st.markdown(
        f"<h1 style='text-align: center; color: #1C1C1C; margin-bottom: 4px;'>{get_text('home_title', lang)}</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='text-align: center; font-size: 18px; color: #555555; margin-bottom: 40px;'>{get_text('home_tagline', lang)}</p>",
        unsafe_allow_html=True,
    )

    # 3 Large Clickable Navigation Cards
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(
            f"""
            <div class="action-card">
                <div>
                    <div class="action-icon">⚡</div>
                    <div class="action-title">{get_text('card_predict_title', lang)}</div>
                    <div class="action-desc">{get_text('card_predict_desc', lang)}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(f"👉 {get_text('card_predict_title', lang)}", key="btn_home_predict", use_container_width=True, type="primary"):
            navigate_to("Prediction")

    with col2:
        st.markdown(
            f"""
            <div class="action-card">
                <div>
                    <div class="action-icon">📊</div>
                    <div class="action-title">{get_text('card_analytics_title', lang)}</div>
                    <div class="action-desc">{get_text('card_analytics_desc', lang)}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(f"👉 {get_text('card_analytics_title', lang)}", key="btn_home_analytics", use_container_width=True):
            navigate_to("Analytics")

    with col3:
        st.markdown(
            f"""
            <div class="action-card">
                <div>
                    <div class="action-icon">🚨</div>
                    <div class="action-title">{get_text('card_emergency_title', lang)}</div>
                    <div class="action-desc">{get_text('card_emergency_desc', lang)}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(f"👉 {get_text('card_emergency_title', lang)}", key="btn_home_emergency", use_container_width=True):
            navigate_to("Prediction")


# ==========================================
# PAGE: PREDICTION (B6 — Real-Time Assessment)
# ==========================================
elif st.session_state.page == "Prediction":
    st.title(f"⚡ {get_text('prediction_header', lang)}")
    st.write(get_text("prediction_subheader", lang))
    st.markdown("<br>", unsafe_allow_html=True)

    districts_list = [
        "Chennai",
        "Coimbatore",
        "Madurai",
        "Tiruchirappalli",
        "Salem",
        "Tirunelveli",
        "Erode",
        "Vellore",
    ]

    with st.form("prediction_form", clear_on_submit=False):
        col_left, col_right = st.columns(2, gap="large")

        with col_left:
            district_input = st.selectbox(
                label=f"📍 {get_text('select_district', lang)}",
                options=districts_list,
                index=0,
            )
            rainfall_input = st.number_input(
                label=f"🌧️ {get_text('rainfall_label', lang)}",
                min_value=0.0,
                max_value=1000.0,
                value=120.0,
                step=5.0,
            )
            water_level_input = st.number_input(
                label=f"🌊 {get_text('water_level_label', lang)}",
                min_value=0.0,
                max_value=50.0,
                value=4.5,
                step=0.2,
            )

        with col_right:
            soil_moisture_input = st.number_input(
                label=f"🌱 {get_text('soil_moisture_label', lang)}",
                min_value=0.0,
                max_value=100.0,
                value=65.0,
                step=1.0,
            )
            humidity_input = st.number_input(
                label=f"💧 {get_text('humidity_label', lang)}",
                min_value=0.0,
                max_value=100.0,
                value=80.0,
                step=1.0,
            )

        submitted = st.form_submit_button(
            label=f"🔍 {get_text('predict_button', lang)}",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        # Validation
        if (
            rainfall_input < 0
            or water_level_input < 0
            or soil_moisture_input < 0
            or humidity_input < 0
        ):
            st.error(get_text("validation_error_negative", lang))
        else:
            try:
                res = predict_flood_risk(
                    district=district_input,
                    rainfall=rainfall_input,
                    water_level=water_level_input,
                    soil_moisture=soil_moisture_input,
                    humidity=humidity_input,
                )

                risk_en = res["risk"]
                confidence_val = res["confidence"]
                probs_dict = res["probabilities"]
                translated_risk = get_translated_risk(risk_en, lang)

                # Store in history
                record = {
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "district": district_input,
                    "rainfall": rainfall_input,
                    "water_level": water_level_input,
                    "soil_moisture": soil_moisture_input,
                    "humidity": humidity_input,
                    "risk": risk_en,
                    "risk_translated": translated_risk,
                    "confidence": confidence_val,
                }
                st.session_state.prediction_history.append(record)
                st.session_state.last_prediction = record

                st.markdown("<br>", unsafe_allow_html=True)
                st.subheader(f"📋 {get_text('prediction_result_header', lang)}")

                # Large Colored Heading
                st.markdown(
                    f"""
                    <div class="risk-badge-{risk_en}">
                        {get_text('risk_level_label', lang)}: {translated_risk.upper()} ({confidence_val * 100:.1f}%)
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.markdown("<br>", unsafe_allow_html=True)

                # Class Probability Breakdown in Expander
                with st.expander(f"📊 {get_text('probability_breakdown', lang)}", expanded=False):
                    classes = ["Safe", "Warning", "Danger"]
                    class_labels = [get_translated_risk(c, lang) for c in classes]
                    class_probs = [probs_dict.get(c, 0.0) * 100 for c in classes]
                    colors = ["#2ECC71", "#F39C12", "#E74C3C"]

                    fig_prob = go.Figure(
                        go.Bar(
                            x=class_labels,
                            y=class_probs,
                            marker_color=colors,
                            text=[f"{p:.1f}%" for p in class_probs],
                            textposition="auto",
                        )
                    )
                    fig_prob.update_layout(
                        title=get_text("probability_chart_title", lang),
                        yaxis_title="Probability (%)",
                        yaxis=dict(range=[0, 100]),
                        height=280,
                        margin=dict(l=20, r=20, t=40, b=20),
                        plot_bgcolor="#FFFFFF",
                        paper_bgcolor="#FFFFFF",
                    )
                    st.plotly_chart(fig_prob, use_container_width=True)

                # Safety Tips
                st.markdown(f"### 🛡️ {get_text('safety_tips_header', lang)}")
                tips = get_translated_tips(risk_en, lang)
                for tip in tips:
                    st.markdown(f"- **{tip}**")

                # Emergency Information Section if Risk == Danger
                if risk_en == "Danger":
                    emg = get_emergency_info(district_input)
                    st.markdown(
                        f"""
                        <div class="emergency-box">
                            <h3 style="color: #E74C3C; margin-top: 0;">🚨 {get_text('emergency_header', lang)} — {district_input}</h3>
                            <div class="contact-row"><strong>📞 {get_text('helpline_label', lang)}:</strong> {emg['helpline']}</div>
                            <div class="contact-row"><strong>🚑 {get_text('ambulance_label', lang)}:</strong> {emg['ambulance']}</div>
                            <div class="contact-row"><strong>🏥 {get_text('hospital_label', lang)}:</strong> {emg['hospital']}</div>
                            <div class="contact-row"><strong>🏕️ {get_text('shelter_label', lang)}:</strong> {emg['shelter']}</div>
                            <p style="font-size: 12px; color: #888888; margin-top: 12px; margin-bottom: 0;">ℹ️ {get_text('emergency_demo_note', lang)}</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            except Exception as e:
                st.error(f"Prediction failed: {e}")


# ==========================================
# PAGE: ANALYTICS (B7 — Environmental Insights)
# ==========================================
elif st.session_state.page == "Analytics":
    st.title(f"📊 {get_text('analytics_title', lang)}")
    st.write(get_text("analytics_subtitle", lang))
    st.markdown("<br>", unsafe_allow_html=True)

    if not DATA_PATH.exists():
        st.warning("Dataset file not found. Please generate the data first.")
    else:
        df_raw = pd.read_csv(DATA_PATH).dropna()

        # 1. Feature Distributions
        st.subheader(f"📈 {get_text('dist_plots_header', lang)}")
        feature_options = {
            "Rainfall_mm": get_text("feature_Rainfall_mm", lang),
            "WaterLevel_m": get_text("feature_WaterLevel_m", lang),
            "SoilMoisture_percent": get_text("feature_SoilMoisture_percent", lang),
            "Humidity_percent": get_text("feature_Humidity_percent", lang),
        }

        color_map = {"Safe": "#2ECC71", "Warning": "#F39C12", "Danger": "#E74C3C"}

        col_f1, col_f2 = st.columns(2)
        numeric_features = ["Rainfall_mm", "WaterLevel_m", "SoilMoisture_percent", "Humidity_percent"]

        for idx, feat in enumerate(numeric_features):
            target_col = col_f1 if idx % 2 == 0 else col_f2
            with target_col:
                fig_hist = px.histogram(
                    df_raw,
                    x=feat,
                    color="FloodRisk",
                    color_discrete_map=color_map,
                    category_orders={"FloodRisk": ["Safe", "Warning", "Danger"]},
                    nbins=25,
                    barmode="overlay",
                    opacity=0.75,
                    title=f"{feature_options[feat]} vs {get_text('risk_level_label', lang)}",
                    labels={feat: feature_options[feat], "FloodRisk": get_text("risk_level_label", lang)},
                )
                fig_hist.update_layout(
                    height=320,
                    margin=dict(l=20, r=20, t=40, b=20),
                    plot_bgcolor="#FFFFFF",
                    paper_bgcolor="#FFFFFF",
                )
                st.plotly_chart(fig_hist, use_container_width=True)

        st.markdown("---")

        # 2. Risk Frequency by District
        st.subheader(f"📍 {get_text('district_risk_header', lang)}")
        fig_dist = px.histogram(
            df_raw,
            x="District",
            color="FloodRisk",
            color_discrete_map=color_map,
            category_orders={"FloodRisk": ["Safe", "Warning", "Danger"]},
            barmode="group",
            labels={"District": get_text("district_label", lang), "FloodRisk": get_text("risk_level_label", lang)},
        )
        fig_dist.update_layout(
            height=360,
            margin=dict(l=20, r=20, t=30, b=20),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
        )
        st.plotly_chart(fig_dist, use_container_width=True)

        st.markdown("---")

        # 3. Correlation Heatmap & Dynamic Plain-Language Explanation
        st.subheader(f"🔥 {get_text('corr_heatmap_header', lang)}")

        corr_df = df_raw[numeric_features].corr()
        # Translated axis labels for heatmap
        display_names = [feature_options[col] for col in numeric_features]

        fig_corr = px.imshow(
            corr_df.values,
            x=display_names,
            y=display_names,
            text_auto=".2f",
            color_continuous_scale="Blues",
            aspect="auto",
        )
        fig_corr.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
        )
        st.plotly_chart(fig_corr, use_container_width=True)

        # Dynamic plain-language explanation
        # Find top correlated pair (excluding diagonal)
        np_corr = corr_df.values.copy()
        np.fill_diagonal(np_corr, 0.0)
        max_idx = np.unravel_index(np.argmax(np.abs(np_corr)), np_corr.shape)
        feat_1_key = numeric_features[max_idx[0]]
        feat_2_key = numeric_features[max_idx[1]]
        max_corr_val = corr_df.iloc[max_idx[0], max_idx[1]]

        feat_1_name = feature_options[feat_1_key]
        feat_2_name = feature_options[feat_2_key]

        st.markdown(
            f"""
            <div class="info-card">
                <p style="font-size: 16px; font-weight: 600; color: #1C1C1C; margin-bottom: 6px;">
                    💡 {get_text('correlation_intro', lang)}
                </p>
                <p style="font-size: 15px; color: #333333; margin-bottom: 4px;">
                    {get_text('corr_explanation', lang).format(feat1=feat_1_name, feat2=feat_2_name)}
                </p>
                <p style="font-size: 12px; color: #777777; margin-bottom: 0;">
                    {get_text('corr_caption', lang).format(val=max_corr_val)}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ==========================================
# PAGE: AREA OVERVIEW (B8 — Citizen Summary)
# ==========================================
elif st.session_state.page == "Area Overview":
    st.title(f"🗺️ {get_text('overview_title', lang)}")
    st.write(get_text("overview_subtitle", lang))
    st.markdown("<br>", unsafe_allow_html=True)

    # 1. Prominent Recent Assessment Card
    st.subheader(f"📌 {get_text('recent_prediction_header', lang)}")
    last_p = st.session_state.last_prediction

    if last_p is None:
        st.markdown(
            f"""
            <div class="info-card" style="text-align: center; padding: 30px;">
                <p style="font-size: 16px; color: #666666; margin-bottom: 12px;">
                    ℹ️ {get_text('no_prediction_yet', lang)}
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        risk_key = last_p["risk"]
        risk_color = "#2ECC71" if risk_key == "Safe" else "#F39C12" if risk_key == "Warning" else "#E74C3C"
        translated_risk = get_translated_risk(risk_key, lang)

        st.markdown(
            f"""
            <div class="info-card" style="border-left: 6px solid {risk_color};">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                    <div>
                        <h3 style="margin: 0; color: #1C1C1C;">📍 {last_p['district']}</h3>
                        <p style="color: #666666; margin: 4px 0 0 0; font-size: 13px;">🕒 {last_p['timestamp']}</p>
                    </div>
                    <div>
                        <span style="background-color: {risk_color}22; color: {risk_color}; border: 1.5px solid {risk_color}; border-radius: 8px; padding: 6px 16px; font-weight: bold; font-size: 20px;">
                            {translated_risk} ({last_p['confidence'] * 100:.1f}%)
                        </span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. Regional Risk Snapshot (Horizontal Bar Chart)
    st.subheader(f"📊 {get_text('district_risk_snapshot_header', lang)}")
    if DATA_PATH.exists():
        df_raw = pd.read_csv(DATA_PATH).dropna()
        risk_counts = df_raw.groupby(["District", "FloodRisk"]).size().reset_index(name="Count")
        color_map = {"Safe": "#2ECC71", "Warning": "#F39C12", "Danger": "#E74C3C"}

        fig_snap = px.bar(
            risk_counts,
            y="District",
            x="Count",
            color="FloodRisk",
            orientation="h",
            color_discrete_map=color_map,
            category_orders={"FloodRisk": ["Safe", "Warning", "Danger"]},
            labels={
                "Count": get_text("areas_at_risk_axis", lang),
                "District": get_text("district_label", lang),
                "FloodRisk": get_text("status_label", lang),
            },
        )
        fig_snap.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
        )
        st.plotly_chart(fig_snap, use_container_width=True)

    # 3. Active Safety Checklist matching latest risk level (or Warning by default)
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f"✅ {get_text('active_checklist_header', lang)}")
    st.write(get_text("checklist_intro", lang))

    current_risk_for_tips = last_p["risk"] if last_p else "Warning"
    tips_list = get_translated_tips(current_risk_for_tips, lang)

    for idx, tip in enumerate(tips_list):
        st.checkbox(f"**{tip}**", value=(idx == 0), key=f"chk_tip_{idx}")


# ==========================================
# PAGE: ABOUT (B9 — Technical & Architectural)
# ==========================================
elif st.session_state.page == "About":
    st.title(f"ℹ️ {get_text('about_title', lang)}")
    st.markdown("<br>", unsafe_allow_html=True)

    # Problem Statement & Objectives
    st.subheader(f"🎯 {get_text('problem_statement_header', lang)}")
    st.info(get_text("problem_statement_text", lang))

    st.subheader(f"📌 {get_text('objectives_header', lang)}")
    st.markdown(f"- {get_text('obj_1', lang)}")
    st.markdown(f"- {get_text('obj_2', lang)}")
    st.markdown(f"- {get_text('obj_3', lang)}")
    st.markdown(f"- {get_text('obj_4', lang)}")

    st.markdown("---")

    # Workflow
    st.subheader(f"🔄 {get_text('workflow_header', lang)}")
    st.markdown(
        f"""
        <div class="info-card" style="line-height: 1.8; font-family: monospace; font-size: 14px; background-color: #EAF4FB;">
            {get_text('workflow_steps', lang)}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Tech Stack & Deep Learning Architecture
    col_tech, col_arch = st.columns(2, gap="large")

    with col_tech:
        st.subheader(f"💻 {get_text('tech_stack_header', lang)}")
        st.markdown(
            """
            - **Programming Language**: Python 3.14
            - **Web Application**: Streamlit
            - **Deep Learning Framework**: Keras 3 / TensorFlow / PyTorch Backend
            - **Machine Learning & Preprocessing**: Scikit-Learn (StandardScaler, LabelEncoder)
            - **Data Processing**: Pandas, NumPy
            - **Interactive Visualizations**: Plotly Express & Plotly Graph Objects
            - **Evaluation & Artifacts**: Matplotlib, Joblib
            """
        )

    with col_arch:
        st.subheader(f"🧠 {get_text('model_arch_header', lang)}")
        st.text(get_text("model_arch_details", lang))

    st.markdown("---")

    # Future Scope
    st.subheader(f"🚀 {get_text('future_scope_header', lang)}")
    st.markdown(get_text("future_scope_details", lang))

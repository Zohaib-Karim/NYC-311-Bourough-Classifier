import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy as np
import plotly.express as px
import folium
from folium.plugins import HeatMap
import streamlit.components.v1 as components

# ---------------------------
# INITIAL CONFIG
# ---------------------------
st.set_page_config(page_title="NYC 311 Complaint Classifier", page_icon="🗽", layout="wide")

# ---------------------------
# LOAD MODEL
# ---------------------------
# (For demo purposes using random predictions)
model = tf.keras.models.load_model("my_bilstm_model.keras", compile=False)

boroughs = ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island']
borough_coords = {
    "Manhattan": [40.7831, -73.9712],
    "Brooklyn": [40.6782, -73.9442],
    "Queens": [40.7282, -73.7949],
    "Bronx": [40.8448, -73.8648],
    "Staten Island": [40.5795, -74.1502],
}

# ---------------------------
# SESSION STATE SETUP
# ---------------------------
if 'history' not in st.session_state:
    st.session_state.history = []
if 'heatmap_points' not in st.session_state:
    st.session_state.heatmap_points = []
if 'heatmap_len' not in st.session_state:
    st.session_state.heatmap_len = 0
if 'heatmap_html' not in st.session_state:
    st.session_state.heatmap_html = None

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("🗂️ NYC 311 Complaint Classifier")
st.sidebar.markdown("### Quick Complaint Examples")

examples = [
    "Illegal parking blocking the driveway",
    "Noise complaint from construction site",
    "Street light not working",
    "Water leak in public street",
    "Overflowing trash on sidewalk"
]
selected_example = st.sidebar.selectbox("Pick an Example", examples)

st.sidebar.info("💡 Try writing a few custom complaints to see how predictions vary!")

# ---------------------------
# HEADER
# ---------------------------
st.markdown(
    """
    <div style="text-align:center; padding: 10px 0; background-color:#0E1117; border-radius:12px; margin-bottom:20px;">
        <h1 style="color:#4DB6AC;">🗽 NYC 311 Complaint Borough Classifier</h1>
        <p style="font-size:18px; color:#AAAAAA;">
        This project uses a BiLSTM model with GloVe embeddings to predict which NYC borough a 311 complaint likely belongs to. 
        It helps city departments prioritize responses based on complaint trends and locations.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# TABS
# ---------------------------
tab1, tab2, tab3 = st.tabs(["🔮 Prediction", "📊 Dashboard", "🌎 Heatmap"])

# ---------------------------
# TAB 1 — PREDICTION
# ---------------------------
with tab1:
    st.subheader("Enter a Complaint Description Below")

    complaint = st.text_area("Complaint Description", value=selected_example, height=100)

    if st.button("🔍 Predict Borough"):
        # Simulated probabilities (replace this with model prediction in your final)
        probabilities = np.random.dirichlet(np.ones(len(boroughs)), size=1)[0]
        predicted_idx = np.argmax(probabilities)
        predicted_borough = boroughs[predicted_idx]

        # Save results
        st.metric("Predicted Borough", predicted_borough)

        prob_df = pd.DataFrame({
            'Borough': boroughs,
            'Probability': probabilities
        })

        fig = px.bar(prob_df, x='Borough', y='Probability', text='Probability',
                     color='Probability', color_continuous_scale='Tealgrn', range_y=[0,1])
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

        # Save to history and heatmap
        st.session_state.history.append({
            "Complaint": complaint,
            "Predicted Borough": predicted_borough
        })
        st.session_state.heatmap_points.append(borough_coords[predicted_borough])

    if st.session_state.history:
        st.subheader("📜 Prediction History")
        hist_df = pd.DataFrame(st.session_state.history)
        st.dataframe(hist_df, use_container_width=True, height=200)

# ---------------------------
# TAB 2 — DASHBOARD
# ---------------------------
with tab2:
    st.subheader("NYC 311 Complaint Analytics Dashboard")

    # Mock data for visualization
    dashboard_data = pd.DataFrame({
        'Borough': boroughs,
        'Number of Complaints': np.random.randint(50, 300, size=len(boroughs))
    })

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Complaint Distribution by Borough")
        fig1 = px.pie(dashboard_data, names='Borough', values='Number of Complaints',
                      color_discrete_sequence=px.colors.sequential.Tealgrn)
        fig1.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.markdown("#### Total Complaints by Borough")
        fig2 = px.bar(dashboard_data, x='Borough', y='Number of Complaints',
                      color='Number of Complaints', color_continuous_scale='Tealgrn')
        st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# TAB 3 — HEATMAP
# ---------------------------
with tab3:
    st.subheader("🌎 Geographic Heatmap of Complaint Density")
    st.write("Visualize borough complaint intensity using a stable heatmap overlay.")

    heat_points = st.session_state.heatmap_points

    # Regenerate only if data changes
    if len(heat_points) != st.session_state.heatmap_len or st.session_state.heatmap_html is None:
        m = folium.Map(location=[40.7128, -74.0060], zoom_start=10, tiles="cartodb positron")

        if heat_points:
            HeatMap(heat_points, radius=20, blur=15, min_opacity=0.4).add_to(m)

        # Add borough markers
        for b, coords in borough_coords.items():
            folium.CircleMarker(
                location=coords,
                radius=6,
                popup=f"{b}",
                color="#2a9df4",
                fill=True,
                fill_color="#2a9df4"
            ).add_to(m)

        # Cache the rendered map
        st.session_state.heatmap_html = m.get_root().render()
        st.session_state.heatmap_len = len(heat_points)

    if st.session_state.heatmap_html:
        components.html(st.session_state.heatmap_html, height=550)
    else:
        st.info("No heatmap data yet — make a prediction to populate the map.")

    if st.button("🧹 Clear Heatmap Data"):
        st.session_state.heatmap_points = []
        st.session_state.heatmap_len = 0
        st.session_state.heatmap_html = None
        st.success("Heatmap data cleared! Make new predictions to add points.")

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888;'>
        💡 Powered by <b>Streamlit + TensorFlow (BiLSTM + GloVe)</b> | Built with ❤️ by <b>Ayush</b>
    </div>
    """,
    unsafe_allow_html=True
)

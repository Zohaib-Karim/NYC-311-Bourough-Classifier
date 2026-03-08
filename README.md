# NYC 311 Complaint Borough Classifier 🗽

A **Machine Learning web application** that predicts which **New York City borough** (Manhattan, Brooklyn, Queens, Bronx, or Staten Island) a **311 complaint likely belongs to based on its text description**.

This project uses **Natural Language Processing (NLP)** and a **Bidirectional LSTM (BiLSTM) deep learning model with GloVe embeddings** to analyze complaint descriptions and classify them into one of the five NYC boroughs.

---

# 🎯 Features

### 🔮 Borough Prediction
- Enter a complaint description
- Predicts the most likely NYC borough
- Displays **probability scores for all boroughs**

### 📊 Analytics Dashboard
- Interactive charts showing complaint distribution
- Visual insights across boroughs using **Plotly**

### 🌎 Complaint Heatmap
- Geographic visualization of complaint density
- Built using **Folium maps**

### 📝 Prediction History
- Tracks prediction history during the session
- Allows users to review previous inputs and results

---

# 🛠️ Tech Stack

### Frontend
- Streamlit

### Machine Learning
- TensorFlow
- Keras

### Model
- Bidirectional LSTM (BiLSTM)
- GloVe Word Embeddings

### Visualization
- Plotly
- Folium

### Data Processing
- Pandas
- NumPy

---

# 📋 Prerequisites

Make sure you have the following installed:

- Python **3.8 or higher**
- pip package manager

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Ayush20Thakur/NYC-311-Borough-Classifier-ML-Project.git
cd NYC-311-Borough-Classifier-ML-Project
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows
```bash
venv\Scripts\activate
```

### macOS/Linux
```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🎮 Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

Then open your browser and go to:

```
http://localhost:8501
```

---

# 🧭 Application Tabs

### 1️⃣ Prediction
- Enter a complaint description
- Get borough predictions with probability scores

### 2️⃣ Dashboard
- View analytics and distribution charts
- Interactive visualization of complaint patterns

### 3️⃣ Heatmap
- Explore complaint density geographically across NYC

---

# 📊 Model Details

**Model Architecture:**  
Bidirectional LSTM (BiLSTM)

**Embeddings:**  
GloVe (Global Vectors for Word Representation)

**Task:**  
Multi-class classification (5 NYC boroughs)

**Input:**  
Text description of a 311 complaint

**Output:**  
Predicted borough with confidence scores

---

# 📁 Project Structure

```
NYC-311-Borough-Classifier-ML-Project/

├── app.py
├── my_bilstm_model.keras
├── tokenizer.pkl
├── requirements.txt
├── test_load.py
└── README.md
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Submit a Pull Request

---

# 📝 License

This project is licensed under the **MIT License**.

---

# 👤 Author

**Syed Zohaib Karim**


---

# 🙏 Acknowledgments

- **NYC Open Data** for the 311 complaint dataset
- **TensorFlow & Keras teams**
- **Streamlit community**

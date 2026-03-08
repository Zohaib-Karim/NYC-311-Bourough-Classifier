# NYC 311 Complaint Borough Classifier 🗽

A machine learning web application that predicts which NYC borough (Manhattan, Brooklyn, Queens, Bronx, or Staten Island) a 311 complaint likely belongs to based on its text description.

## 🎯 Features

- **🔮 Prediction**: Enter complaint text and get borough predictions with probability scores
- **📊 Dashboard**: Visualize complaint distribution across boroughs with interactive charts
- **🌎 Heatmap**: Geographic visualization of complaint density across NYC
- **📝 History**: Track your prediction history during the session

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **ML Framework**: TensorFlow/Keras
- **Model**: BiLSTM (Bidirectional LSTM) with GloVe embeddings
- **Visualization**: Plotly, Folium
- **Data Processing**: Pandas, NumPy

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Ayush20Thakur/NYC-311-Borough-Classifier-ML-Project.git
cd NYC-311-Borough-Classifier-ML-Project
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install required packages:
```bash
pip install -r requirements.txt
```

## 🎮 Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Choose from three tabs:
   - **Prediction**: Enter complaint text or use example complaints
   - **Dashboard**: View analytics and distribution charts
   - **Heatmap**: Explore geographic complaint patterns

## 📊 Model Details

- **Architecture**: Bidirectional LSTM
- **Embeddings**: GloVe (Global Vectors for Word Representation)
- **Task**: Multi-class classification (5 NYC boroughs)
- **Input**: Text descriptions of 311 complaints
- **Output**: Borough prediction with confidence scores

## 📁 Project Structure

```
NYC-311-Borough-Classifier-ML-Project/
├── app.py                    # Main Streamlit application
├── my_bilstm_model.keras     # Trained BiLSTM model
├── tokenizer.pkl             # Tokenizer for text preprocessing
├── requirements.txt          # Python dependencies
├── test_load.py             # Model testing script
└── README.md                # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Ayush Thakur**
- GitHub: [@Ayush20Thakur](https://github.com/Ayush20Thakur)

## 🙏 Acknowledgments

- NYC Open Data for 311 complaint dataset
- TensorFlow and Keras teams
- Streamlit community

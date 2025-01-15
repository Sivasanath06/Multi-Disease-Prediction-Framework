# README.txt

## Multi-Disease Prediction Framework

### Project Overview
This project implements a multi-disease prediction framework using advanced machine learning and deep learning techniques. It is designed to predict the likelihood of diseases such as Diabetes, Lung Cancer, Heart Disease, Kidney Disease, Malaria, and Pneumonia. The system utilizes robust preprocessing methods, exploratory data analysis (EDA), and a diverse range of models tailored to the nature of the datasets.

---

### Features
- **Preprocessing and EDA**: Ensures high-quality datasets for modeling.
- **Model Diversity**:
  - Tabular Data: CatBoost, Random Forest, SVC.
  - Image Data: DenseNet121, EfficientNet_B0, ResNet18.
- **User-Friendly Interface**: Provides predictions via a web-based platform using Django (Backend) and HTML/CSS/JS (Frontend).
- **Disease-Specific Optimizations**:
  - Diabetes and Kidney Disease: CatBoost.
  - Lung Cancer: Support Vector Classifier (SVC).
  - Heart Disease: Random Forest.
  - Malaria and Pneumonia: Convolutional Neural Networks (CNNs).

---

### System Requirements
- **Programming Language**: Python 3.8+
- **Libraries**:
  - Machine Learning: Scikit-learn, XGBoost, CatBoost.
  - Deep Learning: TensorFlow or PyTorch.
  - Data Processing: NumPy, Pandas.
  - Visualization: Matplotlib, Seaborn.
  - Web Framework: Django/Flask.
- **Hardware Requirements**:
  - For image-based models: GPU-enabled systems are recommended for faster training.

---

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-repo/multi-disease-prediction.git
   cd multi-disease-prediction
   ```
2. Install required Python libraries:
   ```
   pip install -r requirements.txt
   ```
3. Set up the database and apply migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Start the web server:
   ```
   python manage.py runserver
   ```
5. Access the application at `http://127.0.0.1:8000/`.

---

### Usage
1. **Input Data**:
   - For tabular data (e.g., Diabetes, Kidney Disease), input patient metrics such as blood pressure, glucose levels, etc.
   - For image-based data (e.g., Malaria, Pneumonia), upload medical images (e.g., X-rays, cell images).
2. **Receive Predictions**:
   - The system provides disease probabilities and recommendations.
   - If the risk is high, consult a healthcare professional.

---

### Results
Key highlights from the models:
- **Diabetes**: CatBoost achieved 92.88% accuracy.
- **Lung Cancer**: SVC achieved 98% accuracy.
- **Heart Disease**: Random Forest achieved 95% accuracy.
- **Kidney Disease**: CatBoost achieved 98% accuracy.
- **Malaria**: DenseNet121 and EfficientNet_B0 achieved 99% accuracy.
- **Pneumonia**: ResNet18 achieved 89.42% accuracy.

---

### Future Work
- Expanding datasets to include larger and more diverse populations.
- Incorporating multimodal data for holistic predictions.
- Enhancing model interpretability for better integration with clinical workflows.

---

### Authors
- Sivasanath Kumar M
- Sandeep N
- Mentor: Dr. Priyanka Dwivedi
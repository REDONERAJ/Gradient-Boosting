# 🍄 Mushroom Edibility Prediction (Gradient Boosting + Flask)

This project is a **web-based machine learning application** that predicts whether a mushroom is **edible** or **poisonous** based on a small set of descriptive features.  
It uses a **Gradient Boosting Classifier** trained on the Mushroom dataset from the UCI Machine Learning Repository.

The model has been optimized for **fast and easy user input**, requiring only **5 categorical features** to make predictions instantly.

---

## 🔹 Features
- Gradient Boosting Classifier trained on the UCI Mushroom dataset
- Uses **only 5 categorical inputs** for quick predictions:
  1. Cap Shape  
  2. Cap Color  
  3. Bruises  
  4. Odor  
  5. Habitat  
- Clean Flask UI with dropdown options for each feature
- Instant prediction output: **Edible** or **Poisonous**

---

## 📂 Project Structure
```mushroom-gradient-boosting-minimal/
│
├── model.py # Trains and saves Gradient Boosting model
├── app.py # Flask web application
├── mushroom_gradient_boosting_minimal.pkl # Saved model + encoders
├── templates/
│ └── index.html # HTML form with 5 dropdown inputs
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

## 📊 Dataset
- **Source:** [UCI Machine Learning Repository – Mushroom Dataset](https://archive.ics.uci.edu/ml/datasets/mushroom)
- **Instances:** 8,124  
- **Classes:** Edible (0) / Poisonous (1)  
- **Features used in this app:**
  - `cap-shape`: bell, conical, convex, flat, knobbed, sunken  
  - `cap-color`: brown, buff, cinnamon, gray, green, pink, purple, red, white, yellow  
  - `bruises`: bruises present (t) or no (f)  
  - `odor`: almond, anise, creosote, fishy, foul, musty, none, pungent, spicy  
  - `habitat`: grasses, leaves, meadows, paths, urban, waste, woods

---

## 🖥 Prediction Output
- **"Edible"** – Safe to consume  
- **"Poisonous"** – Unsafe to consume  

---

## 📦 Requirements
Flask
scikit-learn
pandas
numpy
joblib


---

## 📷 Screenshot
<img width="1366" height="633" alt="Screenshot 2025-08-12 001918" src="https://github.com/user-attachments/assets/fcf74c79-dcb1-4b85-b37d-6db58898aa01" />
<img width="1366" height="647" alt="Screenshot 2025-08-12 001934" src="https://github.com/user-attachments/assets/ac70d6aa-bca1-4a1b-a012-34529886a28e" />
<img width="1366" height="641" alt="Screenshot 2025-08-12 001944" src="https://github.com/user-attachments/assets/aad4dd94-6970-457e-8470-8ebe9a1bf5a0" />


---

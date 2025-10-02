# 🌊 AquaPredict - AI-based Molecular Solubility Predictor

AquaPredict is a simple **Machine Learning + Flask Web App** that predicts the **aqueous solubility (logS)** of molecules based on four molecular descriptors:  
- **MolLogP** (Hydrophobicity)  
- **MolWt** (Molecular Weight)  
- **NumRotatableBonds**  
- **AromaticProportion**  

The app provides a **clear interpretation** of solubility:  
- 🟢 **Highly Soluble**  
- 🟡 **Moderately Soluble**  
- 🔴 **Poorly Soluble**  

---

## 🚀 Features
- Train a **Linear Regression ML model** on molecular descriptor data.  
- Flask-based **interactive web app** with user input form.  
- Live predictions with **color-coded solubility results**.  
- User-friendly **Bootstrap UI**.  
- Can be deployed to **Heroku, Render, or mobile-friendly PWA** in the future.  

---

## 🛠️ Tech Stack
- **Python** 🐍  
- **Flask** (Backend + Web Server)  
- **Scikit-learn** (Machine Learning)  
- **Joblib** (Model persistence)  
- **NumPy**  
- **Bootstrap 5** (Frontend styling) 

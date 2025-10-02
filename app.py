from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get inputs
        MolLogP = float(request.form["MolLogP"])
        MolWt = float(request.form["MolWt"])
        NumRotatableBonds = float(request.form["NumRotatableBonds"])
        AromaticProportion = float(request.form["AromaticProportion"])

        # Make prediction
        input_array = np.array([[MolLogP, MolWt, NumRotatableBonds, AromaticProportion]])
        prediction = model.predict(input_array)[0]

        # Interpret solubility + choose color
        if prediction > 0:
            solubility = "Highly Soluble in water 💧"
            alert_class = "success"   # green
        elif prediction > -2:
            solubility = "Moderately Soluble ⚖️"
            alert_class = "warning"   # yellow
        else:
            solubility = "Poorly Soluble ❌"
            alert_class = "danger"    # red

        result = f"Predicted logS: {prediction:.3f} → {solubility}"

        return render_template("index.html", prediction_text=result, alert_class=alert_class)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}", alert_class="danger")

if __name__ == "__main__":
    app.run(debug=True)

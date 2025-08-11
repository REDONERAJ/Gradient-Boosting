from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model, label_encoders = joblib.load('mushroom_gradient_boosting_minimal.pkl')

features = ["cap-shape", "cap-color", "bruises", "odor", "habitat"]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        input_data = []
        for f in features:
            val = request.form[f]
            val_encoded = label_encoders[f].transform([val])[0]
            input_data.append(val_encoded)
        pred = model.predict([input_data])[0]
        prediction = "Poisonous" if pred == 1 else "Edible"
    options = {f: label_encoders[f].classes_.tolist() for f in features}
    return render_template("index.html", features=features, options=options, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "http://localhost:5000/convert"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        celsius = request.form.get("celsius")

        # Call the API app
        api_response = requests.get(API_URL, params={"c": celsius})

        if api_response.status_code == 200:
            result = api_response.json()["fahrenheit"]
        else:
            result = "Error contacting API"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, port=8000)


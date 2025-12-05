from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/convert")
def convert():
    celsius = request.args.get("c", type=float)

    if celsius is None:
        return jsonify({"error": "Please supply ?c=value"}), 400

    fahrenheit = (celsius * 9/5) + 32
    return jsonify({"fahrenheit": fahrenheit})

if __name__ == "__main__":
    app.run(debug=True, port=5000)


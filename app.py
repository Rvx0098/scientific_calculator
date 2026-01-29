from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

SAFE_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "ln": math.log,
    "sqrt": math.sqrt,
    "pi": math.pi,
    "e": math.e,
    "pow": pow,
    "abs": abs
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    expr = data.get("expression", "")

    try:
        result = eval(expr, {"__builtins__": None}, SAFE_FUNCTIONS)
        return jsonify({"result": result})
    except:
        return jsonify({"result": "Error"})

if __name__ == "__main__":
    app.run(debug=True)


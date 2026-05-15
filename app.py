import ast
import math
import operator
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

ALLOWED_FUNCTIONS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "ln": math.log,
    "sqrt": math.sqrt,
}

ALLOWED_CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}

ALLOWED_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def evaluate_expression(expression):
    """Evaluate calculator expressions without exposing Python builtins."""
    tree = ast.parse(expression, mode="eval")
    return _evaluate_node(tree.body)


def _evaluate_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.Name) and node.id in ALLOWED_CONSTANTS:
        return ALLOWED_CONSTANTS[node.id]

    if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)
        return ALLOWED_OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_UNARY_OPERATORS:
        return ALLOWED_UNARY_OPERATORS[type(node.op)](_evaluate_node(node.operand))

    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        function = ALLOWED_FUNCTIONS.get(node.func.id)
        if function and len(node.args) == 1:
            return function(_evaluate_node(node.args[0]))

    raise ValueError("Unsupported expression")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True) or {}
    expression = data.get("expression", "")

    try:
        result = evaluate_expression(expression)
        return jsonify({"result": result})
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError):
        return jsonify({"result": "Error"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

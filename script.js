let display = document.getElementById("display");
let expression = "";

function press(value) {
    if (display.innerText === "0") expression = "";
    expression += value;
    display.innerText = expression;
}

function clearDisplay() {
    expression = "";
    display.innerText = "0";
}

function calculate() {
    fetch("/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ expression: expression })
    })
    .then(res => res.json())
    .then(data => {
        display.innerText = data.result;
        expression = data.result.toString();
    });
}

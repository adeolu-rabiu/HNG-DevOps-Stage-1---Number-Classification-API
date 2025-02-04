from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

# Initialize Flask App
app = Flask(__name__)
CORS(app)  # Enable CORS

# Utility Functions
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is perfect."""
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = list(map(int, str(abs(n))))
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_digit_sum(n):
    """Calculate the sum of the digits of the number."""
    return sum(map(int, str(abs(n))))

def get_fun_fact(n):
    """Fetch a fun fact about the number from the Numbers API or generate custom fact if Armstrong."""
    if is_armstrong(n):
        digits = list(map(int, str(abs(n))))
        power = len(digits)
        calculation = " + ".join([f"{d}^{power}" for d in digits])
        return f"{n} is an Armstrong number because {calculation} = {n}"
    
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json", timeout=3)
        response.raise_for_status()
        return response.json().get("text", "No fun fact available.")
    except (requests.RequestException, ValueError):
        return "No fun fact available."

def classify_properties(n):
    """Classify the properties of the number."""
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("odd" if n % 2 else "even")
    return properties

# API Route
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num = request.args.get("number")

    # Input validation
    if not num or not (num.lstrip("-").isdigit()):
        return jsonify({"number": num, "error": True}), 400

    num = int(num)
    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": classify_properties(num),
        "digit_sum": get_digit_sum(num),
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(response), 200

# Main Application Entry Point
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)



from flask import Flask, request, render_template_string

app = Flask(__name__)

# ---------- HTML is stored right here as a string ----------
PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BMI Calculator</title>
    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
        rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container py-5" style="max-width: 500px;">
        <h1 class="text-center mb-4">BMI Calculator</h1>

        <form method="POST" class="mb-4">
            <div class="mb-3">
                <label class="form-label">Weight (kg)</label>
                <input type="text" name="weight" class="form-control" placeholder="e.g. 65">
            </div>
            <div class="mb-3">
                <label class="form-label">Height (m)</label>
                <input type="text" name="height" class="form-control" placeholder="e.g. 1.70">
            </div>
            <button type="submit" class="btn btn-primary w-100">Calculate BMI</button>
        </form>

        {% if error %}
            <div class="alert alert-danger">{{ error }}</div>
        {% endif %}

        {% if result %}
            <div class="alert alert-success text-center">
                <h4>Your BMI: {{ result.bmi }}</h4>
                <p class="mb-0">Category: <strong>{{ result.category }}</strong></p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""


def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        weight = request.form.get("weight", "")
        height = request.form.get("height", "")

        try:
            weight = float(weight)
            height = float(height)

            if weight <= 0 or height <= 0:
                error = "Please enter positive numbers only."
            else:
                bmi = calculate_bmi(weight, height)
                category = get_category(bmi)
                result = {"bmi": bmi, "category": category}

        except ValueError:
            error = "Please enter valid numbers (e.g. 65 or 1.7)."

    return render_template_string(PAGE, result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)

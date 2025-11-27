
from flask import Flask, render_template, request

app = Flask(__name__)

messages_A = [
    "Kiitos! Valitsit Vaihtoehto A.",
    "Hienoa, että pidät A:sta!",
    "A on suosittu valinta!"
]

messages_B = [
    "Kiitos! Valitsit Vaihtoehto B.",
    "B on hyvä valinta!",
    "B:llä on oma kannattajakuntansa!"
]

click_count_A = 0
click_count_B = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global click_count_A, click_count_B
    message = None

    if request.method == "POST":
        vote = request.form.get("vote")
        if vote == "A":
            message = messages_A[click_count_A % len(messages_A)]
            click_count_A += 1
        elif vote == "B":
            message = messages_B[click_count_B % len(messages_B)]
            click_count_B += 1

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)

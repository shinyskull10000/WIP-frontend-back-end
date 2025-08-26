from flask import Flask, render_template, request

app = Flask(__name__)

stored_data = None

@app.route("/", methods=["GET", "POST"])
def index():
    global stored_data
    if request.method == "POST":
        stored_data = "WHO"
    return render_template("index.html", data=stored_data)

if __name__ == "__main__":
    app.run(debug=True)

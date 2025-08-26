from flask import Flask, render_template

app = Flask(__name__)

# Let's say this is our "stored information"
stored_data = "who?"

@app.route("/")
def index():
    return render_template("index.html", data=stored_data)

#if __name__ == "__main__":
    # Render needs host="0.0.0.0"
    #app.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    app.run()
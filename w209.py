from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dash_time")
def dash_time():
    return render_template("dash_time.html")

@app.route("/dash_var")
def dash_var():
    return render_template("dash_var.html")

@app.route("/dash_age")
def dash_age():
    return render_template("dash_age.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")

@app.route("/sources")
def sources():
    return render_template("sources.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dash_1")
def dash_1():
    return render_template("dash_1.html")

@app.route("/dash_2")
def dash_2():
    return render_template("dash_2.html")

@app.route("/dash_3")
def dash_3():
    return render_template("dash_3.html")

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

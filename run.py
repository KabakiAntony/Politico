from app import create_app
from flask import render_template

app = create_app()


@app.route("/")
def root():
    """Return a welcome message to the users of this app"""
    return render_template("index.html")

@app.route("/voter")
def voter():
    """Return a welcome message to the users of this app"""
    return render_template("voter-dash.html")
if __name__ == "__main__":
    app.run(debug=True)

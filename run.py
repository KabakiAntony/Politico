from app import create_app

app = create_app()


@app.route("/")
def root():
    """Return a welcome message to the users of this app"""
    return "<p  style=""text-align:center"">"\
        "Hello and welcome to Politico. "\
        "To use the endpoints in here use /api/v1 or /api/v2 "\
        "done by @kabakikiarie </p>"

if __name__ == "__main__":
    app.run(debug=True)

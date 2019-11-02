from app import create_app
from flask import render_template

app = create_app()


@app.route("/")
def root():
    """Return a welcome message to the users of this app"""
    return '<h2 style="color:white;text-align:center;background:black;">Hello and welcome to Politico\
        done by <a style="color:white;" href="https://twitter.com/kabakikiarie">Kabaki Kiarie</a></h2>\
        <h3 style="text-align:center;">We have two versions /api/v1 and /api/v2</h3>\
        <h4 style="text-align:center;">Resources are /parties and offices/</h4>'
 
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import render_template, render_template_string
from jinja2 import Template



app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("child.html")






if __name__ == "__main__":
    app.run(debug=True, port=2745) 
from flask import Flask
from flask import render_template, render_template_string
from jinja2 import Template

from pymongo import MongoClient

client = MongoClient("0.0.0.0:27018")

database_apple = client.refurbApple
collection_product = database_apple['product']


app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route('/')
def landingPage():
    return render_template("landing_page.html")

@app.route('/show_refurb')
def refurbComparaisonPage():
    documents = collection_product.find({})
    response = []
    for document in documents:
        response.append(document)

    print(response)

    return render_template("refurb_page.html", products = response)






if __name__ == "__main__":
    app.run(debug=True, port=2745) 
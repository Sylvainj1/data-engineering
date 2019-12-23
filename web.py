from flask import Flask, redirect, url_for
from flask import render_template, render_template_string, request
from jinja2 import Template

from pymongo import MongoClient

from elasticsearch import Elasticsearch

ES_LOCAL = True

es_client = Elasticsearch(hosts=["localhost" if ES_LOCAL else "elasticsearch"])

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

    return render_template("refurb_page.html", products = response)


@app.route('/search/', methods=['GET', 'POST'])
def searchPage():

    if request.method == 'POST':
        search_term = request.form["input"]
        res = es_client.search(
            index="product", 
            size=20, 
            body={
                "query": {
                    "multi_match" : {
                        "query": search_term, 
                        "fields": [
                            "title", 
                            "currentPrice",
                        ] 
                    }
                }
            }
        )
        return render_template('search.html', res=res )
    #   return redirect(url_for('searchPage'))
    else:
      return render_template('search.html')






if __name__ == "__main__":
    app.run(debug=True, port=2745) 
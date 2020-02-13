from flask import Flask, redirect, url_for
from flask import render_template, render_template_string, request
from jinja2 import Template

from pymongo import MongoClient

from elasticsearch import Elasticsearch

import pprint

import dash
import dash_core_components as dcc
import dash_html_components as html

import chart

ES_LOCAL = True

es_client = Elasticsearch(hosts=["localhost" if ES_LOCAL else "elasticsearch"])

client = MongoClient("0.0.0.0:27018")

database_apple = client.refurbApple
collection_product = database_apple['product']


app = Flask(__name__)

dash_app = dash.Dash(__name__, server=app, routes_pathname_prefix= '/dash/')

chart.GraphDash(dash_app=dash_app)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route('/')
def landingPage():
    return render_template("landing_page.html")


@app.route('/show_refurb/', methods=['GET', 'POST'])
def refurbComparaisonPage():
    documents = collection_product.find({})
    response = []
    for document in documents:
        response.append(document)

    if request.method == 'POST':
        search_term = request.form["input"]
        query = es_client.search(
            index="product",
            size=30,
            body={
                "query": {
                    "multi_match": {
                        "query": search_term,
                        "fields": [
                            "title",
                            "currentPrice",
                        ]
                    }
                }
            }
        )

        #es_client.search(index="suggest_product", body=suggest, size=10)
        return render_template('refurb_page.html', res=query)
    else:
        return render_template("refurb_page.html", products=response)


@app.route('/suggest_product/suggest', methods=['GET', 'POST'])
def suggest_method():
    if request.method == 'GET':
        #permet de recuperer le query passé en url grace au JavaScript
        req = request.args.get('search')

        query = es_client.search(
            index="suggest_product",
            size=5,
            body={
                "query": {
                    "multi_match": {
                        "query": req,
                        "type": "bool_prefix",
                        "fields": [
                            "title",
                            "title._2gram",
                            "title._3gram"
                        ]
                    }
                }
            }
        )
        return query
    else:
        return "La méthode devrait renvoyer un index ES à la suite d'un GET pas d'un POST"


if __name__ == "__main__":
    
    app.run(debug=True, port=2745)
    # dash_app.run_server(debug=True, port=2745)

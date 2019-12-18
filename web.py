from flask import Flask
from flask import render_template, render_template_string
from jinja2 import Template

from pymongo import MongoClient

client = MongoClient("0.0.0.0:27018")

database_apple = client.refurbApple

collectionName = database_apple.list_collection_names()

collection_mac = database_apple["mac"]
collection_iphone = database_apple["iphone"]
collection_ipad = database_apple["ipad"]

iphonedoc = collection_iphone.find_one()
ipaddoc = collection_ipad.find_one()
macdoc = collection_mac.find_one()


app = Flask(__name__)

@app.route('/')
def landingPage():
    return render_template("landing_page.html")

@app.route('/show_refurb')
def refurbComparaisonPage():
    return render_template("refurb_page.html", iphone = iphonedoc, ipad= ipaddoc, mac = macdoc)






if __name__ == "__main__":
    app.run(debug=True, port=2745) 
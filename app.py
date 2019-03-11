import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "cook_book"
app.config["MONGO_URI"] = "mongodb+srv://Geronimo1992:CrazyHorse1992@myfirstcluster-ljwxr.mongodb.net/cook_book?retryWrites=true"

mongo = PyMongo(app)

recipes = mongo.db.recipes



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
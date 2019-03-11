import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "cook_book"
app.config["MONGO_URI"] = "mongodb+srv://Geronimo1992:CrazyHorse1992@myfirstcluster-ljwxr.mongodb.net/cook_book?retryWrites=true"

mongo = PyMongo(app)

recipes = mongo.db.recipes

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template('index.html', recipes = mongo.db.recipes.find())

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    return render_template('recipe.html', recipes = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
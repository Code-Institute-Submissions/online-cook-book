import os
from flask import Flask, render_template, redirect, request, url_for, session
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
    recipes = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template('recipe.html', recipes=recipes)
    
@app.route('/breakfast_recipes')
def breakfast_recipes():
    return render_template('breakfast.html', recipes = mongo.db.recipes.find())
    
@app.route('/lunch_recipes')
def lunch_recipes():
    return render_template('lunch.html', recipes = mongo.db.recipes.find())
    
@app.route('/dinner_recipes')
def dinner_recipes():
    return render_template('dinner.html', recipes = mongo.db.recipes.find())
   
@app.route('/contribute_recipes')
def contribute_recipes():
    return render_template('contribute.html', recipes= mongo.db.recipes.find())

@app.route('/add_recipes', methods=['POST'])
def add_recipes():
    con_recipe = mongo.db.recipes
    con_recipe.insert_one({
        "meal_name": request.form.get("meal_name"),
        "preparation": request.form.get("preparation"),
        "description": request.form.get("description"),
        "author": {
                "last_name": request.form.get("last_name"),
                "name": request.form.get("name")
            },
        "category_course": request.form.get("category_course"),
        "ingredients":request.form.get("ingredients"),
        "macros":{
                    "fat":request.form.get("fat"),
                    "calories":request.form.get("calories"),
                    "proteins":request.form.get("proteins"),
                    "carbs":request.form.get("carbs")
                },
        "url_img": request.form.get("url_img"),
        "upvote": 1,
        "downvote": 1
})
    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
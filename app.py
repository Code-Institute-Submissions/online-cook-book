import os
from flask import Flask, render_template, redirect, request, url_for, session, g
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import json 
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config["MONGO_DBNAME"] = "cook_book"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route("/")
@app.route('/session_user')
def session_user():
    return render_template("user.html")
    
@app.route('/get_username', methods=["GET", "POST"])
def get_username():
    if request.method == "POST":
        session["username"] = request.form["username"]
    return redirect(url_for("get_recipes"))

@app.before_request
def before_request():
    g.user=None
    if "username" in session:
        g.user = session["username"]

@app.route('/get_recipes')
def get_recipes():
    if g.user:
        return render_template('index.html', recipes = mongo.db.recipes.find().sort("upvote", -1))
    else:
        return redirect(url_for("session_user"))

@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    if g.user:
        recipes = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
        return render_template('recipe.html', recipes=recipes)
    else:
        return redirect(url_for("session_user"))
    
@app.route('/filter_courses?')
def breakfast_recipes():
    if g.user:
        return render_template('breakfast.html', recipes = mongo.db.recipes.find().sort("upvote", -1))
    else:
        return redirect(url_for("session_user"))
    
@app.route('/lunch_recipes')
def lunch_recipes():
    if g.user:
        return render_template('lunch.html', recipes = mongo.db.recipes.find().sort("upvote", -1))
    else:
        return redirect(url_for("session_user"))
    
@app.route('/dinner_recipes')
def dinner_recipes():
    if g.user:
        return render_template('dinner.html', recipes = mongo.db.recipes.find().sort("upvote", -1))
    else:
        return redirect(url_for("session_user"))
   
@app.route('/contribute_recipes')
def contribute_recipes():
    if g.user:
        return render_template('contribute.html', recipes= mongo.db.recipes.find())
    else:
        return redirect(url_for("session_user"))

@app.route('/add_recipes', methods=['POST'])
def add_recipes():
    if g.user:
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
            "user": session["username"]
        })
        return redirect(url_for('get_recipes'))
    else:
        return redirect(url_for("session_user"))

@app.route('/edit_page')
def edit_page():
    if g.user:
        return render_template('edit_page.html', recipes = mongo.db.recipes.find().sort("upvote", -1))
    else:
        return redirect(url_for("session_user"))

@app.route('/delete_page')
def delete_page():
    if g.user:
        return render_template('delete_page.html', recipes = mongo.db.recipes.find().sort("upvote", -1))
    else:
        return redirect(url_for("session_user"))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    if session['username']:
        recipes = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
        if session['username'] == recipes['user']:
            mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
        return redirect(url_for('delete_page'))
    else:
        return redirect(url_for("session_user"))
    
@app.route('/edit_page_form/<recipe_id>')
def edit_page_form(recipe_id):
    if g.user:
        return render_template('edit_page_form.html', recipes = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}))
    else:
        return redirect(url_for("session_user"))

#edit recipe function
@app.route('/edit_recipe/<recipe_id>', methods=["POST"])
def edit_recipe(recipe_id):
    if g.user:
        recipes = mongo.db.recipes
        recipes.update({"_id": ObjectId(recipe_id)},
            {"$set": {
            "meal_name": request.form.get("meal_name"),
            "preparation": request.form.get("preparation"),
            "description": request.form.get("description"),
            "author": {
                "last_name": request.form.get("last_name"),
                "name": request.form.get("name")
            },
            "category_course": request.form.get("category_course"),
            "ingredients": request.form.get("ingredients"),
            "macros": {
                "fat": request.form.get("fat"),
                "calories": request.form.get("calories"),
                "proteins": request.form.get("proteins"),
                "carbs": request.form.get("carbs")
            },
            "url_img": request.form.get("url_img")
            }})
        return redirect(url_for('edit_page'))
    else:
        return redirect(url_for("session_user"))

@app.route('/upvote/<recipe_id>', methods=["POST"])
def upvote(recipe_id):
    if g.user:
        recipes=mongo.db.recipes
        recipes.update({"_id": ObjectId(recipe_id)},{"$inc": {"upvote": 1}})
        return redirect(url_for("get_recipes"))
    else:
        return redirect(url_for("session_user"))

@app.route('/downvote/<recipe_id>', methods=["POST"])
def downvote(recipe_id):
    if g.user:
        recipes=mongo.db.recipes
        recipes.update({"_id": ObjectId(recipe_id)},{"$inc": {"upvote": -1}})
        return redirect(url_for("get_recipes"))
    else:
        return redirect(url_for("session_user"))

@app.route('/show_popular_courses')
def show_popular_courses():
    if g.user:
        recipes= mongo.db.recipes.find().sort("upvote", -1)
        data = []
        for recipe in recipes:
            print(recipe)
            data.append({'category_course': recipe['category_course']})
            data.append({'upvote': recipe['upvote']})
        
        with open("data_from_python.json", "w") as write_file:
            json.dump(data, write_file)
        return render_template("chart.html")
    else:
        return redirect(url_for("session_user"))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
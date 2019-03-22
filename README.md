# Interactive Font End Development Milestone Project
This an online cookbook that is made for people who like to live a healthy lifestyle but don't necessarly want to eat brocolli and boiled chikcen every day.
The recipes are made out of alternatives like stevia instead of sugar, olive oil instead of other less heamthy oils, nuts, seeds and many other ingredients are used to replace the traditional ones,
enjoy!

# UX
The design of the website is simple and it is straight forward how to use it. It is responsive and it has been developed with the end user in mind. The navigation has bg image and the text is slightly grey.
Some of the text in the navabr is also white. The same bg image has been used on the footer and forms just to keep it clean. The home page has a background color of seashell, which is slightly 
different from white. Text throughout the website is black and items have a nice hover effect on all pages. The text is aligned left when above 768px and aligned in the middle below that point.

# Features
* User can add new recipes by clicking on the contribute link in the navabr
* User can edit recipes by clicking on the edite recipes link in the navbar
* User can delete recipes (only the ones he added while active in his session) by clicking on the delte link in the navbar
* User can naviagte through courses by choosing options in navabar (breakfast, lunch, dinner) 
* When you click on the recipe, you get directed to the details of that recipe which include a, image, description, macronutrients, ingredients, instructions, author name. You can also like and 
dislike a recipe. This will then rank the recipe on the website dpeneding on the amounts of likes it gets.

Wireframes can be found [here]: (https://github.com/Geronimo1992/online-cook-book/tree/master/WIREFRAMES)

# Techologies Used
* [HTML]: (https://www.w3schools.com/html/html_intro.asp) has been used for the structure of the page
* [CSS]: (https://www.w3schools.com/css/) has been used for styling
* [CSS]: (https://getbootstrap.com/) has been used for the navigation bar, the grid layout and forms
* [Python]: (https://www.python.org/) has been used to write the backend code
* [Flask]: (http://flask.pocoo.org/) has been used to facilitate the backend development
* [Jinja]: (http://jinja.pocoo.org/) has been used to be able to write logic in the HTML document itself
* [Mongo Db]: (https://www.mongodb.com/) has been used to store the data of the website
* [PyMongo]: (https://api.mongodb.com/python/current/) has been used to be able to work with the database from a python file instead of the command line

# Testing

* HTML has been tested on [W3C]: (https://validator.w3.org/nu/#textarea)
* CSS has been tested on [W3C]: (https://jigsaw.w3.org/css-validator/validator)
* Python has been tested on [pep8 online check]: (http://pep8online.com/)
* Testing of every views status code has been done. Testing of user session has also been done. See  [here]: (https://github.com/Geronimo1992/online-cook-book/blob/master/app_tests.py)
* Manual tests have been performed as well (checking links, forms, etc)

# deployment
Code can be found on [Github]: (https://github.com/Geronimo1992/online-cook-book)
Website has been deployed and can be found on [Heroku]: (https://cookbook-flask-mls.herokuapp.com/)

# Credits

* Many times i refered to the python documentation
* During the project i refered to the flask docs as well which have been a huge help
* A big thank you to my mentor for planning and helping with the projects
* A big thanks to tutor support for helping me out with many difficult issues.
* A tutorial has been taken for learning how to use context varibles and sessions on [Youtube]: (https://www.youtube.com/watch?v=eBwhBrNbrNI)
* Many more resources have been consulted online for advice and python syntax (stackoverflow, pyhton pep8, blogs, etc) so thank you to all the authors!
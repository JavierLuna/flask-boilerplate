# Flask-Boilerplate
My current flask-app skeleton. Works with Python 3.

## Instructions
I'm gonna try to bring you guys a one-liner, but until then there is this script hosted in a public [Gist](https://gist.github.com/JavierLuna/494cd8694498346e287b13d5d0733797)

You have to have ```git``` installed as well as ```python3``` for this to work.

You can either download it manually or use fancy commands like ```curl``` or ```wget```:

```
curl -O https://gist.githubusercontent.com/JavierLuna/494cd8694498346e287b13d5d0733797/raw/473a7669e0e30bf0cd5965f72c26c384bcaa810f/flask-boilerplate.sh
```
or

```
wget https://gist.githubusercontent.com/JavierLuna/494cd8694498346e287b13d5d0733797/raw/473a7669e0e30bf0cd5965f72c26c384bcaa810f/flask-boilerplate.sh
```


This will download ```flask-skeleton.sh``` (good file, better script) which you have to make executable with this my dudes:

```chmod +x flask-skeleton.sh```

And then, finally, run it. Seriously, you deserve it!

```./flash-skeleton.sh```

The script will request *His Dudeness* a name for *His* project and then a path to the python executable you want to use (no biggies about that, it will create such a nice virtual environment, you won't believe)

Then, it will create and install all my favorite libraries! For your only amusement!

I'll explain the project tree in the next section

## Behold! The project tree
This, right here, is the project tree my marvelous script will create for you.
But don't be fooled, it isn't a real tree. It is an ASCII representation of the structure of the project.

<pre>
.
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── __init__.py
│   │       ├── auth
│   │       │   ├── __init__.py
│   │       │   ├── schemas.py
│   │       │   └── views.py
│   │       ├── errors.py
│   │       ├── exceptions.py
│   │       ├── father
│   │       │   ├── __init__.py
│   │       │   ├── schemas.py
│   │       │   └── views.py
│   │       ├── son
│   │       │   ├── __init__.py
│   │       │   ├── schemas.py
│   │       │   └── views.py
│   │       └── utils.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── father.py
│   │   ├── son.py
│   │   └── user.py
│   ├── templates
│   │   └── index.html
│   └── views
│       ├── __init__.py
│       ├── errors.py
│       ├── exceptions.py
│       └── hello.py
├── config.py
├── env
│   
├── manage.py
├── Pipfile
├── Pipfile.lock
├── tests
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── __init__.py
│   │       ├── test_auth.py
│   │       ├── test_father.py
│   │       └── test_son.py
│   └── utils.py
└── wsgi.py
</pre>

### The concept behind this skeleton
I really like python for a bunch of reasons but the most important one is its philosophy. It is simple, concise and _explicit_.

I tried other web frameworks like [Django](https://www.djangoproject.com/), but find them very confusing as they do a lot of heavy lifting behind the scenes, often hiding the logic behind it. Don't get me wrong, I like the project and know they have fantastic documentation, but the fact that I have to go looking at docs to get a grasp of what's going on in my own project really slows me down. And I like things very explicit.

Furthermore, I find several things very wrong about Django's tree (let me rant a little):

* **Models must be separated from all views and "serializers"**: Ladies and gentleman, if it follows the MVC pattern, why are they so tied down? Let them models breathe!. This leads to the development of monolithic web applications which is very bad for scaling. Even with all your fancy whale-swarm thingies.
* **Web routes' level of abstraction is too high:** I get you are going for the clean look and separate a bit routes from code, but maybe this slows down the general development or debugging of the app or the beginners learning curve to the project (in addition of the steeper django's learning curve).
* **The whole tree is so rigid and strict!:** Due to all hidden heavy lifting we get ourselves stuck with a default project-tree which doesn't really give us much freedom to play around. This is good if you like to boost your ego writing programming articles at [Medium](https://medium.com/) about how you did api versioning _right_ in Django, but if this ain't your thing it can be a little frustrating. The tree that doesn't bend, breaks. Be flexible, be like bamboo.

With this said, please allow me to introduce... my skeleton.

In the root of the directory we find several packages and files:

### Config.py
There goes our configuration file. Here we can find all the classes containing the different configuration settings we'll use.

Personally, I like my whole team having the same kind of configuration, so I only placed three different settings: **Development, Testing and Production**. All three configuration extends a very interesting method, **init_app**, which receives the app at the beginning of the configuration process, so you can execute custom code depending on the configuration selected. For example, running Sentry only in Production.


### Manage.py
Okay, maybe I've robbed this one from Django. It is so handy to have a manage script though!
The five commands we are going to use the most are:

##### Database and migration repository creation
```
python manage.py db init
```
##### Create a migration from existing models and database
```
python manage.py db migrate
```
##### Apply pending migrations to database
```
python manage.py db upgrate
```

##### Runs the server in localhost:5000
```
python manage.py runserver
```

And my most fav one:
```
python manage.py shell
```

The thing about this last one is that you can load whatever variables you want beforehand into the shell session. It is so useful to have already in context models like User...


### App directory
Home of our beloved web app! This point is the big one, so I'll try to get straight to the point.

In the __init__.py file we can find the initialization of the application. First, we declare our libraries and then in our **create_app** factory we attach all things to the app object. This makes scalability much easier.

Here it also lives our **Model** package, holding our... models (yes, I wouldn't have guessed it either). Notice how files inside must be included in the __init__.py file located in the **Model** package. Them models can't even smell the controllers.

The **Templates** folder is where we put our Jinja infused HTML. You can configure it nicely in Pycharm too!


Now comes the interesting part:

**Api** and **Views** folders

 These two are two versions of the same concept, being api a much more complex one.
 
 In both we are going to store views (**views.py**), custom decorator and helper functions (**utils.py**), custom exceptions (**exceptions.py**) and custom error messages (**errors.py**) but in different layouts.
 
 Take into account that we are versioning the api using the route method (/api/version/resource/blabla), and we make use of the project tree so that the versioning and structure is as close as their routes.
 
 If the route for the resource ```Father``` is like this  ```/api/v1/father``` it will be resting in the **views.py** in the package father under **v1** which is, as well, under the **api** package (```api/v1/father/views.py```).
  SO INTUITIVE.
 
 In every api's endpoint I like to have two files: 
 
 * **views.py**: Here we find our endpoints.
* **schemas.py**: Here we have our schemas. Also named "serializers" by them Django people.

Also, in the api's __init__.py we find initialization of stuff like auth by token etc.

#### IMPORTANT TO REMEMBER: ALWAYS LOAD YOUR MODULES OR FILES IN THEIR PARENT'S __init__.py


### Tests
Y'all like tests too much to not cover them in my skeleton.

Just kidding, I've only coded a couple of tests as examples because this is really a boilerplate, and tests means more code to remove after the bootstrapping.
Test structure is kinda the same as the **api** one but easier to grasp so don't worry, you'll be fine.
One thing that is cool about this tests is that they run on an in-memory sqlite database, so they are fast! And fast to run tests mean more people liking tests, so it is a win win situation for everyone!

I've coded a little API test client because I don't know anything better. Please, enlighten me!


### wsgi.py
This teeny tiny script is used to deploy later on. Let it be!

### Pipfile and Pipfile.lock
I decided to start using [Pipenv](https://github.com/pypa/pipenv) for this skeleton instead of `pip`.
While I don't really like some aspects of `pipenv`, I think they are moving towards the right direction.
Resolution of dependencies and their respective subdependencies, dependencies hash checking and security scans are a must nowadays.
The usage of the tool is outside of this project, so I kindly suggest to read their [basics guide](https://docs.pipenv.org/en/latest/basics/).


## Farewell
I hope you like my project tree. I really do!
If not, you can always message me with the one you like so I could learn from you!

Also, I'm a beginner to bash scripting, so if you could help with the one-liner thing, or give me advice on my script, I would be so grateful!


Thank you guys.

Javier.

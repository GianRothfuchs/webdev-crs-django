# Setup

## Setting up a Project
Windows Setup for [virtual environment](https://docs.python.org/3/library/venv.html).
1. mkdir project folder "Project1" and cd inside to "Project1"
2. Create virtual environment `python -m venv Project1-env`, where Project1-env is the name.
3. activate the virtual environment `.\Project1-env\Scripts\activate`
4. Install Django inside the virtual environment `pip install django`
5. Check if Django is installed: `python -m django version`
6. Create Django project: `django-admin startproject Project1-Name`  
7. cd to newly created folder `Project1-Name`
8. rund python `python manage.py runserver`

MAC Setup for [virtual environment](https://docs.python.org/3/library/venv.html).
1. mkdir project folder "Project1" and cd inside to "Project1"
2. Create virtual environment `python3 -m venv Project1-env`, where Project1-env is the name.
3. activate the virtual environment `source Project1-env/bin/activate`
4. Install Django inside the virtual environment `pip install django`
5. Check if Django is installed: `python -m django version`
6. Create Django project: `django-admin startproject Project1-Name`  
7. cd to newly created folder `Project1-Name`
8. run python `python manage.py runserver`


Winhin dir where manage.py is located run:

```python
python3 manage.py runserver # To run the server
python3 manage.py makemigrations # To compile the migrations
python3 manage.py migrate  # To migrate the changes in Database
```


## Setting up an App within a Project

create app within project as a project can hold multiple apps. For this to work you need to cd into the Project folder (i.e. `cd Project1-Name`)

9. run python command `python manage.py startapp demoapp`

The program actually creates a new folder called demoapp

###urls.py
The file urls.py can be generated at project or at app level. In case you do not have an app level demoapp/urls.py file, you can create one and insert: 
```
from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name='index'), 
] 
```

On the project level the urls.py file should look like this:
```
from django.contrib import admin 
from django.urls import include, path 

urlpatterns = [ 
    path('demo/', include('demoapp.urls')), 
    path('admin/', admin.site.urls), 
] 
```

###urls.py

The data models required for processing in this app are created in this file. It is empty by default. A data model is a Python class based on django.db.modelsclass.All the models present here are migrated to the database tables. 

###settings.py

Lastly, you need to update the list of INSTALLED_APPS in the project’s setting file. This list already contains some pre-installed apps. Add the name of demoapp so that it looks like this:
```
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "demoapp",
]
```

Hi I am in week 1> Exercise: Creating your first project and app> In the Lab Exercise
I think im done but I cannot 'submit' to compare to the solution so I am stuck

## Resulting folder Structure

Here is the resulting folder structure

myDjangoEnv
├── Project1  <- Project Folder
│   ├── demoapp <- app folder, one of potentially many
│   │   ├── migrations
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py  <- app level routes
│   │   ├── views.py 
│   ├── Project1 <- overarching project folder
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py <- top level routes
│   │   ├── wsgi.py
│   ├── manage.py

├── Project1-env <- This is the enivronment created
    ├── bin
    │   ├── [...]
    ├── Lib
    │   ├── [...]
    ├── Scripts
	│   ├── activate
	│   ├── [...]
    ├── .gitignore

## The wiring

###Example 1: working with user supplied ids. 

User supplied ids: I.e. the user inputs `htpp://127.0.0.1/menue/1`. This means the id provided is a "1".

App Level urls.py file contains. The second path statement routes requests for `menu/` and also extracts the id as an int, which is in this case a `menu

``` 
urlpatterns = [ 
    path('', views.index, name='index'), 
	path ('menu/<int:menu_id>', views.menu_by_id, name='menu_by_id'),
] 	
```

The second argument directs the request to the `views.py` file and within the file to the function `menu_by_id`. Which is the one taking the argument `menu_id`. Within `views.py` you find: 

``` 
def menu_by_id(request,menu_id):
	menu = Menu.Object.get(pk=menu_id)
	return HttpResponse(f"{menu.menu_item}: Type of {menu.cuisine} cuisine")
```

This is then sent to the viewport as a response.

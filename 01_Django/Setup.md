Setup for [virtual environment](https://docs.python.org/3/library/venv.html).
1. mkdir project folder "Project1" and cd inside to "Project1"
2. Create virtual environment `python -m venv Project1-env`, where Project1-env is the name.
3. activate the virtual environment `.\Project1-env\Scripts\activate`
4 Install Django inside the virtual environment `pip install django`
5. Check if Django is installed: `python -m django version`
6. Create Django project: `django-admin startproject Project1-Name`  
7. cd to newly created folder `Project1-Name`
8. rund python `python manage.py runserver`


Winhin dir where manage.py is located run:

```python
python3 manage.py runserver # To run the server
python3 manage.py makemigrations # To compile the migrations
python3 manage.py migrate  # To migrate the changes in Database
```


Setup for [virtual environment](https://docs.python.org/3/library/venv.html).
1. mkdir project folder "Project1" and cd inside to "Project1"
2 Create virtual environment `python3 -m venv Project1-env`, where Project1-env is the name.


Winhin dir where manage.py is located run:

```python
python3 manage.py runserver # To run the server
python3 manage.py makemigrations # To compile the migrations
python3 manage.py migrate  # To migrate the changes in Database
```


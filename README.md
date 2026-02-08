# Hello Flask

A simple Flask application with three pages, built to help beginners learn Flask basics


## Features

- Home Page (/) displays a welcome message and a link to visit the about page
- About Page (/about) displays a description and a form with a name field
- Hello Page (/hello/<name>) displays "Hello [name]"


## Project Structure

hello-flask/
│
├── app.py
├── templates/
│ ├── home.html
│ ├── about.html
│ └── hello.html
└── LICENSE
└── README.md


## Requirements

- Python 3.x
- pip(Python package manager)
- Flask


## How to Run

1. git clone git@github.com:hermesged/hello-flask.git
2. cd hello-flask
3. python -m venv env
4. source env/bin/activate
5. pip install flask
6. export FLASK_APP=app.py
7. flask run or flask run --debug (for debug mode)
# flask imports
from flask import Flask, render_template, request, redirect, url_for

# SQLAlchemy
from model import Base, Storis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# setup
app = Flask(__name__)
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/categories/stori/<int:id>')
def categories_stori():
    return render_template('categories_stori.html')

@app.route('/stori/<int:id>')
def index_stori():
    return render_template('index_stori.html')
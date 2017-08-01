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
def HomePage():
    # stori_list = session.query(Storis).all()
    stori_list = [
    {"author": "MAtt","rating": "1", "description": "hello", "pic_url":"http:///"},
    {"author": "MAtt","rating": "1", "description": "hello", "pic_url":"http:///"},
    {"author": "MAtt","rating": "1", "description": "hello", "pic_url":"http:///"},
    {"author": "MAtt","rating": "1", "description": "hello", "pic_url":"http:///"},
    {"author": "MAtt","rating": "1", "description": "hello", "pic_url":"http:///"}]
    return render_template('index.html', stori_list=stori_list)


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

stori1 = Storis(author = "Amir", rating = 15 , description = "fake" , pic_url = "url here")
session.add(stori1)
session.commit()

@app.route('/',methods = ['GET','POST'])
def home_page():
    if request.methods == 'POST':
        request.form.get(stori_name)
        request.form.get(author_name)
        request.form.get(tags)
    stori_1ist = session.query(Storis).all()
    return render_template('index.html',stori_1ist=stori_1ist)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/stori/<int:stori_id>')
def index_stori():
    return render_template('index_stori.html', stori_id = stori_id)

@app.route('/search/<int:search_id>')
def index_search():
    return render_template('index_search.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


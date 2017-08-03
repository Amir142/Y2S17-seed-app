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

example = Storis(name = "stori1", author = "Amir", tags = "#this #that", rating = 23, description = "fake",text = "stori here", pic_url = "insert fake url")
session.add(example)
session.commit()


@app.route('/')
def home_page():
<<<<<<< Updated upstream
    stori_list = session.query(Storis).all()
    return render_template('index.html',stori_list=stori_list)


@app.route('/add')
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        stori_name_instance         = request.form.get('stori_name')
        author_name_instance        = request.form.get('author_name')
        tags_instance               = request.form.get('tags')
        stori_description_instance  = request.form.get('stori_description')
        text_instance               = request.form.get('stori_here')
        instance = Storis(name = stori_name_instance, author = author_name_instance,tags = "#thisthis", rating = 4,description = "description fake", text = "enter fake stori", pic_url= "pic here")
        session.add(instance)
        session.commit()
        return redirect(url_for('home_page'))

@app.route('/stori/<int:stori_id>', methods = ['GET','POST'])
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
    if request.method == 'GET':
        return render_template('sign_up.html', username = "", email = "")
    elif request.form.get('password') != request.form.get('confirm_password'):
        save_username = request.form.get('username')
        save_email = request.form.get('email')
        return render_template('sign_up',username = save_username, email = save_email)
    else:
        username_istance    = request.form.get('username')
        pass_instance       = request.form.get('password')

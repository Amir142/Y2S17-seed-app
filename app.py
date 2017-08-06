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

for deletethis in session.query(Storis):
    

# for deleting in session.query(Storis):
#     session.delete(deleting)
#     session.commit()

# example = Storis(name = "stori1", author = "Amir", tags = "#this #that", rating = 23, description = "fake",text = "stori here", pic_url = "insert fake url")
# session.add(example)
# session.commit()

###USER PAGE AND REMEMBER USER LIKED STORIS

@app.route('/', methods = ['GET','POST'])
def home_page():
    # if request.method = "GET":
    stori_list = session.query(Storis).order_by(Storis.rating.desc()).all()
    # stori_list = stori_list.reverse()
    return render_template('index.html',stori_list=stori_list)
    # def fixtags(tags):
    #     for char in tags:
    #         if char == '':
    #             tags = tags[:char]+tags[char+1:]



@app.route('/add',methods = ['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        stori_name_instance         = request.form.get('stori_name')
        author_name_instance        = request.form.get('author_name')
        tags_instance               = request.form.get('tags')
        stori_description_instance  = request.form.get('stori_description')
        text_instance               = request.form.get('stori_here')
        pic_url_instance            = request.form.get('pic_url')
        instance = Storis(name = stori_name_instance, author = author_name_instance,tags = tags_instance, rating = 0, description = stori_description_instance, text = text_instance, pic_url= pic_url_instance)
        session.add(instance)
        session.commit()
        return redirect(url_for('index_stori',stori_id = instance.id))

@app.route('/stori/<int:stori_id>')
def index_stori(stori_id):
    stori = session.query(Storis).filter_by(id=stori_id).all()
    return render_template('index_stori.html', stori=stori)

@app.route('/search/<int:search_id>')
def index_search():
    return render_template('index_search.html')

@app.route('/profile')
def profile_page():
    return render_template('profile_page.html')

@app.route('/sign_in', methods= ['GET','POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('sign_in.html')
    else:
        login_username = request.form.get('username_login')
        login_pass = request.form.get('password_login')
        return render_template(url_for('home_page'))

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html', username = "", email = "")
    else:
        # if request.form.get('username_sign_up') is in Users:    ###CHECK IF TAKEN
        username_istance    = request.form.get('username_sign_up')
        pass_instance       = request.form.get('password_sign_up')
        user_instance = Users(username = "username_istance",password = "password instance", online = True)
        session.add(user_instance)
        session.commit()
        return redirect(url_for('home_page'))

Base.metadata.create_all()
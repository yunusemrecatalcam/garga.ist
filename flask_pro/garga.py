from flask import Flask,render_template,\
    request,jsonify,session,redirect,url_for, \
    send_from_directory
import os
from flask_pro.db_handler import db_handler

dber = db_handler()

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)
app.secret_key = 'any random string'

ERR_TEXT = " //Booom, looks like I failed, please send an email about error yunusemrecatalcam@gmail.com "

@app.route("/")
def index():
    try:
        rend = render_template("index.html")
        return rend
    except Exception as e:
        return (str(e)+ ERR_TEXT)

@app.route("/ekle")
def ekle():
    try:
        rend = render_template("ekle.html")
        return rend
    except Exception as e:
        return (str(e)+ ERR_TEXT)

@app.route("/kilavuz")
def kilavuz():
    try:
        rend = render_template("kilavuz.html")
        return rend
    except Exception as e:
        return (str(e)+ ERR_TEXT)

@app.route("/kimiz")
def kimiz():
    try:
        rend = render_template("kimiz.html")
        return rend
    except Exception as e:
        return (str(e)+ ERR_TEXT)

@app.route("/content_get",methods=['POST'])
def content_get():
    try:
        namy  = request.form.get('text_name')
        texty = request.form.get('text')
        mahlas= request.form.get('mahlas')
        passy = request.form.get('password')
        print(namy,texty,mahlas,passy)
        dber.insert_text(namy,texty,mahlas)
        return (jsonify(success=True))
    except Exception as err:
        print(err)
        return(jsonify(success=False))

@app.route('/content_view/<content_id>')
def content_view(content_id):
    fetchy = dber.get_text_and_attr(content_id)
    fetched_title = fetchy.get('textname')
    fetched_text = fetchy.get('text')
    fetched_mahlas = fetchy.get('mahlas')
    if 'username' in session: #check for admin session
        fetched_votes = dber.get_votes(content_id)
        return render_template("textview.html",
                               text_name=fetched_title,
                               text=fetched_text,
                               mahlas=fetched_mahlas,
                               votes=fetched_votes,
                               username=session['username'],
                               text_id=content_id)
    else:
        return render_template("textview.html",
                               text_name=fetched_title,
                               text=fetched_text,
                               mahlas=fetched_mahlas)

@app.route('/admin/waitlist')
def waitlist():
    if 'username' in session:
        url_list = dber.get_waitings()
        return render_template("waitlist.html",urls= url_list
                               , username=session['username'])
    else:
        return redirect(url_for('index'))

@app.route('/admin/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        try:
            is_admin = dber.admin_login(request.form['username'],request.form['password'])
            if is_admin is True:
                session['username'] = request.form['username']
                return redirect(url_for('waitlist'))
            else:
                return redirect(url_for('index'))
        except Exception as err:
            return 'failure: '+ str(err)
    else:
        return render_template('login.html')

@app.route('/admin/vote',methods=['GET','POST'])
def vote():
    if request.method == 'POST':
        if 'username' in session:
            try:
                usr = session.get('username')
                text_id = request.form.get('text_id')
                vote = 1 if request.form.get('vote')== 'onay' else 0
                print(usr, text_id, vote)
                dber.insert_vote(text_id,usr,vote)
                return (jsonify(success=True))
            except:
                return (jsonify(success=False))

    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run()

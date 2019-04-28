from flask import Flask,render_template,request,jsonify
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)

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
        return (jsonify(success=True))
    except:
        return(jsonify(success=False))

@app.route('/content_view/<content_id>')
def content_view(content_id):
    fetched_title = 'heasder'
    fetched_text = 'I was living at the first floor,' \
                   'now Im climbing'
    fetched_mahlas = 'developer_developer_developer'
    return render_template("textview.html",text_name=fetched_title,
                           text = fetched_text,
                           mahlas=fetched_mahlas)
if __name__ == '__main__':
    app.run()

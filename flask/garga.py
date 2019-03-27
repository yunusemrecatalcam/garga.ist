from flask import Flask,render_template
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)

@app.route("/")
def index():
    try:
        rend = render_template("index.html")
        return rend
    except Exception as e:
        return (str(e)+" //Booom, looks like I failed, please send an email about error yunusemrecatalcam@gmail.com ")

@app.route("/ekle")
def ekle():
    try:
        rend = render_template("ekle.html")
        return rend
    except Exception as e:
        return (str(e)+" //Booom, looks like I failed, please send an email about error yunusemrecatalcam@gmail.com ")

@app.route("/kilavuz")
def kilavuz():
    try:
        rend = render_template("kilavuz.html")
        return rend
    except Exception as e:
        return (str(e)+" //Booom, looks like I failed, please send an email about error yunusemrecatalcam@gmail.com ")


if __name__ == '__main__':
    app.run()

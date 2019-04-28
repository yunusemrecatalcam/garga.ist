from flask import Flask,render_template
import os

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, '')
app = Flask(__name__, template_folder=template_path)


@app.route("/flask")
def hello():
    return "Hello Worlddddd!"

@app.route("/")
def index():
    try:
        rend = render_template("index.html")
        return rend
    except Exception as e:
        return (str(e)+"Booom, joking. Working on integrating flask right now!")
if __name__ == '__main__':
    app.run()

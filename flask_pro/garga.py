from flask import Flask,render_template,\
    request,jsonify,session,redirect,url_for, \
    send_from_directory
import os
from db_handler import db_handler

dber = db_handler()

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'templates')
app = Flask(__name__, template_folder=template_path)
app.secret_key = 'any random string'

ERR_TEXT = " //Booom, looks like I failed, please send an email about error yunusemrecatalcam@gmail.com "

@app.route("/", methods=['GET'])
def index():
    try:
        page = request.args.get('p')
        flowers, current_page, comment_cnt = dber.get_flow(page)
        page_indexes = dber.get_page_indexes()
        min_thresh = 0 if current_page-2<0 else current_page-2
        max_thresh = page_indexes[len(page_indexes)-1] if page_indexes[len(page_indexes)-1]<current_page+2 else current_page+2
        page_indexes = page_indexes[min_thresh:max_thresh+1]
        next_idx = (current_page+1) if current_page+1 <= page_indexes[-1] else current_page
        prev_idx = (current_page-1) if current_page>0 else current_page
        page_indexes = list(range(prev_idx, next_idx+1))
        rend = render_template("index.html", texts=flowers,
                               pages=page_indexes, current=current_page,
                               next=next_idx, prev=prev_idx,
                               comment_count=comment_cnt)
        return rend
    except Exception as e:
        return (str(e)+ ERR_TEXT)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'sitemap.xml')

@app.route("/ekle")
def ekle():
    try:
        rend = render_template("ekle.html", text_name="İçerik Ekle")
        return rend
    except Exception as e:
        return (str(e)+ ERR_TEXT)

@app.route("/kilavuz")
def kilavuz():
    try:
        rend = render_template("kilavuz.html", text_name="Kılavuz")
        return rend
    except Exception as e:
        return (str(e)+ ERR_TEXT)

@app.route("/kimiz")
def kimiz():
    try:
        rend = render_template("kimiz.html", text_name="Biz Kimiz?")
        return rend
    except Exception as e:
        return (str(e)+ ERR_TEXT)

@app.route("/comment",methods=['POST'])
def comment():
    comment = request.form.get('text')
    mahlas = request.form.get('mahlas')
    passy = request.form.get('password')
    text_id = request.form.get('text_id')
    insert_stat = dber.insert_comment(comment, mahlas, passy, text_id)
    return jsonify(success= True,
                   status=insert_stat)
@app.route("/content_get",methods=['POST'])
def content_get():
    try:
        namy  = request.form.get('text_name')
        texty = request.form.get('text')
        mahlas= request.form.get('mahlas')
        passy = request.form.get('password')
        insert_stat = dber.insert_text(namy,texty,mahlas,passy)
        return (jsonify(success=True,
                        status=insert_stat))
    except Exception as err:
        print(err)
        return(jsonify(success=False))

@app.route('/content_view/<content_id>')
def content_view(content_id):
    fetchy = dber.get_text_and_attr(content_id)
    comments = dber.get_comments(content_id)
    fetched_title = fetchy.get('textname')
    fetched_text = fetchy.get('text')
    fetched_mahlas = fetchy.get('mahlas')
    fetched_img = fetchy.get('img_path')
    pub_stat = dber.is_published(content_id)
    if 'username' in session: #check for admin session
        fetched_votes = dber.get_votes(content_id)
        return render_template("textview.html",
                               text_name=fetched_title,
                               text=fetched_text,
                               mahlas=fetched_mahlas,
                               votes=fetched_votes,
                               username=session['username'],
                               text_id=content_id,
                               img_path=fetched_img,
                               comments=comments)
    elif pub_stat is True:
        return render_template("textview.html",
                               text_name=fetched_title,
                               text=fetched_text,
                               mahlas=fetched_mahlas,
                               img_path=fetched_img,
                               text_id=content_id,
                               comments=comments)
    else:
        return render_template("textview.html")
@app.route('/admin/waitlist')
def waitlist():
    if 'username' in session:
        url_list = dber.get_waitings()
        return render_template("waitlist.html",urls= url_list
                               , username=session['username'])
    else:
        return redirect(url_for('index'))
@app.route('/admin/waiting_for_image')
def wait_for_it():
    url_list = dber.get_waiting_for_img()
    return render_template("waitlist.html", urls=url_list)

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
            except Exception as e:
                print(e)
                return (jsonify(success=False))

    return redirect(url_for('index'))

@app.route('/admin/comments')
def show_comments():
    if 'username' in session:
        comments = dber.get_all_published_comments()
        return render_template("comments.html", urls=comments)
    return "0"

@app.route('/search', methods=['GET'])
def search():
    search_word = request.args.get('key')
    search_in = request.args.get('search_in')
    if search_in not in ['text', 'textname', 'mahlas']:
        search_in = 'text'
    flowers, comment_cnt = dber.search(search_word, search_in)
    rend = render_template("index.html", texts=flowers, comment_count=comment_cnt,
                           search=True, search_word=search_word, key=search_in)
    return rend

@app.route("/dergi")
def dergi():
    return redirect("https://online.fliphtml5.com/yscwl/tuyt/", code=302)
    try:
        return render_template("dergi.html")
    except Exception as e:
        return (str(e)+ ERR_TEXT)

@app.route('/dergipdf')
def send_pdf():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'Garga_Sayi_1.pdf')

@app.route("/dergi2")
def dergi2():
    return redirect("https://online.fliphtml5.com/olrtq/yrbt/", code=302)

@app.route('/dergipdf2')
def send_pdf2():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'Garga_Sayi_2.pdf')

if __name__ == '__main__':
    app.run(debug=True)
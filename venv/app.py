import os
from flask import Flask, render_template, url_for, request, session,  redirect, send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GGFCFYBYFKUQSCFIUYFIUQjdrhibcsjdfnhshrlksnhndyihnkyhaukn'
menu = [{"name": "главная", "url": "cs"},
        {"name": "каталог", "url": "catalog"},
        {"name": "инфо", "url": "info"},
        {"name": "права сергея", "url": "web"},
        {"name": "Вход", "url": "login"}]

@app.route("/info")
def index():
    print( url_for('index') )
    return render_template('xindex.html', menu=menu)


@app.route("/start")
def cs():
    print(url_for('cs') )
    return render_template('cs.html', menu=menu)

@app.route("/web")
def web():
    print(url_for('web') )
    return render_template('index.html', menu=menu)

@app.route("/profile/<username>")
def profile(username):
    return f"Профиль: {username}"

@app.route("/login", methods=["GET", "POST"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "vovan" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title="", menu=menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Не удолось найти страницу", menu=menu)

@app.route("/catalog")
def catalog():
    print(url_for('catalog'))
    return render_template('huyra.html', menu=menu)


with app.test_request_context():
    print(url_for('catalog'))
    print(url_for('index'))
    print(url_for('cs'))
    print(url_for('profile', username="vovan"))


if __name__ == "__main__":
    app.run(debug=True)


#web: gunicorn app:app
#process.env.PORT




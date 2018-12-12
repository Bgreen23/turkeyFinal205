from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/start')
def start():
    # players = Draft.query.all()
    # return render_template('index.html', players=players)
    return render_template('start.html')

@app.route('/index')
def index():
    # posts = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     }
    # ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/backend', methods=["POST", "GET"])
@login_required
def backend():
    # if request.method == "POST":
    #     player = request.form["player"]
    #     team = request.form["team"]
    #     new_player = Draft(player, team)
    #     db_session.add(new_player)
    #     db_session.commit()
    #
    #     data = {
    #         "id": new_player.id,
    #         "player": player
    #         }
    #
    #     print(session['user'])
    #
    #     pusher_client.trigger('table', 'new-record', {'data': data})
    #
    #     return redirect("/backend", code=302)
    # else:
    #     players = Draft.query.all()
          return render_template('backend.html')
        # return render_template('backend.html', players=players)

#This route is for if I wanted to have more Users for my app. My app only needs one User(admin) so I decided to take #this block of code out

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)

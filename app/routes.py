from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User, Player


@app.route('/')
@app.route('/start')
def start():

    return render_template('start.html')

# Gathers all players in the database
@app.route('/index')
def index():
    players = Player.query.all()
    return render_template('index.html', title='Home', players=players)

# Log in function for ADMIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    # routes to index page if ADMIN is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # username and password verification
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

# Log out function
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# The ADMIN panel. This route allows you to add players and allows you to edit players
@app.route('/backend', methods=["POST", "GET"])
# requires the ADMIN to be logged in to access this route
@login_required
def backend():
    if request.method == "POST":
        name = request.form["player"]
        team = request.form["team"]
        db.execute('INSERT INTO Player (name, team) VALUES (name, team)')

        data = {
            "id": new_player.id,
            "player": player
            }

        pusher_client.trigger('table', 'new-record', {'data': data})

        return redirect("/backend", code=302)
    else:
        players = Player.query.all()
        return render_template('backend.html', players=players)

# The Edit Route
@app.route('/edit/<int:id>', methods=["POST", "GET"])
def update_record(id):
    if request.method == "POST":
        player = request.form["player"]
        team = request.form["team"]
        # updates specific player by id
        update_player = Player.query.get(id)
        update_player.player = player
        update_player.team = team
        db.session.commit()

        data = {
            "id": id,
            "player": player,
            "team": team
            }
        return redirect("/backend", code=302)
    else:
        new_player = Player.query.get(id)

        return render_template('update_player.html', data=new_player)


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

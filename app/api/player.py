@api.route('/api/players')
def index():
     players = Draft.query.all()
     return render_template('index.html', players=players)

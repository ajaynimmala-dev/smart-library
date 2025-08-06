import os

from flask import Flask, render_template

from database.models import db
from routes.user_ui import user

template_dir = os.path.abspath('../frontend')

app = Flask(__name__, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.register_blueprint(user)
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
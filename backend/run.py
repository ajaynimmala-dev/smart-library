from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from routes.user import user
template_dir = os.path.abspath('../frontend')

app = Flask(__name__, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.register_blueprint(user)
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

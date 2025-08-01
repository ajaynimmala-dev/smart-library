from flask import Flask, render_template
import os

template_dir = os.path.abspath('../frontend')

app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

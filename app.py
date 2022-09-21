import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix
app = Flask(__name__)
# Required for redirects to work in the preview window that's integrated in the lab IDE
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'
# Required for cookies to work in the preview window that's integrated in the lab IDE
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True




##base view
@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
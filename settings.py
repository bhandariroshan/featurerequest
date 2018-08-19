from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# set the project root directory as the static folder, you can set others.
app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/static',
    template_folder='templates'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db/engineering'
db = SQLAlchemy(app)

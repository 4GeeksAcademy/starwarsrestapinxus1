from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes import api 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def home():
    return "Bienvenido a la API de Star Wars"

if __name__ == '__main__':
    app.run(debug=True)

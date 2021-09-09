from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AOP'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/people_info'

db = SQLAlchemy(app)


class Peoples(db.Model):
    __tablename__= 'people_t'
    id=db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    first_name=db.Column('first_name', db.String(50), index=True, unique=True)
    last_name=db.Column('last_name', db.String(50), index=True, unique=True)
    email=db.Column('email',db.String(28), unique=True)



@app.route('/')
def home():
    return '<h1>Homy Page</h1><p>Never see it</p>'


@app.route('/fetch_user/<people_id>', methods=['GET'])
def fetch_user(people_id):
    peoples = Peoples.query.get(int(people_id))
    return jsonify(peoples)



@app.route('/create_user', methods=['POST'])
def create_user():
    return ' yaah! yr created, enjoy! '



@app.route('/update_user', methods=['GET'])
def update_user():
    return 'editing profile is commited'



@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    return 'your deleted'




if __name__ == "__main__":
        with app.app_context():
            db.create_all()
        app.run(debug=True)
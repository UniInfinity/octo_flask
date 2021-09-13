from flask import Flask, request, jsonify, Response, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AOP'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/peopl_info'

db = SQLAlchemy(app)


class Peoples(db.Model):
    __tablename__= 'people_t'
    id=db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    first_name=db.Column('first_name', db.String(50), index=True, unique=True)
    last_name=db.Column('last_name', db.String(50), index=True, unique=True)
    email=db.Column('email',db.String(28), unique=True)

    def __repr__(self):
        return {
            'first_name':self.first_name,
            'last_name':self.last_name,
            'email':self.email
        }

# data = [
#     {"id": 1,
#     "firstname":"Vaibhav",
#     "lastname":"Pawar",
#     "email":"pvai99@gmail.com"
#     },
#     {
#     "id": 2,
#     "firstname":"Roki",
#     "lastname":"Barbosa",
#     "email":"baro9@gmail.com"
#     }
# ]






@app.route('/home')
def home_page():
    return render_template("register.html")




@app.route('/get', methods=['GET'])
def get_user():
    peoples = Peoples.query.all()
    return jsonify(peoples)





@app.route('/fetch_user/<people_id>', methods=['GET'])
def fetch_user(people_id):
    peoples = Peoples.query.get(int(people_id))
    response = peoples.__repr__()
    return jsonify(response)




@app.route('/create_user', methods=['POST'])
def create_user():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    email=request.form['email']
    people = Peoples(first_name=first_name, last_name=last_name, email=email)
    db.session.add(people)
    db.session.commit()
    return render_template("register.html", people=people)





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
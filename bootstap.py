from flask import Flask,render_template , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:mayank%407@127.0.0.1:3306/flask_db"
db = SQLAlchemy(app)

class Contacts(db.Model):
    #sno = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(50), unique=False, nullable=False)
    phone_no = db.Column(db.String(11), unique=True, nullable=False)
    msg = db.Column(db.String(100), unique=True, nullable=False)
    #date = db.Column(db.String(10), unique=True, nullable=True)
    # id: Mapped[int] = mapped_column(primary_key=True)
    # username: Mapped[str] = mapped_column(unique=True)
    # email: Mapped[str]

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone_no')
        msg = request.form.get('msg')

        print("Form Data : ",name, email, phone, msg)
        entry = Contacts(name=name, phone_no=phone , msg=msg , email=email)
        db.session.add(entry)
        try:
            db.session.commit()
            print("Data Saved")
        except Exception as e:
            print("Error : ",e)
            db.session.rollback()
     
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True)
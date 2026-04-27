from flask import Flask , render_template , url_for , request, redirect
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/ahmed'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # this line i think it wrong

db = SQLAlchemy(app)

class Notes(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    note = db.Column(db.String(300))

with app.app_context():
    db.create_all()


@app.route("/")
def home():
     
    notes = Notes.query.all()

    return render_template("index.html" , notes = notes)


@app.route("/add" , methods= ['POST'])
def add():

    note = request.form.get('note')
    if note == "":
        return redirect('/')

    new_note = Notes(note=note)
    db.session.add(new_note)
    db.session.commit()
    return redirect('/')

@app.route("/delete/<int:id>")
def delete(id):
    note = Notes.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask , request , render_template , redirect , url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/ahmed'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Notes2(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    note = db.Column(db.String(300))

with app.app_context():
    db.create_all()

@app.route("/")
def home():

    notes = Notes2.query.all()
    return render_template("index.html", notes = notes)

@app.route('/add' , methods=['POST'])
def add():
    if request.method== 'POST':
        note = request.form.get('note')
        addnote = Notes2(note=note)
        db.session.add(addnote)
        db.session.commit()
    return redirect('/')

@app.route("/delete/<int:id>" )
def delete(id):
    note = Notes2.query.get_or_404(id)

    if note :
        db.session.delete(note)
        db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>'  , methods = [ 'POST' , 'GET'])
def update(id):
    note = Notes2.query.get_or_404(id)
    if request.method == "POST":
        note.note = request.form.get('update_note')
        db.session.commit()
        return redirect('/')

    return render_template("update.html")

if __name__ == "__main__":

    app.run(debug=True)

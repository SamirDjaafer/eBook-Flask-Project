from flask import Flask, render_template, url_for, flash, redirect
from forms import CreateBookForm, SearchBookForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a76hfb34ls9u6ty6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# eBook class
class Ebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Ebook('{self.id}', '{self.title}', '{self.author}')"

@app.route('/')
@app.route('/home')
def home():
    ebooks = Ebook.query.all()
    return render_template('home.html', title='Home', ebooks=ebooks)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/create', methods=['POST', 'GET'])
def create():
    form = CreateBookForm()
    if form.validate_on_submit():
        ebook = Ebook(title=form.title.data, author=form.author.data)
        db.session.add(ebook)
        db.session.commit()
        flash(f'{form.title.data} has been added to the database!', 'success')
        return redirect(url_for('home'))
    return render_template('create.html', title='Create eBook', form=form)


@app.route('/search')
def search():
    form = SearchBookForm()
    return render_template('search.html', title='Search for eBook', form=form)


# Checking if name is main
if __name__ == '__main__':
    app.run(debug=True)

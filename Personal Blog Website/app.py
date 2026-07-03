from flask import Flask, render_template, redirect, request, session
from models import db, User, Blog

app = Flask(__name__)
app.secret_key = "secret123"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    blogs = Blog.query.all()
    return render_template('index.html', blogs=blogs)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()
        if user:
            session['user'] = user.username
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'user' not in session:
        return redirect('/login')
    if request.method == 'POST':
        blog = Blog(
            title=request.form['title'],
            content=request.form['content'],
            author=session['user']
        )
        db.session.add(blog)
        db.session.commit()
        return redirect('/')
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    blog = Blog.query.get(id)
    if request.method == 'POST':
        blog.title = request.form['title']
        blog.content = request.form['content']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', blog=blog)

@app.route('/delete/<int:id>')
def delete(id):
    blog = Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

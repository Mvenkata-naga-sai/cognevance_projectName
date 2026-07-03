
from flask import Flask, render_template, request, redirect, session
from models import db, User, Job, Application

app = Flask(__name__)
app.secret_key = "secret123"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobportal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    jobs = Job.query.all()
    return render_template('jobs.html', jobs=jobs)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user = User(
            username=request.form['username'],
            password=request.form['password'],
            role=request.form['role']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()
        if user:
            session['user'] = user.username
            session['role'] = user.role
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/post-job', methods=['GET','POST'])
def post_job():
    if session.get('role') != 'employer':
        return redirect('/')
    if request.method == 'POST':
        job = Job(
            title=request.form['title'],
            description=request.form['description'],
            company=session['user']
        )
        db.session.add(job)
        db.session.commit()
        return redirect('/')
    return render_template('post_job.html')

@app.route('/apply/<int:id>')
def apply(id):
    if session.get('role') != 'candidate':
        return redirect('/')
    app_data = Application(user=session['user'], job_id=id)
    db.session.add(app_data)
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask,render_template,url_for,flash,redirect
from forms import Registrationform,Loginform
app = Flask(__name__)
app.config['SECRET_KEY']='d1ccf6248125c6b06ade3657bcbfa8a1'
posts = [
    {
        'author': 'Steve jobs',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Bill gates',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    }
]
@app.route('/')
def home():
    return render_template("home.html",posts=posts)
@app.route('/about')
def about():
    return render_template("about.html",title="About")


@app.route('/register',methods=['GET','POST'])
def register():
    form=Registrationform()
    if form.validate_on_submit():
        flash(f'Account created for user!','success')
        return redirect(url_for('home'))

    return render_template("register.html",title='register',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form=Loginform()
    if form.validate_on_submit():
        if form.Email.data=='kisan@gmail.com' and form.Password.data=='Password':
            flash('You have been logged in !','success')
            return redirect(url_for('home'))
    else:
        flash('Login unsuccessful.Please check username and password correctly!','danger')
        return render_template("login.html",title='login',form=form)
app.run(debug=True)

# import the Flask class from the flask module
from flask import Flask,render_template,request,redirect,url_for,session,flash

# create the application object
app = Flask(__name__)

app.secret_key="my precious"

# use decorators to link the function to a url
@app.route('/')
def home():
    # return "Hello,world!" # return a string
    return render_template("index.html")  # render a template

@app.route('/welcome')
def welcom():
    return render_template("welcome.html")  # render a template

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username']!='admin' or request.form['password']!='admin':
            error='Incorrect account or password, please try again.'
        else:
            session['logged_in']=True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html',error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were just logged out!')
    return redirect(url_for('welcom'))



# start the server with the 'run()' method
if __name__=='__main__':
    app.run(debug=True)

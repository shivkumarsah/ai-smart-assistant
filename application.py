from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
    	return redirect("/assistant", code=302)
    else:
        return show_the_login_form()
    ###### Login check ######
    error = None
    if request.method == 'POST':
        if valid_login(request.form['loginuser'],
                       request.form['loginpw']):
            return log_the_user_in(request.form['loginuser'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)



@app.route('/assistant', methods=['GET', 'POST'])
def assistant(name="Shiv"):
	return render_template('assistant.html', name=name)
from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.survey import Survey
from flask_app.models.user import User
from flask_app.models.menu import Menu
from flask_app.models.customer import Customer
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register/customer',methods=['POST'])
def registercustomer():
    if not Customer.validate_register(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = Customer.save(data)
    session['customer_id'] = id

    return redirect('/take/survey')


@app.route('/take/survey')
def takesurvey():
    if 'customer_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['customer_id']
    }
    return render_template("take_survey.html",customer=Customer.get_by_id(data),surveys=Survey.get_all(),menus=Menu.get_all())

@app.route('/login/customer',methods=['POST'])
def customerlogin():
    customer = Customer.get_by_email(request.form)

    if not customer:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(customer.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['customer_id'] = customer.id
    return redirect('/take/survey')     


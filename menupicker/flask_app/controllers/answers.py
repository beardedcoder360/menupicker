from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.survey import Survey
from flask_app.models.menu import Menu
from flask_app.models.customer import Customer
from flask_app.models.answer import Answer







@app.route('/answer/survey',methods=['post'])
def create_answer():
    if 'customer_id' not in session:
        return redirect('/logout')
    if not Answer.validate_answer(request.form):
        return redirect('/')
    data = {
        "answer1": request.form["answer1"],
        "answer2": request.form["answer2"],
        "answer3": request.form["answer3"],
        "answer4": request.form["answer4"],
        "answer5": request.form["answer5"],
        "customer_id": session ["customer_id"]
    }
    Answer.save(data)
    return redirect('/display/result')


@app.route('/display/result')
def displayresult():
    if 'customer_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['customer_id']
    }
    return render_template("results.html",customer=Customer.get_by_id(data),menus=Menu.get_all())
from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.survey import Survey
from flask_app.models.user import User
from flask_app.models.menu import Menu



@app.route('/new/survey')
def new_survey():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_survey.html',user=User.get_by_id(data))


@app.route('/edit/survey/<int:id>')
def edit_survey(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_survey.html",edit=Survey.get_one(data),user=User.get_by_id(user_data))



@app.route('/update/survey',methods=['POST'])
def update_survey():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Survey.validate_survey(request.form):
        return redirect(f'/edit/survey/{request.form["id"]}')
    data = { 
        "name"   : request.form["name"],
        "option1": request.form["option1"],
        "option2": request.form["option2"],
        "option3": request.form["option3"],
        "option4": request.form["option4"],
        "option5": request.form["option5"],
        "option6": request.form["option6"],
        "option7": request.form["option7"],
        "option8": request.form["option8"],
        "option9": request.form["option9"],
        "option10": request.form["option10"],
        "id": request.form["id"]
    }
    Survey.update(data)
    return redirect('/dashboard')

@app.route('/create/survey',methods=['post'])
def create_survey():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Survey.validate_survey(request.form):
        return redirect('/dashboard')
    data = {
        "name": request.form["name"],
        "option1": request.form["option1"],
        "option2": request.form["option2"],
        "option3": request.form["option3"],
        "option4": request.form["option4"],
        "option5": request.form["option5"],
        "option6": request.form["option6"],
        "option7": request.form["option7"],
        "option8": request.form["option8"],
        "option9": request.form["option9"],
        "option10": request.form["option10"],
        "user_id": session ["user_id"]
    }
    Survey.save(data)
    return redirect('/dashboard')


@app.route('/survey/<int:id>')
def show_survey(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_survey.html",survey=Survey.get_one(data),user=User.get_by_id(user_data))


@app.route('/destroy/survey/<int:id>')
def destroy_survey(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Survey.destroy(data)
    return redirect('/dashboard')

#@app.route('/take/survey')
#def take_survey():
  #  if 'customer_id' not in session:
   #     return redirect('/logout')
   # data ={
  #      'id': session['user_id']
   # }
   # return render_template("take_survey.html",user=User.get_by_id(data),surveys=Survey.get_all())
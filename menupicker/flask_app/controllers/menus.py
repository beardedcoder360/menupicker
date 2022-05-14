from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.survey import Survey
from flask_app.models.user import User
from flask_app.models.menu import Menu



@app.route('/new/menu')
def new_menu():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_menu.html',user=User.get_by_id(data))

@app.route('/create/menu',methods=['post'])
def create_menu():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Menu.validate_menu(request.form):
        return redirect('/new/menu')
    data = {
        "name" : request.form ["name"],
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
    Menu.save(data)
    return redirect('/dashboard')


@app.route('/edit/menu/<int:id>')
def edit_menu(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_menu.html",edit=Menu.get_one(data),user=User.get_by_id(user_data))



@app.route('/update/menu',methods=['POST'])
def update_menu():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Menu.validate_menu(request.form):
        return redirect('/dashboard')
        
    data = {
        "name": request.form ["name"], 
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
    Menu.update(data)
    return redirect('/dashboard')


@app.route('/menu/<int:id>')
def show_menu(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_menu.html",menu=Menu.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy/menu/<int:id>')
def destroy_menu(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Menu.destroy(data)
    return redirect('/dashboard')

from flask import render_template, request, redirect, session
from flask_app.model.ninja_model import Ninja
from flask_app.model.dojo_model import Dojo
from flask_app import app





@app.route('/ninja/add')
def add_ninja():
    all_dojo = Dojo.get_all()
    return render_template('new_ninja.html', all_dojo = all_dojo)


@app.route('/ninja/get_all')
def get_all():
    all_ninja = Ninja.get_all({'id' : id})
    print(all_ninja)
    return render_template('dojo.html', all_ninja = all_ninja)



@app.route('/ninja/submit', methods=['POST'])
def submit():
    # data = {
    #     'first_name': request.form['first_name'],
    #     'last_name': request.form['last_name'],
    #     'age': request.form['age'],
    #     'dojo_id': request.form['dojo_id']
    # }
    Ninja.add_ninja(request.form)
    return redirect('/')

@app.route('/ninja/show/<int:id>')
def show_ninja_id(id):
    ninja = Ninja.choose_dojo({'id' : id})
    return render_template('show.html', ninja = ninja)









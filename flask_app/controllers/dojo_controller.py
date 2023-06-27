from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.model.dojo_model import Dojo
from flask_app.model.ninja_model import Ninja



@app.route('/')
def Home ():
    # one_dojo = Dojo.get_one({'id' : id})
    # for ninjas in one_dojo.all_ninjas:
    #     print(ninjas.name)
    all_dojo = Dojo.get_all()
    return render_template('dojo.html', all_dojo = all_dojo)

    

# @app.route('/dojo/create')
# def create_dojo():
    
#     return render_template('dojo.html')

@app.route('/dojo/add',  methods=['POST'])
def add_dojo():
    # Dojo.add_dojo(request.form)
    data = {
        'name' : request.form['name']
    }
    Dojo.add_dojo(data)
    return redirect('/')


# @app.route('/dojo/show')
# def ninjas_show():
#     show_ninjas = Ninja.get_all()
#     print(show_ninjas)
#     return render_template('show.html', show_ninjas = show_ninjas)

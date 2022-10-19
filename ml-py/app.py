import re
from flask import Flask, render_template,request, url_for
from requests import get, post

get_cursos = get('http://localhost:5000/cursos').json()
get_comments = get('http://localhost:5000/comentarios').json()

list = {'coments': get_comments, 'cursos': get_cursos, 'index': 0, 'link': False}
app = Flask('__name__')

@app.route('/jujuba_store', methods=["GET", "POST"])
def home(): 
    return render_template('index.html', list = list)


@app.route('/choice_course', methods=['POST'])
def choice_course():

    index = request.form.get('button_choice')
    list = {'coments': get_comments, 'cursos': get_cursos, 'index': int(index) - 1 }

    return render_template('index.html', list=list)

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', 'PUT'])
def autenticar():
    password = request.form.get('senha')
    username = request.form.get('usuario')
    data = {'password': password, 'username': username}

    response = get('http://localhost:5000/user').json()

        
    if (len(response['user']) < 1):
        var = post('http://localhost:5000/user/create', json = data)

        if (var.json()['status']):
            return render_template('index.html', list = list)
        else :
            return render_template('login.html', message = var.json()['message'])
    else :
        return render_template('index.html', list = list)
    

@app.route('/create_course', methods=['POST', 'PUT'])
def create_course():
    nome = request.form.get('name_course')
    descricao = request.form.get('description')
    link = request.form.get('link')

    data = {
        'nome': nome,
        'descricao': descricao,
        'link': link
    }

    var = post('http://localhost:5000/cursos/create', json=data)
    
    if (var.json()['status']):
        list = {'coments': get_comments, 'cursos': get_cursos, 'index': 0,'link': link}
        return render_template('index.html', list = list)
    else :
        return 'status: {0} \n {1}'.format(var.json()['status'],var.json()['message']) 

@app.route('/create_comentary', methods=['POST'])
def create_comentary():
    body = request.form.get('comentary')

    data = {'user_id': 1, 'curso_id':1 , 'body': body}
    response = post('http://localhost:5000/comentarios/create',json = data)

    if (response.json()['status']):
        return render_template('index.html', list = list)
    else :
        return 'status: {0} \n {1} \n verifique os dados e tente novamente'.format(response.json()['status'], response.json()['message'])



if __name__ == '__main__':
    app.run('0.0.0.0', 5500, debug=True)
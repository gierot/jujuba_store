from flask import Flask, render_template,request##,requests, json,jsonify

app = Flask('__name__')

@app.route('/jujuba_store', methods=["GET", "POST"])
def home():
    ##coments = request.get('https://localhost:5000/comentarios/')
    ##cursos = request.get('https://localhost:5000/cursos/')
    ##list = [coments, cursos]
    ##list  = request.get('https://localhost:5000/user/').json()
    return render_template('index.html'  )# ,list)

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', 'PUT'])
def autenticar():
    password = request.form.get('senha')
    username = request.form.get('usuario')
    data = [password, username]

    response = request.post('https://localhost:5000/user/', data)

    if(response.data):
        return home()
    else :
        ##request.post('https://localhost:5000/user/create', data)
        return "usuario: {0}, senha: {1}".format(data[0], data[1])

@app.route('/create_course', methods=['POST', 'PUT'])
def create_course():
    nome = request.form.get('name_course')
    descricao = request.form.get('description')
    link = request.form.get('link')

    data = [nome, descricao, link]

    ##request.post('https://localhost:5000/cursos/create', data)

@app.route('/create_comentary', methods=['POST'])
def create_comentary():
    body = request.form.get('text')

    ##request.post('https://localhost:5000/comentarios/create',body)

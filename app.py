from flask import Flask, request, redirect, render_template
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy
from controller.User import UserController
from admin.Admin import start_views


config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder="templates")

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    db = SQLAlchemy(config.APP)
    start_views(app, db)
    db.init_app(app)
    
    @app.route('/')
    def index():
        return "Meu primeiro run"
    
    @app.route('/login/')
    def login():
        return "Login"
    
    @app.route('/login/', methods=['POST'])
    def login_post():
        user = UserController()
        email = request.form.get('email')
        password = request.form.get('password')

        result = user.login(email, password)

        if result:
            return redirect('/admin/')
        else:
            return render_template('login.html', data={'status': 401, 'message': 'Usuário ou senha inválidos!', "type": None})
    
    @app.route('/recovery-password/')
    def recovery_password():
        return "Recuperar senha"
    
    @app.route('/recovery-password/', methods=['POST'])
    def recovery_password_post():
        user = UserController()
        email = request.form.get('email')

        result = user.recovery_password(email)

        if result:
            return redirect('/login/')
        else:
            return render_template('recovery.html', data={'status': 401, 'message': 'Erro ao enviar e-mail de recuperação', "type": None})
    
    @app.route('/profile/<int:id>/action/<action>/')
    def profile_action(id, action):
        if action == 'action1':
            return f"Perfil {id} - Ação 1"
        elif action == 'action2':
            return f"Perfil {id} - Ação 2"
        elif action == 'action3':
            return f"Perfil {id} - Ação 3"
        
    @app.route('/profile', methods=['POST'])
    def create_profile():
        username = request.form.get('username')
        password = request.form.get('password')

        return f"Usuário {username} criado com sucesso!"
    
    @app.route('/profile/<int:id>', methods=['PUT'])
    def update_profile(id):
        username = request.form.get('username')
        password = request.form.get('password')

        return f"Usuário {id} atualizado com sucesso!"  
    
    return app

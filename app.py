#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, render_template
from config import app_config, app_active
from extensions import db, migrate
from model.User import User
from model.Role import Role
from model.Category import Category
from model.Product import Product
from controller.User import UserController
from admin.Admin import start_views


config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    migrate.init_app(app, db)
    start_views(app, db)

    db.init_app(app)


    @app.route('/')
    def index():
        return 'Meu primeiro Run'

    @app.route('/login/')
    def login():
        return 'Aqui entrará a tela de login'

    @app.route('/login', methods=['POST'])
    def login_post():
        user = UserController()

        email = request.form['email']
        password = request.form['password']

        result = user.login(email, password)

        if result:
            return redirect('/admin')
        else:
            return render_template('login.html', data={'status': 401, 'msg': 'Dados de Usuário incorretos', 'type': None})

    @app.route('/recovery-password/')
    def recovery_password():
        return 'Aqui entrará a tela de recuperar senha'

    @app.route('/recovery-password/', methods=['POST'])
    def send_recovery_password():
        user = UserController()

        result = user.recovery(request.form['email'])

        if result:
            return render_template('recovery.html', data={'status': 200, 'msg': 'E-Mail de recuperação enviado com sucesso'})
        else:
            return render_template('recovery.html', data={'status': 401, 'msg': 'Erro ao enviar e-mail de recuperação'})


    @app.route('/profile/<int:id>/action/<action>/')
    def profile(id, action):
        return f'A ação é {action} e O ID desse usuário é {id}'

    @app.route('/profile', methods=['POST'])
    def create_profile():
        username = request.form['username']
        password = request.form['password']

        return f'Essa rota possui um método POST e criará um usuário com os dados de usuário {username} e senha {password}'

    @app.route('/profile/<int:id>', methods=['PUT'])
    def edit_total_profile(id):
        username = request.form['username']
        password = request.form['password']

        return f'Essa rota possui um método PUT e editará o usuário {id}  com os dados de usuário {username} e senha {password}'



    return app



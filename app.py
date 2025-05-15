from flask import Flask, request, redirect, render_template # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
from config import app_config, app_active
from controller.User import UserController
from extensions import db, migrate

config = app_config[app_active]

def create_app() -> Flask:
    """
    Create a Flask application instance.
    :return: A Flask application instance.
    """
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(config)
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)
    migrate.init_app(app, db)

    # Load configuration from a file
    with app.app_context():
        from model import Category, Product, Role, User
        from admin.Admin import start_views
        start_views(app, db)
        
    
    @app.route('/')
    def index():
        return "Hello, World!"
    
    @app.route('/login/')
    def login():
        return 'Tela de login'
    
    @app.route('/login/', methods=['POST'])
    def login_post():
        """
        Handle the login form submission.
        :return: Redirect to the home page or render the login template with an error message.
        """
        email = request.form.get('email')
        password = request.form.get('password')

        user = UserController()
        result = user.login(email, password)

        if result:
            return redirect('/admin')
        else:
            return render_template('login.html', error='Dados de usuario incorretos')
        
    @app.route('/recovery_password/')
    def recovery_password():
        """
        Render the password recovery page.
        :return: Render the password recovery template.
        """
        return 'recuperar senha'
    
    @app.route('/recovery_password/', methods=['POST'])
    def recovery_password_post():
        """
        Handle the password recovery form submission.
        :return: Redirect to the home page or render the recovery template with an error message.
        """
        email = request.form.get('email')
        user = UserController()
        result = user.recovery(email)

        if result:
            return render_template('recovery.html', data={"status": 200, "msg": "Email enviado com sucesso"})
        else:
            return render_template('recovery.html', data={"status": 401, "msg": "Erro ao enviar email"})
    
    return app
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from model.User import User
from model.Role import Role
from model.Category import Category
from model.Product import Product


def start_views(app, db):
    admin = Admin(app, name='Meu Estoque', template_mode='bootstrap3')
    
    admin.add_view(ModelView(User, db.session, "Usuarios", category="Usuários"))
    admin.add_view(ModelView(Role, db.session, "Funções", category="Usuários"))
    admin.add_view(ModelView(Category, db.session, "Categorias", category="Produtos"))
    admin.add_view(ModelView(Product, db.session, "Produtos", category="Produtos"))
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from config import app_config, app_active


config = app_config[app_active]

class HomeView(AdminIndexView):
    @expose('/')
    def index(self):
        data = {
            'username': 'adam'
        }
        return self.render('home_admin.html', data=data)


class UserView(ModelView):

    column_labels = {
        'funcao': "Função",
        'username': 'Nome do usuário',
        'email': 'E-mail',
        'date_created': 'Data da criação',
        'last_update': 'Ultima atualização',
        'active': 'Ativo',
        'password': 'Senha',
    }

    column_descriptions = {
        'funcao': 'Função no painel administrativo',
        'username': 'Nome de usuário no sistema',
        'email': 'E-mail do usuário no sistema',
        'date_created': 'Data de criação do usuário no sistema',
        'last_update': 'Última atualização desse usuário no sistema',
        'active': 'Estado ativo ou inativo no sistema',
        'password': 'Senha do usuário no sistema'
    }

    
    form_excluded_columns = ['last_update', 'recovery_code']
    can_set_page_size = True
    can_view_details = True
    can_export = True
    column_exclude_list = ['password', 'recovery_code']
    column_searchable_list = ["username", "email"]
    column_filters = ["username", "email", "funcao"]
    column_editable_list = ["username", "email", "funcao", "active"]
    column_sortable_list = ["username"]
    column_default_sort = [("username", True), ("date_created", True)]
    column_details_exclude_list = ["password", "recovery_code"]
    column_export_exclude_list = ["password", "recovery_code"]
    create_modal = True
    edit_modal = True
    
    export_types = ["json", "yaml", "csv", "xls", "df"]

    form_widget_args = {
        'password': {
            'type': 'password'
        }
    }

    def on_model_change(self, form, User, is_created):
        if 'password' in form:
            if form.password.data:
                User.set_password(form.password.data)
            else:
                del form.password
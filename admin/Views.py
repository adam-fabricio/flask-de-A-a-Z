from flask_admin.contrib.sqla import ModelView
from config import app_config, app_active


config = app_config[app_active]

class UserView(ModelView):
    
    form_excluded_columns = ['last_update', 'recovery_code']
    can_set_page_size = True
    can_view_details = True
    column_exclude_list = ['password', 'recovery_code']
    column_searchable_list = ["username", "email"]
    column_filters = ["username", "email", "funcao"]
    column_editable_list = ["username", "email", "funcao", "active"]
    column_sortable_list = ["username"]
    column_default_sort = ("username", True)
    column_details_exclude_list = ["password", "recovery_code"]
    column_export_exclude_list = ["password", "recovery_code"]
    create_modal = True
    edit_modal = True
    can_export = True
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
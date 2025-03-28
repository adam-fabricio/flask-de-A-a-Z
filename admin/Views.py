# -*- coding: utf-8 -*-
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import Select2Widget
from wtforms import SelectField

class UserView(ModelView):
    column_exclude_list = ['password', 'recovery_code']
    form_excluded_columns = ['last_update', 'recovery_code']
    form_widget_args = {
            'password': {
                    'type': 'password'
                    }
            }
    form_columns = ['username', 'email', 'password', 'active', 'funcao']



    column_list = ['username', 'email', 'funcao', 'active']


def on_model_change(self, form, User, is_created):
    if 'password' in form:
        if form.password.data is not None:
            User.set_password(form.password.data)
        else:
            del form.password

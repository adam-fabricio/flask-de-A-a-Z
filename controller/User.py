from model.User import User


class UserController:
    def __init__(self):
        self.user_model = User()
    
    def login(self, email, password):
        """Login method to authenticate user"""
        self.user_model.email = self.user_model.get_user_by_email(email)
        result = self.user_model.get_user_by_email()

        if result:
            res = self.user_model.verify_password(password, result.password)
            if res:
                return result
            else:
                return {}
        return {}
    
    def recovery_password(self, email):
        """Todo: Implementar método para recuperação de senha"""
        return ''
    
    

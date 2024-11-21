from domain.core_classes import User

class UserBuilder:
    def __init__(self):
        self.user_id = None
        self.name = "Guest"
        self.role = "guest"
        self.email = None
        self.phone = None

    def set_user_id(self, user_id):
        self.user_id = user_id
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_role(self, role):
        self.role = role
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_phone(self, phone):
        self.phone = phone
        return self

    def build(self):
        if self.user_id is None:
            raise ValueError("User ID is required to build a User.")
        
        user = User(self.user_id, self.name, self.role)
        
        user.email = self.email
        user.phone = self.phone
        
        return user

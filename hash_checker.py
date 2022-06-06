import hashlib
import os


class Password:

    def __init__(self):
        self.users_data = {}

    def add_new_user(self, username, password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(hash_name='sha256',
                                  password=password.encode('utf-8'),
                                  salt=salt,
                                  iterations=150000)

        self.users_data[username] = {
            'salt': salt,
            'key': key,
        }

    def check_password(self, username, password):
        salt = self.users_data[username]['salt']
        password = hashlib.pbkdf2_hmac(hash_name='sha256',
                                       password=password.encode('utf-8'),
                                       salt=salt,
                                       iterations=150000)

        if self.users_data[username]['key'] == password:
            return True
        return False



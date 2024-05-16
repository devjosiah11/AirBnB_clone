Updates to keyboard shortcuts … On Thursday, 1 August 2024, Drive keyboard shortcuts will be updated to give you first-letter navigation.Learn more
#!/usr/bin/python3
'''This module creates a User class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Class for managing user objects'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the User class'''
        super().__init__(*args, **kwargs)

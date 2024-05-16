Updates to keyboard shortcuts … On Thursday, 1 August 2024, Drive keyboard shortcuts will be updated to give you first-letter navigation.Learn more
#!/usr/bin/python3
'''This module creates a Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Class for managing review objects'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the review class'''
        super().__init__(*args, **kwargs)

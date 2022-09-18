from email import message
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, AnyOf


class AddPet(FlaskForm):
    """allows to add a new pet with all information available"""
    
    name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField("Pet Species", validators=[InputRequired(), AnyOf(["cat","dog","porcupine"], message="Sorry, we do not accept animals of this species")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="must input a valid URL")])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min = 0, max = 30, message="age is out of range (0-30)")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")

class EditPet(FlaskForm):
    """similar to new pet, but provides only the fields that users are allowed to edit"""

    photo_url = StringField("Photo URL", validators=[Optional(), URL(message="must input a valid URL")])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("Available")
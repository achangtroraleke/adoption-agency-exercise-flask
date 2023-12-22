from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, TextAreaField, URLField, SelectField
from wtforms.validators import InputRequired, Optional, ValidationError

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField("Species", choices=['Dog', 'Cat', 'Porcupin'],validators=[InputRequired()])
    age = IntegerField("Age:")
    notes = TextAreaField("Notes:")
    photo_url = URLField("Photo URL", validators=[Optional()])
    
    def validate_age(form, field):
        if field.data < 0 or field.data > 30:
            raise ValidationError('Age must be between the ages of 1 and 30.')

class EditPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField("Species", choices=['Dog', 'Cat', 'Porcupin'],validators=[InputRequired()])
    age = IntegerField("Age:", validators=[Optional()])
    notes = TextAreaField("Notes:")
    photo_url = URLField("Photo URL", validators=[Optional()])
    available = BooleanField('Available: ')

    def validate_age(form, field):
        if field.data < 0 or field.data > 30:
            raise ValidationError('Age must be between the ages of 1 and 30.')

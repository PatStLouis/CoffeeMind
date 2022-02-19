from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import (
    ValidationError,
    DataRequired,
    Length,
)


class SettingsForm(FlaskForm):

    submit = SubmitField("Set")
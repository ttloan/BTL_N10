from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_uploads import UploadSet, IMAGES
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from werkzeug.utils import secure_filename


images = UploadSet('images', IMAGES)


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    old_price = IntegerField('OldPrice', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    type_id = IntegerField('TypeId', validators=[DataRequired()])
    vote = IntegerField('Vote', validators=[DataRequired(), NumberRange(min=0, max=5)])
    image = FileField('image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])


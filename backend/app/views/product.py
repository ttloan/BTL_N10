from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_uploads import UploadSet, IMAGES
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, Label
from wtforms.validators import DataRequired, NumberRange
from werkzeug.utils import secure_filename


images = UploadSet('images', IMAGES)


class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    old_price = IntegerField('old_price', validators=[DataRequired()])
    price = IntegerField('price', validators=[DataRequired()])
    type_id = IntegerField('type_id', validators=[DataRequired()])
    vote = IntegerField('vote', validators=[DataRequired(), NumberRange(min=0, max=5)])
    image = FileField('image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    deal_image = FileField('deal_image', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    big_image_1 = FileField('big_image_1', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    big_image_2 = FileField('big_image_2', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    small_image_1 = FileField('small_image_1', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    small_image_2 = FileField('small_image_2', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    description = TextAreaField('description', validators=[DataRequired()])
    chemical = BooleanField('chemical')
    organic = BooleanField('organic')
    from_farm = BooleanField('from_farm')
    deal = BooleanField('deal')
    free_ship = BooleanField('free_ship')
    sell = BooleanField('sell')
    feature = BooleanField('feature')

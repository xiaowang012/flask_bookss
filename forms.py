#coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField,DateField,SubmitField,FileField,TextAreaField
from wtforms.validators import AnyOf, DataRequired, EqualTo,Length, NumberRange
from flask_wtf.file import FileRequired,FileAllowed

#用户注册表单
class RegisterForms(FlaskForm):
    username = StringField('username',validators = [DataRequired('Username cannot be empty!'),Length(min=6,max=12,message = 'The username must be 6-12 characters long!')])
    password = PasswordField ('password',validators = [DataRequired('Password cannot be empty!'),Length(min=6,max=12,message = 'The password must be 6-12 characters long!')])
    password1 = PasswordField ('password1',validators = [DataRequired('Password1 cannot be empty!'),Length(min=6,max=12,message = 'The password must be 6-12 characters long!'),EqualTo('password',message = 'The entered passwords are inconsistent')])
    submit = SubmitField('submit')

#用户登录表单
class UserForms(FlaskForm):
    username = StringField('username',validators = [DataRequired('Username cannot be empty!'),Length(min=6,max=12,message = 'The username must be 6-12 characters long!')])
    password = PasswordField ('password',validators = [DataRequired('Password cannot be empty!'),Length(min=6,max=12,message = 'The password must be 6-12 characters long!')])
    submit = SubmitField('submit')

#添加书本表单
class AddBooksForms(FlaskForm):
    bookname = StringField('bookname',validators = [DataRequired('bookname cannot be empty!'),Length(1,50,message = 'The bookname must be 1-50 in length')])
    # booktype = SelectField ('booktype',validators=[DataRequired('booktype cannot be empty!')])
    book_description = TextAreaField('book_description',validators=[DataRequired('book description cannot be empty!')])
    issue_year = DateField ('issue_year',validators=[DataRequired('book issue year cannot be empty!')])
    bookfile = FileField('bookfile',validators = [FileRequired(message = 'File cannot be empty!'),FileAllowed(['pdf','doc','docx','txt'],message = 'File format error (pdf,doc,docx,txt only)!')])
    submit = SubmitField('submit')

#home界面查询书本的表单
class SearchBookForms(FlaskForm):
    book_name= StringField('book_name',validators = [DataRequired()])
    submit = SubmitField('submit')

#批量导入用户的表单
class UploadFileForms(FlaskForm):
    file = FileField('file',validators = [FileRequired(message = 'File cannot be empty!'),FileAllowed(['xlsx','xls'],message = 'File format error (XLSX/XLS only)!')])
    submit = SubmitField('submit')
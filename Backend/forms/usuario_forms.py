from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email

class RegisterForm(FlaskForm):
    first_name = StringField('Primeiro nome', render_kw={"placeholder": "Nome"}, validators=[DataRequired()])
    last_name = StringField('Sobrenome', render_kw={"placeholder": "Sobrenome"})
    email = StringField('E-mail', render_kw={"placeholder": "E-mail"}, validators=[Email(message='E-mail inválido!'), InputRequired()])
    password = PasswordField('senha', render_kw={"placeholder": "Senha"}, validators=[InputRequired(), EqualTo('confirm', message='As senhas devem ser correspondentes!')])
    confirm = PasswordField('Confirme sua senha', render_kw={"placeholder": "Confirme sua senha"})
    submit = SubmitField('CADASTRAR')
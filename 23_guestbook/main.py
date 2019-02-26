import os 
from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required 

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLAlCHEMY_COMMIT_ON_TEARDOWN'] = True 
app.config['SECRET_KEY'] = 	'hard to guess string'

db = SQLAlchemy(app)

class Guestbook(db.Model):
	__tablename__ = 'guestbooks'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(16), default='Anonymous')
	content = db.Column(db.String(64))
	time = db.Column(db.DateTime)

	def __repr__(self):
		return '<Guestbook %r>' %self.name 

class MessageForm(FlaskForm):
	username = StringField('Username')
	content = StringField('Content', validators=[Required()])
	submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def leave_a_message():
	form = MessageForm()
	if form.validate_on_submit():
		user.content = form.content.data
		user.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		db.session.add(user)
	return render_template("message1.html", form=form)

if __name__ == '__main__':
	app.run(debug=True)
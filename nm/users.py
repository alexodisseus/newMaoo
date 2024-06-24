import app
import model


from flask import Blueprint, render_template, current_app , request , session, redirect, url_for


users = Blueprint('users' , __name__ , url_prefix='/cotistas')


#usado para usersistrar os usuarios do sistema
@users.route('/', methods = ['GET','POST'])
def index():
	"""
	if 'username' not in session:
		return redirect(url_for('users.login'))

	"""

	#data = model.read_tasks(session['userid'])
	
	return render_template('users/index.html' )
	#return render_template('login.html' )



@users.route('/cadastrar', methods = ['GET','POST'])
def create():
	if request.method == 'POST':

		name = request.form['name']
		password = request.form['password']
		data = model.read_user(name,password)

		if data:

			session['username'] = data.name
			session['userid'] = data.id
			
			return redirect(url_for('users.index'))

		return render_template('login.html' )


	return render_template('users/create.html' )



@users.route('/painel', methods = ['GET','POST'])
def painel():
	return render_template('painel.html')

"""

@users.route('/view/<id>', methods = ['GET','POST'])
def view(id):
	if 'username' not in session:
		return redirect(url_for('users.login'))

	data = model.read_tasks_view(id)
	
	#sai da sessao se o usuario estiver errado
	if data.person_id != session['userid']:
		session.pop('username', None)
		return redirect(url_for('users.login'))

	return render_template('view.html' , data=data)


@users.route('/create/', methods = ['GET','POST'])

def create():
	#if 'username' not in session:
		#return redirect(url_for('users.login'))

	if request.method == 'POST':
		user = request.form['name']
		password = request.form['password']

		model.create_user(user,password)
		return redirect(url_for('users.login'))

	return render_template('create.html')





@users.route('/create_task/', methods = ['GET','POST'])
def create_task():

	if request.method == 'POST':
		title = request.form['title']
		status = request.form['status']

		model.create_tasks(title,status , session['userid'])
		return redirect(url_for('users.index'))

	return render_template('create_task.html')


@users.route('/logout', methods = ['GET','POST'])
def logout():

	session.pop('username', None)
	return redirect(url_for('users.login'))
"""

def configure(app):
	app.register_blueprint(users)
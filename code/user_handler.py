from flask import session
from SQL_handler import getUserById, getUserByUsername, User
from werkzeug.security import generate_password_hash, check_password_hash
from database_handler import IncorrectObjectDeclaration

# Places the current users id in the session
def login_parse(username, password):
	try:
		user = getUserByUsername(username)
	except IncorrectObjectDeclaration:
		return False
	
	if not user is None and check_password_hash(user.password, password):
		session['userId'] = user.id
		return True

	return False


# Pulls userId from session and returns its user
def get_user():
	try:
		id = session['userId']
		user = getUserById(id)
		return user
	except:
		return None

# Clears the session
def logout_parse():
	session['userId'] = None
from flask import session
from random_word import RandomWords
from random import choice
from SQL_handler import getUserById, getUserByUsername, insert_user, update_user, User
from werkzeug.security import generate_password_hash, check_password_hash
from database_handler import IncorrectObjectDeclaration

randomWords = RandomWords()

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


def signup_parse(username, password):
	if not getUserByUsername(username) is None:
		return False
		
	insert_user(User({'id': 'x', 'username': username, 'password': generate_password_hash(password), 'alias': generateAlias(), 'clearance': '2'}))
	return True


def update_parse(user: User) -> None:
	if getUserByUsername(username) is None:
		return False

	update_user(user)


def update_password(user: User, password) -> None:
	user.password = generate_password_hash(password)



def generateAlias():
	return choice(['Mr. ', 'Mrs. ', 'Miss. ', 'Sir ', 'Lord ', 'Prof. ', 'Dr. ', 'Lady ']) + randomWords.get_random_word().capitalize()
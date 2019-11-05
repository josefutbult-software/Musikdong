import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():
	app = Flask(__name__, instance_relative_config=True)

	app.config.from_mapping(
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(app.instance_path, 'app.db'),
	    SQLALCHEMY_TRACK_MODIFICATIONS = False
	)
	
	db = SQLAlchemy(app)
	migrate = Migrate(app, db)

	return (app, db, migrate)

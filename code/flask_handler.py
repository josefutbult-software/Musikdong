import os
from flask import Flask, request, render_template


# Not much at the moment, but returns a new flask instance
# TODO: Add
def create_app():
	return Flask(__name__, instance_relative_config=True)
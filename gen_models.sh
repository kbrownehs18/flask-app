#!/bin/sh

flask-sqlacodegen mysql+pymysql://username:password@localhost:3306/database?charset=utf8mb4 --outfile=./application/models/__init__.py
flask-sqlacodegen mysql+pymysql://username:password@localhost:3306/database?charset=utf8mb4 --outfile=./application/models/flask.py --flask

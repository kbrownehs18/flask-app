#!/bin/sh

sqlacodegen --outfile=./application/models/__init__.py mysql+pymysql://username:password@localhost:3306/database?charset=utf8mb4
flask-sqlacodegen --outfile=./application/models/flask.py mysql+pymysql://username:password@localhost:3306/database?charset=utf8mb4

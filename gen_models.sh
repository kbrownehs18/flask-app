#!/bin/sh

sqlacodegen --outfile=./application/models.py mysql+pymysql://username:password@localhost:3306/database?charset=utf8mb4
sqlacodegen --flask --outfile=./application/flask/models.py mysql+pymysql://username:password@localhost:3306/database?charset=utf8mb4

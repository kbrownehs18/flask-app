#!/usr/bin/env python
# coding: utf-8

from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cache = FlaskRedis()

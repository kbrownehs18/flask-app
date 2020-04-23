#!/usr/bin/env python
# coding: utf-8

from flask import Blueprint

mod = Blueprint("api", __name__, url_prefix="/api")

from . import home 

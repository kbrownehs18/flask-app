#!/usr/bin/env python
# coding: utf-8

from . import routes

@routes.route("/")
def index():
    return "Hello world"
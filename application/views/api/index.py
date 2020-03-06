#!/usr/bin/env python
# coding: utf-8

from . import mod
from utils4py.flask_utils import response


@mod.route("/", methods=["POST"])
def func():
    return response(data=["Hello world"])

#!/usr/bin/env python
# coding: utf-8

from utils4py.blueprint import NestedBlueprint
from utils4py.flask_utils import response

routes = NestedBlueprint("application", __name__, url_prefix="/")

from . import index
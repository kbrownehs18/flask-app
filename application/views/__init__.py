#!/usr/bin/env python
# coding: utf-8

from utils4py.blueprint import NestedBlueprint

routes = NestedBlueprint("application", __name__, url_prefix="/")

from . import index, api

routes.register_blueprint(api.mod)

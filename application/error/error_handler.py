#!/usr/bin/env python
# coding: utf-8

import traceback
from utils4py.flask_utils import response


def error_response(error):
    traceback.print_exc()
    return response(data="System error", code=500)

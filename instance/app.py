#!/usr/bin/env python
# coding: utf-8

import os

APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_URL = os.getenv("APP_URL", "http://127.0.0.1:8000")

UPLOAD_FOLDER = APP_ROOT + "/application/public"

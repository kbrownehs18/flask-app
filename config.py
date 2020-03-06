#!/usr/bin/env python
# coding: utf-8

import os

APP_NAME = os.getenv("APP_NAME", "API")  # application name
DEBUG = True if os.getenv("DEBUG", "true").lower() == "true" else False  # debug
HOST = os.getenv("HOST", "0.0.0.0")  # bind host
PORT = int(os.getenv("PORT", 8000))  # bind port
LOG_LEVEL = os.getenv("LOG_LEVEL", "debug")  # log level

APP_KEY = os.getenv("APP_KEY", "")  # application key
APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # application root path

CORS_ENABLED = (
    True if os.getenv("CORS_ENABLED", "false").lower() == "true" else False
)  # nginx

WTF_CSRF_ENABLED = True if os.getenv("WTF_CSRF_ENABLED", "true").lower() == "true" else False

WTF_CSRF_SECRET_KEY = APP_KEY

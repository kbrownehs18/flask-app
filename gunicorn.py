#!/usr/bin/env python
# coding: utf-8

import os

debug = True if os.getenv("DEBUG", "false").lower() == "true" else False
loglevel = os.getenv("LOG_LEVEL", "debug")
bind = "%s:%d" % (os.getenv("HOST", "0.0.0.0"), os.getenv("PORT", 8000))

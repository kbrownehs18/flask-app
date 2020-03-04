#!/usr/bin/env python
# coding: utf-8

import os

REDIS_URL = os.getenv("APP_NAME", "redis://:password@localhost:6379/0")

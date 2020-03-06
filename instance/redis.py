#!/usr/bin/env python
# coding: utf-8

import os

REDIS_URL = os.getenv("REDIS_URL", "redis://:password@localhost:6379/0")

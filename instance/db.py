#!/usr/bin/env python
# coding: utf-8

import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    "mysql+pymysql://username:password@localhost:3306/database?charset=utf8mb4",
)
SQLALCHEMY_COMMIT_ON_TEARDOWN = (
    True
    if os.getenv("SQLALCHEMY_COMMIT_ON_TEARDOWN", "true").lower() == "true"
    else False
)
SQLALCHEMY_TRACK_MODIFICATIONS = (
    True
    if os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "false").lower() == "true"
    else False
)
SQLALCHEMY_ECHO = (
    True if os.getenv("SQLALCHEMY_ECHO", "true").lower() == "true" else False
)
SQLALCHEMY_POOL_RECYCLE = int(os.getenv("SQLALCHEMY_POOL_RECYCLE", 3600))
SQLALCHEMY_POOL_SIZE = int(os.getenv("SQLALCHEMY_POOL_SIZE", 10))

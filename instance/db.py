#!/usr/bin/env python
# coding: utf-8

import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    "mysql+pymysql://username:password@localhost:3306/database?charset=utf8mb4",
)
SQLALCHEMY_TRACK_MODIFICATIONS = (
    True
    if os.getenv("SQLALCHEMY_COMMIT_ON_TEARDOWN", "false").lower() == "true"
    else False
)
SQLALCHEMY_ECHO = (
    True if os.getenv("SQLALCHEMY_ECHO", "true").lower() == "true" else False
)

SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_recycle": int(os.getenv("SQLALCHEMY_POOL_RECYCLE", 5)),
    "pool_timeout": int(os.getenv("SQLALCHEMY_POOL_TIMEOUT", 5)),
    "pool_size": int(os.getenv("SQLALCHEMY_POOL_SIZE", 10)),
    "pool_pre_ping": True
    if os.getenv("SQLALCHEMY_POOL_PRE_PING", "true").lower() == "true"
    else False,
}

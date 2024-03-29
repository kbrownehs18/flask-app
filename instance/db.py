#!/usr/bin/env python
# coding: utf-8

import os
from sqlalchemy.pool import QueuePool

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    "mysql+pymysql://username:password@localhost:3306/database?charset=utf8mb4",
)
SQLALCHEMY_TRACK_MODIFICATIONS = (
    True
    if os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "false").lower() == "true"
    else False
)
SQLALCHEMY_ECHO = (
    True if os.getenv("SQLALCHEMY_ECHO", "true").lower() == "true" else False
)

SQLALCHEMY_ENGINE_OPTIONS = {
    "poolclass": QueuePool,
    "pool_size": int(os.getenv("SQLALCHEMY_POOL_SIZE", 10)),
    "pool_pre_ping": True
    if os.getenv("SQLALCHEMY_POOL_PRE_PING", "true").lower() == "true"
    else False,
    "pool_recycle": int(os.getenv("SQLALCHEMY_POOL_RECYCLE", 86400)),
    "pool_timeout": int(os.getenv("SQLALCHEMY_POOL_TIMEOUT", 3600)),
}


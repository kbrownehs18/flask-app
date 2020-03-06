#!/usr/bin/env python
# coding: utf-8

import logging
import application


app = application.create_app()

if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
    app.logger.setLevel(logging.getLevelName(app.config["LOG_LEVEL"].upper()))
else:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


#!/usr/bin/env python
# coding: utf-8

import logging
import application
import sys

app = application.create_app()


if "run" in sys.argv:
    # debug in vscode, "run" in sys.argv
    # and run.py
    log_level = logging.getLevelName(app.config["LOG_LEVEL"].upper())
    app.logger.setLevel(log_level)
    if __name__ == "__main__":
        app.run(
            host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"]
        )
else:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


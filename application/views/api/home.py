#!/usr/bin/env python
# coding: utf-8

from . import mod
from utils4py.flask_utils import response
from utils4py import utils
from flask import request
import time
from ... import app
import os


@mod.route("/upload", methods=["POST"], endpoint="upload")
def upload():
    """
    upload image
    """
    files = request.files.getlist("files")
    files_path = []
    for file in files:
        ext = utils.extension(file.filename)
        app.logger.info("Upload files: %s %s", ext, app.config["ALLOW_UPLOAD_EXT"])
        if app.config["ALLOW_UPLOAD_EXT"] and ext not in app.config["ALLOW_UPLOAD_EXT"]:
            # forbid upload
            return response(code=9010, msg="文件类型[%s]不允许上传" % ext)

        name = utils.md5(str(time.time()))
        file_path = "/uploads/files/%s/%s" % (name[0:2], name[2:4])
        if not os.path.exists(file_path):
            os.makedirs(app.config["UPLOAD_FOLDER"] + file_path)

        filename = "%s/%s.%s" % (file_path, name, ext)
        file.save(app.config["UPLOAD_FOLDER"] + filename)

        files_path.append(filename)

    abs_path = [(app.config["IMAGE_URL"] + v) for v in files_path]

    return response(data={"files_url": abs_path, "files_path": files_path})

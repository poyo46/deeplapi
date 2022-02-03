import logging
import traceback
from datetime import datetime

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from deeplapi import (
    __author__,
    __author_email__,
    __copyright__,
    __description__,
    __license__,
    __title__,
    __version__,
)

from .apis.languages import languages_api
from .apis.translation import translation_api
from .apis.usage import usage_api
from .config import Config

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
for api in (translation_api, usage_api, languages_api):
    app.register_blueprint(api)


@app.route("/")
def root():
    return jsonify(
        {
            "name": __title__,
            "version": __version__,
            "description": __description__,
            "author": f"{__author__} <{__author_email__}>",
            "license": __license__,
            "copyright": __copyright__,
        }
    )


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        name = e.name
        message = e.description
        code = e.code
        logger.error(message)
    else:
        name = "Internal Server Error"
        message = "See server log"
        code = 500
        logger.error(traceback.format_exc())

    timestamp: str = datetime.now().isoformat()
    response_json = {"error": name, "message": message, "datetime": timestamp}
    return jsonify(response_json), code


if __name__ == "__main__":
    app.run(host=Config.host, port=Config.port, debug=Config.in_dev)

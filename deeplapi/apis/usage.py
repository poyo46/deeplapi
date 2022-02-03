from typing import Dict

from deepl.exceptions import DeepLException
from deepl.translator import Usage
from flask import Blueprint, jsonify
from werkzeug.exceptions import InternalServerError

from deeplapi import translator

name = "usage"
usage_api = Blueprint(name, __name__, url_prefix=f"/{name}")


def detail_to_dict(detail) -> Dict:
    return {
        "count": detail.count,
        "limit": detail.limit,
        "valid": detail.valid,
        "limit_exceeded": detail.limit_exceeded,
    }


@usage_api.route("", methods=["GET"])
def fetch_usage():
    try:
        usage: Usage = translator.get_usage()
        return jsonify(
            {
                "character": detail_to_dict(usage.character),
                "document": detail_to_dict(usage.document),
                "team_document": detail_to_dict(usage.team_document),
            }
        )
    except DeepLException as e:
        raise InternalServerError(str(e))

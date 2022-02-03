from typing import Dict, List

from deepl.exceptions import DeepLException
from deepl.translator import Language
from flask import Blueprint, jsonify
from werkzeug.exceptions import InternalServerError

from deeplapi import translator

name = "languages"
languages_api = Blueprint(name, __name__, url_prefix=f"/{name}")


def language_to_dict(language: Language) -> Dict:
    return {"code": language.code, "name": language.name}


@languages_api.route("", methods=["GET"])
def fetch_languages():
    try:
        source_languages: List[Language] = translator.get_source_languages()
        target_languages: List[Language] = translator.get_target_languages()
        return jsonify(
            {
                "source_languages": [
                    language_to_dict(lang) for lang in source_languages
                ],
                "target_languages": [
                    language_to_dict(lang) for lang in target_languages
                ],
            }
        )
    except DeepLException as e:
        raise InternalServerError(str(e))

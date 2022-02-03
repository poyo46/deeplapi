from deepl.exceptions import DeepLException
from deepl.translator import TextResult
from flask import Blueprint, jsonify, request
from werkzeug.exceptions import BadRequest, InternalServerError

from deeplapi import translator

name = "translation"
translation_api = Blueprint(name, __name__, url_prefix=f"/{name}")


@translation_api.route("", methods=["GET"])
def translate():
    text = request.args.get("text", None)
    if text is None:
        raise BadRequest("parameter `text` is required.")
    source_lang = request.args.get("source_lang", None)
    target_lang = request.args.get("target_lang", None)
    if target_lang is None:
        raise BadRequest("parameter `target_lang` is required.")

    try:
        result: TextResult = translator.translate_text(
            text, source_lang=source_lang, target_lang=target_lang
        )
        return jsonify(
            {"text": result.text, "detected_source_lang": result.detected_source_lang}
        )
    except DeepLException as e:
        raise InternalServerError(str(e))

import logging
import os
from logging import NullHandler

import deepl

__title__ = "deeplapi"
__description__ = "DeepL translation API"
__url__ = "https://github.com/poyo46/deeplapi"
__version__ = "0.1.0"
__author__ = "poyo46"
__author_email__ = "poyo4rock@gmail.com"
__license__ = "Apache-2.0"
__copyright__ = "Copyright 2022 poyo46"

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())

# DeepL translator
_auth_key = os.getenv("DEEPL_AUTH_KEY")
translator = deepl.Translator(_auth_key)

import os
from pathlib import Path

import yaml

from . import __title__

_DEV = "development"
_ROOT_DIR = Path(__file__).parents[1].resolve()
_CONFIG_DIR = _ROOT_DIR / "config"


def _get_env() -> str:
    env_name = f"{__title__.upper()}_ENV"
    env_value = os.getenv(env_name, "").lower()
    if env_value in (_DEV, "test", "production"):
        return env_value
    # default
    return _DEV


_ENV = _get_env()


with open(_CONFIG_DIR / "server.yml", mode="rt") as f:
    SERVER = yaml.safe_load(f.read())[_ENV]


class Config(object):
    in_dev = _ENV == _DEV

    # Flask
    host = SERVER["host"]
    port = int(SERVER["port"])

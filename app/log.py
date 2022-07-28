import logging

import yaml

from paths import Path

with open(Path.base("config.yaml"), "rt") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    logger = logging.getLogger("ROOT")

import re
import os

REPO_PATH = os.path.dirname(os.path.dirname(__file__))
LOCALS_PATH = os.path.join(REPO_PATH, ".local")

TABOR_CONFIG_SEARCH_PATHS = [
    os.path.join(REPO_PATH, "tabor.yaml"),
    os.path.join(LOCALS_PATH, "tabor.yaml"),
] + re.split(r"[\s,]+", os.environ.get("TABOR_CONFIG_SEARCH_PATHS", ""))

ENVIRONMENT = os.environ.get("ENVIRONMET", "dev")

import os
from typing import List
from bole import CascadingConfig
from bole.config import merge_cascading_dicts

from tabor_api.consts import REPO_PATH, TABOR_CONFIG_SEARCH_PATHS, ENVIRONMENT


class TaborConfig(CascadingConfig):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def port(self) -> int:
        return self.get("port", 5026)

    @property
    def host(self) -> str:
        return self.get("host", "0.0.0.0")

    @property
    def reload(self) -> bool:
        return self.get("reload", True)

    @property
    def reload_dir(self) -> str:
        return self.get("reload_dir", REPO_PATH)

    @property
    def visa_port(self) -> int:
        return self.get("visa_port", 5025)

    @property
    def visa_host_address(self) -> object:
        return self.get("visa_host_address", "localhost")


def load_config(*src: List[str], environment: str = ENVIRONMENT):
    """Loads configuration from src paths,
    if empty, uses the default source paths
    """
    if len(src) == 0:
        src = TABOR_CONFIG_SEARCH_PATHS

    config = TaborConfig()
    loaded = []
    for s in src:
        if not os.path.exists(s):
            continue
        loaded.append(TaborConfig.load(s, environment=environment))

    if len(loaded) > 0:
        config = merge_cascading_dicts(config, *loaded)

    return config

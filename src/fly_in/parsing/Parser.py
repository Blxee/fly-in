from typing import Any
import re


class Parser:
    _nb_drones_pattern: re.Pattern = re.compile(
        r"^\s*nb_drones\s*:\s*(?P<nb_drones>[0-9]+)\s*$"
    )
    _meta_max_drones_pattern: str = (
        r"(?:max_drones\s*=\s*(?P<max_drones>[0-9]+)"
    )
    _meta_zone_pattern: str = (
        r"(?:zone\s*=\s*(?P<zones>normal|blocked|restricted|priority))"
    )
    _hub_meta_option: str = (
        rf"\s*({_meta_max_drones_pattern}|{_meta_zone_pattern})\s*"
    )
    _hub_meta_data_pattern: str = (
        rf"(?:\[{_hub_meta_option}(?:\s+{_hub_meta_option})*])?"
    )
    _start_hub_pattern: re.Pattern = re.compile(
        rf"^\s*start_hub\s*:\s*([0-9]+)\s+([0-9]+){_hub_meta_data_pattern}\s*$"
    )

    @staticmethod
    def from_str(config: str) -> dict[str, Any]:
        return Parser._start_hub_pattern.match(config)

    @staticmethod
    def _parse_nb_drones(config: str) -> int:
        pass

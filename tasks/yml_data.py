from pathlib import Path

from kink import inject
import yaml


@inject
def get_tts_yml_data(curr_dir: Path) -> dict:
    with open(curr_dir.parent / "silero-pretrained.yml") as f:
        return yaml.safe_load(f)

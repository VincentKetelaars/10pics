"""Helper functions."""
import shutil
import tempfile

import requests


def download_media_item(*, url: str) -> str:
    """Download photo to your /tmp directory."""
    response = requests.get(url, stream=True)
    response.raise_for_status()

    temp_file = tempfile.NamedTemporaryFile(dir="/tmp", delete=False)
    shutil.copyfileobj(response.raw, temp_file)
    temp_file.close()
    response.close()

    return temp_file.name

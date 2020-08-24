"""Functions to interact witht the google photos library API."""

from datetime import date
from typing import Any, Callable, Dict, List, Optional

from googleapiclient.discovery import Resource  # pylint: disable=import-error

_MEDIA_ITEMS_PAGE_SIZE = 100
_ALBUMS_PAGE_SIZE = 50


def search_photos(*, client: Resource, start_date: date) -> List[Dict[str, Any]]:
    """Get the meta data for all photos since start date."""
    body = {
        "filters": _create_start_date_filter(start_date=start_date),
        "pageSize": _MEDIA_ITEMS_PAGE_SIZE,
    }
    return _do_pagination(executable=client.mediaItems().search, body=body, parameters=None, object_name="mediaItems")


def get_albums(*, client: Resource) -> List[Dict[str, Any]]:
    """Get meta data on all albums."""
    parameters = {"pageSize": _ALBUMS_PAGE_SIZE}
    return _do_pagination(
        executable=client.albums().list, body=None, parameters=parameters, object_name="albums"
    ) + _do_pagination(
        executable=client.sharedAlbums().list, body=None, parameters=parameters, object_name="sharedAlbums"
    )


def get_photos_by_album(*, client: Resource, album_id: str) -> List[Dict[str, Any]]:
    """Get the meta data for all photos for this album."""
    body = {
        "albumId": album_id,
        "pageSize": _MEDIA_ITEMS_PAGE_SIZE,
    }
    return _do_pagination(executable=client.mediaItems().search, body=body, parameters=None, object_name="mediaItems")


def photo_download_url(*, base_url: str) -> str:
    """Convert the photo's base url to a downloadable url."""
    return base_url + "=d"


def _do_pagination(
    *, executable: Callable, body: Optional[Dict[str, Any]], parameters: Optional[Dict[str, Any]], object_name: str
) -> List[Dict[str, Any]]:  # pylint: disable=C0330
    """Iterate over the result pages of the executable endpoint.

    Some endpoints require a body, others query parameters. One of those is necessary for the call.
    """
    items = []
    next_page_token = ""
    while next_page_token is not None:
        if body is not None:
            body["pageToken"] = next_page_token
            results = executable(body=body).execute()
        elif parameters is not None:
            parameters["pageToken"] = next_page_token
            results = executable(**parameters).execute()
        else:
            raise NotImplementedError
        next_page_token = results.get("nextPageToken")
        items.extend(results.get(object_name, []))
    return items


def _create_start_date_filter(*, start_date: date) -> Dict[str, Any]:
    """Create date range filter, which requires both a start and end date."""
    end_date = date.today()
    return {
        "dateFilter": {
            "ranges": [
                {
                    "startDate": {"year": start_date.year, "month": start_date.month, "day": start_date.day},
                    "endDate": {"year": end_date.year, "month": end_date.month, "day": end_date.day},
                }
            ]
        }
    }

import os
from static.API.constants.common import API_BASE_URL
from static.API.constants.marketdata import API_PUBLIC_PATH, METHOD_TIME, METHOD_ASSET_PAIRS


def get_base_url() -> str:
    return os.getenv(API_BASE_URL)


def get_public_time_url() -> str:
    return "{}{}{}".format(get_base_url(), API_PUBLIC_PATH, METHOD_TIME)


def get_public_asset_pairs_url(from_asset: str, to_asset: str) -> str:
    return "{}{}{}?pair={}{}".format(get_base_url(), API_PUBLIC_PATH, METHOD_ASSET_PAIRS, from_asset, to_asset)

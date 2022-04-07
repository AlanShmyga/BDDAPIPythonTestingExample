import base64
import hashlib
import hmac
import time
import urllib
import requests
from static.API.constants import common
from utils import config_helper


def get_encode_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data[common.NONCE]) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()


def authorized_post_request(uri_path, data, api_key, api_sec):
    headers = {
        common.HEADER_API_KEY: api_key,
        common.HEADER_API_SIGN: get_encode_signature(uri_path, data, api_sec)
    }
    return requests.post((config_helper.get_base_url() + uri_path), headers=headers, data=data)


def generate_nonce():
    return str(int(1000 * time.time()))
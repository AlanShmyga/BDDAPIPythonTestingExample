from assertpy import assert_that
from static.API.constants.common import RESPONSE_RESULT_KEY


def get_trading_pairs(context):
    return context.response.json()[RESPONSE_RESULT_KEY]


def get_trading_pair_from_server(context):
    response_pairs = get_trading_pairs(context)
    assert_that(response_pairs).is_length(1)
    first_pair_description = response_pairs.popitem()[1]
    return first_pair_description

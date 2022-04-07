import requests
from assertpy import assert_that
from behave import when, then, runner
from static.API.constants import marketdata
from utils.config_helper import get_public_asset_pairs_url
from utils.response_helper import get_trading_pair_from_server


@when("I make a request for {from_asset}/{to_asset} trading pair")
def get_trading_pair_info(context: runner.Context, from_asset: str, to_asset: str):
    context.response = requests.get(get_public_asset_pairs_url(from_asset, to_asset))


@then("Response contains a trading pair description content")
def response_trading_pair_description_general(context: runner.Context):
    pair_description = get_trading_pair_from_server(context)
    actual_pair_description_keys = list(pair_description.keys())
    expected_pair_description_keys = marketdata.TRADING_PAIR_DESCRIPTION_KEYS
    assert_that(actual_pair_description_keys).is_equal_to(expected_pair_description_keys)


@then("Response trading pair description contains valid altname {altname}")
def response_trading_pair_altname(context: runner.Context, altname:str):
    pair_description = get_trading_pair_from_server(context)
    assert_that(pair_description[marketdata.ALTNAME]).is_equal_to(altname)


@then("Response trading pair description contains valid {from_asset}/{to_asset} trading pair name")
def response_trading_pair_name(context: runner.Context, from_asset: str, to_asset: str):
    pair_description = get_trading_pair_from_server(context)
    expected_trading_pair_name = "{}/{}".format(from_asset, to_asset)
    assert_that(pair_description[marketdata.TRADING_PAIR_NAME]).is_equal_to(expected_trading_pair_name)


@then("Response trading pair description contains minimum order value {ordermin}")
def response_trading_pair_ordermin(context: runner.Context, ordermin: float):
    pair_description = get_trading_pair_from_server(context)
    assert_that(pair_description[marketdata.MINIMUM_ORDER]).is_equal_to(ordermin)

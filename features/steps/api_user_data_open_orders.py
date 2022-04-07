from assertpy import assert_that
from behave import when, then, runner
from static.API.constants import common, userdata
from static.API.constants.userdata import REQUEST_BODY_INCLUDE_TRADES_KEY, METHOD_OPEN_ORDERS, API_PRIVATE_PATH
from utils import request_helper
from utils.request_helper import generate_nonce


@when("I make a request for my open orders")
def request_user_data_open_orders(context: runner.Context):
    context.expected_open_orders = {}
    context.response = request_helper.authorized_post_request("{}{}".format(API_PRIVATE_PATH, METHOD_OPEN_ORDERS), {
        common.NONCE: generate_nonce(),
        REQUEST_BODY_INCLUDE_TRADES_KEY: True
    }, context.api_key, context.api_sec)


@then("Response contains correct open orders")
def response_user_data_open_orders(context: runner.Context):
    actual_open_orders = context.response.json()[common.RESPONSE_RESULT_KEY][userdata.RESPONSE_OPEN_ORDERS_KEY]
    expected_open_orders = context.expected_open_orders
    assert_that(actual_open_orders).is_equal_to(expected_open_orders)

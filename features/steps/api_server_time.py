import requests
from assertpy import assert_that
from behave import when, then, runner
from datetime import datetime, timezone
from static.API.constants.common import RESPONSE_RESULT_KEY
from static.API.constants.marketdata import RESPONSE_RESULT_HUMAN_READABLE_TIME_FORMAT, RESPONSE_RESULT_TIMESTAMP_NAME,\
    RESPONSE_RESULT_HUMAN_READABLE_TIME_NAME
from utils.config_helper import get_public_time_url


@when("I make a request for server time")
def get_server_time(context: runner.Context):
    context.response = requests.get(get_public_time_url())


@then("Response contains correct timestamp")
def response_timestamp(context: runner.Context):
    current_timestamp = int(datetime.now().timestamp())
    assert_that(context.response.json()[RESPONSE_RESULT_KEY][RESPONSE_RESULT_TIMESTAMP_NAME])\
        .is_close_to(current_timestamp, tolerance=1)


@then("Response contains correct human readable time")
def response_formatted_datetime(context: runner.Context):
    current_datetime = datetime.now().astimezone(timezone.utc)
    response_datetime = context.response.json()[RESPONSE_RESULT_KEY][RESPONSE_RESULT_HUMAN_READABLE_TIME_NAME]
    actual_datetime_formatted = datetime.strptime(response_datetime, RESPONSE_RESULT_HUMAN_READABLE_TIME_FORMAT)
    assert_that(actual_datetime_formatted).is_equal_to_ignoring_seconds(current_datetime)

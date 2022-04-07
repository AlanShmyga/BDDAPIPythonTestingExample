import os
from assertpy import assert_that
from behave import given, then, runner
from static.API.constants.common import API_BASE_URL, API_KEY, API_SEC
from static.API.constants.marketdata import RESPONSE_RESULT_ERROR_NAME


@given("I am a registered user")
def login_as_register_user(context: runner.Context):
    context.api_url = os.environ[API_BASE_URL]
    context.api_key = os.environ[API_KEY]
    context.api_sec = os.environ[API_SEC]


@then("Response contains a success status")
def response_status_success(context: runner.Context):
    assert_that(context.response.status_code).is_equal_to(200)


@then("Response contains no error")
def response_error_is_empty(context: runner.Context):
    assert_that(context.response.json()[RESPONSE_RESULT_ERROR_NAME]).is_empty()

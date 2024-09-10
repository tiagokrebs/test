from behave import given, when, then
from app.auth import create_token

@given('I am a user with id "{user_id}"')
def step_impl(context, user_id):
    context.user_id = user_id   

@when('I register')
def step_impl(context):
    context.response = context.app.post('/auth/register', json={'user_id': context.user_id})
    print(context.response)

@then('I should receive a token')
def step_impl(context): 
    assert context.response.status_code == 200
    assert 'token' in context.response.json

@then('I should be able to login with the token')
def step_impl(context):
    token = context.response.json['token']
    context.response = context.app.post('/auth/login', json={'token': token})
    assert context.response.status_code == 200
import requests
from behave import given, when, then

from check_website_inventory import CheckWebsiteInventory


@given(u'I want to go to a website')
def step_impl(self):
    assert CheckWebsiteInventory() is not None


@when(u'I enter "{url_request}" URL')
def step_impl(self, url_request):
    self.response = requests.get(url_request)
    self.response.raise_for_status()


@then(u'I see the "{message}" on the page')
def step_impl(self, message):
    assert CheckWebsiteInventory.check_label_on_website(self.response, message)
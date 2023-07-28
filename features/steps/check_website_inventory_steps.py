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


@when(u'I check the availability of the "{product_name}" item')
def step_impl(self, product_name):
    self.result = CheckWebsiteInventory.check_product_availability_on_website(self.response, product_name)


@then(u'I see the "{message}" on the page')
def step_impl(self, message):
    assert CheckWebsiteInventory.check_label_on_website(self.response, message)


@then(u'I see "{availability_text}" for the item')
def step_impl(self, availability_text):
    if availability_text == "Available":
        availability_text = ""
    assert self.result == availability_text

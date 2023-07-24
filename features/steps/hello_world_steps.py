from behave import given, when, then
from selenium import webdriver
from django.contrib.staticfiles.testing import LiveServerTestCase

from hello_world import HelloWorld


class HelloWorldTestCase(LiveServerTestCase):

    @given(u'I have a hello_world application')
    def step_impl(self):
        assert HelloWorld() is not None

    @given(u'I have a web server running')
    def step_impl(self):
        self.result = webdriver.Chrome()

    @when(u'I say hi')
    def step_impl(self):
        greeter = HelloWorld()
        self.result = greeter.say_hi()

    @when(u'I goto the hello world page')
    def step_impl(self):
        self.result.get('http://localhost:8000/hello_world')

    @then(u'I hear "{expected_result}"')
    def step_impl(self, expected_result):
        assert expected_result == self.result, 'Expect {} but got {}'.format(expected_result, self.result)

    @then(u'I see "{expected_result}" in the title')
    def step_impl(self, expected_result):
        assert expected_result in self.result.title, 'Expected {} but got {}'.format(expected_result, self.result.title)

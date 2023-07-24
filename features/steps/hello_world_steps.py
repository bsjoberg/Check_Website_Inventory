from behave import given, when, then

from hello_world import HelloWorld

class HelloWorldTestCase():

    @given(u'I have a hello_world application')
    def step_impl(self):
        assert HelloWorld() is not None

    @when(u'I say hi')
    def step_impl(self):
        greeter = HelloWorld()
        self.result = greeter.say_hi()

    @then(u'I hear "{expected_result}"')
    def step_impl(self, expected_result):
        assert expected_result == self.result, 'Expect {} but got {}'.format(expected_result, self.result)
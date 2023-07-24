Feature: Dev environment configured
  Scenario: Say hello
    Given I have a hello_world application
    When I say hi
    Then I hear "Hello World"
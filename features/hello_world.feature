Feature: Dev environment configured
  Scenario: Say hello
    Given I have a hello_world application
    When I say hi
    Then I hear "Hello World"

  Scenario: Say hello from local website
    Given I have a web server running
    When I goto the hello world page
    Then I see "Hello World" in the title
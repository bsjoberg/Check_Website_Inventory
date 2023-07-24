Feature: Sign-up for online bank account
  Scenario: Happy path sign up
    Given I navigated to the most amazing online bank website ever
    When I apply with valid details for a "checking" account
    Then I receive an "approved" notification
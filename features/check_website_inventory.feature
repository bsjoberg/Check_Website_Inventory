Feature: Check Inventory of Website
  Scenario: Go to website
    Given I want to go to a website
    When I enter "https://donut.media/collections/t-shirts/" URL
    Then I see the "Pop Up & Down Headlights Tee - White" on the page

  Scenario: Check if item is sold out
    Given I want to go to a website
    When I enter "https://donut.media/collections/t-shirts/" URL
    And I check the availability of the "Pop Up & Down Headlights Tee - White" item
    Then I see "Sold Out" on the page

  Scenario: Check if item is available
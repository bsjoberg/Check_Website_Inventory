Feature: Check Inventory of Website
  Scenario: Go to website
    Given I want to go to a website
    When I enter "https://donut.media/collections/t-shirts/products/pop-up-down-headlights-tee-white" URL
    Then I see the "Pop Up & Down Headlights Tee - White" on the page

  Scenario: Check if item is sold out

  Scenario: Check if item is available
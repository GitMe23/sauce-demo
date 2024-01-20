Feature: Logging in to the Sauce Demo inventory

  Scenario: Logging in with a valid password
   Given I open the Sauce Demo login page
    When I enter a valid user name and password
     And I click the login button
    Then I should be taken to the inventory page
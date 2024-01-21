Feature: Successful user journeys on the Sauce Demo website

  Scenario: The user can log in with a valid password
   Given I am on the Sauce Demo login page
    When I enter a valid user name and password
     And I click the login button
    Then I should be taken to the inventory page



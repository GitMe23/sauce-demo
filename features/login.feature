Feature: Logging in to the Sauce Demo inventory

  Scenario: Logging in with a valid password
   Given the user opens the Swag login page
    When the user enters a valid user name and password
     And the user clicks the login button
    Then the user should be on the inventory page
Feature: BBC Website Navigation

  Scenario: Navigate to SWAG login
   Given the user opens the Swag login page
    When the user enters a valid user name and password
     And the user clicks the login button
    Then the user should be in the inventory page